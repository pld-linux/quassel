# TODO
# - lang tag translations
#
# Conditional build:
%bcond_with	kde		# Integration with the KDE Frameworks runtime environment

%define		qtver	5.5.0
Summary:	Modern, cross-platform, distributed IRC client based on the Qt4 framework
Summary(pl.UTF-8):	Nowoczesny, wieloplatformowy i rozproszony klient IRC oparty na bibliotece Qt4
Name:		quassel
Version:	0.14.0
Release:	2
License:	GPL v2, GPL v3
Group:		Applications/Communications
Source0:	https://www.quassel-irc.org/pub/%{name}-%{version}.tar.bz2
# Source0-md5:	abc3843021840a00d9d83778a2c1211b
URL:		https://www.quassel-irc.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Multimedia-devel >= %{qtver}
BuildRequires:	Qt5Sql-devel >= %{qtver}
BuildRequires:	Qt5Svg-devel >= %{qtver}
%ifarch x32
BuildRequires:	Qt5WebKit-devel >= %{qtver}
%else
BuildRequires:	Qt5WebEngine-devel >= %{qtver}
%endif
BuildRequires:	boost-devel >= 1.54
BuildRequires:	cmake >= 3.5
%if %{with kde}
BuildRequires:	kf5-extra-cmake-modules
BuildRequires:	kf5-kconfigwidgets-devel
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-knotifications-devel
BuildRequires:	kf5-knotifyconfig-devel
BuildRequires:	kf5-ktextwidgets-devel
BuildRequires:	kf5-kwidgetsaddons
BuildRequires:	kf5-kxmlgui-devel
BuildRequires:	kf5-sonnet-devel
%endif
BuildRequires:	libdbusmenu-qt5-devel
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	phonon-qt5-devel
BuildRequires:	pkgconfig
BuildRequires:	qca-qt5-devel
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	qt5-linguist >= %{qtver}
BuildRequires:	qt5-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	sed >= 4.0
BuildRequires:	zlib-devel
Suggests:	Qt5Sql-sqldriver-sqlite3 >= %{qtver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quassel IRC is modern Internet chat client. It allows one (or
multiple) client(s) can attach to and detach from a central core
(distributed), but also can act plain client.

%description -l pl.UTF-8
Quassel IRC jest nowoczesnym klientem rozmów w Internecie. Pozwala na
podłączanie się i odłączanie wielu klientów od centralnego rdzenia
(rozproszony), ale również może zachowywać się jak zwyczajny klient.

%prep
%setup -q

%{__sed} -E -i -e '1s,#!\s*/usr/bin/env\s+perl(\s|$),#!%{__perl}\1,' \
      data/scripts/inxi \
      data/scripts/mpris

%build
install -d build
cd build
%cmake \
	-DEMBED_DATA=OFF \
%if %{with kde}
	-DWITH_KDE=ON \
%else
	-DWITH_KDE=OFF \
	-DECM_FOUND=NO \
%endif
	-DWITH_LIBINDICATE=ON \
%ifarch x32
	-DWITH_WEBKIT=ON \
	-DWITH_WEBENGINE=OFF \
%else
	-DWITH_WEBKIT=OFF \
	-DWITH_WEBENGINE=ON \
%endif
	..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/quassel
%attr(755,root,root) %{_bindir}/quasselclient
%attr(755,root,root) %{_bindir}/quasselcore
%attr(755,root,root) %{_libdir}/libquassel-client.so.0.14.0
%attr(755,root,root) %{_libdir}/libquassel-common.so.0.14.0
%attr(755,root,root) %{_libdir}/libquassel-core.so.0.14.0
%attr(755,root,root) %{_libdir}/libquassel-qtui.so.0.14.0
%attr(755,root,root) %{_libdir}/libquassel-uisupport.so.0.14.0
%{_datadir}/%{name}
%{_iconsdir}/hicolor/*/*/*.png
%{_desktopdir}/quassel.desktop
%{_desktopdir}/quasselclient.desktop
%{?with_kde:%{_datadir}/knotifications5/quassel.notifyrc}
