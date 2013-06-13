Summary:	Modern, cross-platform, distributed IRC client based on the Qt4 framework
Summary(pl.UTF-8):	Nowoczesny, wieloplatformowy i rozproszony klient IRC oparty na bibliotece Qt4
Name:		quassel
Version:	0.9.0
Release:	1
License:	GPL v2, GPL v3
Group:		Applications/Communications
Source0:	http://www.quassel-irc.org/pub/%{name}-%{version}.tar.bz2
# Source0-md5:	29b843f18d703abfadb8fc729ca1df11
URL:		http://www.quassel-irc.org/
BuildRequires:	QtCore-devel
BuildRequires:	QtSql-backend
BuildRequires:	QtSql-devel
BuildRequires:	QtSvg-devel
BuildRequires:	QtWebKit-devel
BuildRequires:	QtXmlPatterns-devel
BuildRequires:	automoc4
BuildRequires:	cmake
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	phonon-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	sed >= 4.0
Suggests:	QtSql-sqlite3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quassel IRC is modern Internet chat client. It allows one (or
multiple) client(s) can attach to and detach from a central core
(distributed), but also can act plain client. It is developed for and
tested on Linux®, Windows®, and MacOS X®, and should work on other
platforms supporting Qt4 library (cross-platform).

%description -l pl.UTF-8
Quassel IRC jest nowoczesnym klientem rozmów w Internecie. Pozwala na
podłączanie się i odłączanie wielu klientów od centralnego rdzenia
(rozproszony), ale również może zachowywać się jak zwyczajny klient.
Jest rozwijany i testowany na platformy Linux®, Windows® oraz MacOS
X®, powinien także działać na innych platformach wspierających
bibliotekę Qt4 (wieloplatformowy).

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DWITH_KDE=ON \
	..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir} \
        kde_libs_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/quassel
%{_iconsdir}/hicolor/*/*/*.png
%{_pixmapsdir}/quassel.png
%{_desktopdir}/quassel.desktop
%{_desktopdir}/quasselclient.desktop
