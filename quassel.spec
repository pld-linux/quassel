# TODO
# - lang tag translations
%define		qtver	4.6.0
Summary:	Modern, cross-platform, distributed IRC client based on the Qt4 framework
Summary(pl.UTF-8):	Nowoczesny, wieloplatformowy i rozproszony klient IRC oparty na bibliotece Qt4
Name:		quassel
Version:	0.12.2
Release:	0.1
License:	GPL v2, GPL v3
Group:		Applications/Communications
Source0:	http://www.quassel-irc.org/pub/%{name}-%{version}.tar.bz2
# Source0-md5:	f5473a9c5927a0e8cb3a204ced887aa8
URL:		http://www.quassel-irc.org/
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtSql-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	QtWebKit-devel >= %{qtver}
BuildRequires:	automoc4
BuildRequires:	cmake >= 2.8.9
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	openssl-devel
BuildRequires:	phonon-devel
BuildRequires:	pkgconfig
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	sed >= 4.0
Suggests:	QtSql-sqlite3 >= %{qtver}
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

%build
install -d build
cd build
%cmake \
	-DEMBED_DATA=OFF \
	-DWITH_CRYPT=ON \
	-DWITH_DBUS=ON \
	-DWITH_KDE=ON \
	-DWITH_LIBINDICATE=ON \
	-DWITH_OPENSSL=ON \
	-DWITH_OXYGEN=ON \
	-DWITH_PHONON=ON \
	-DWITH_QT5=OFF \
	-DWITH_SYSLOG=ON \
	-DWITH_WEBKIT=ON \
	..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/quassel
%attr(755,root,root) %{_bindir}/quasselclient
%attr(755,root,root) %{_bindir}/quasselcore
%{_datadir}/%{name}
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svgz
%{_pixmapsdir}/quassel.png
%{_desktopdir}/kde4/quassel.desktop
%{_desktopdir}/kde4/quasselclient.desktop
