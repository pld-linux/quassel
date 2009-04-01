Summary:	Quassel IRC is a modern, cross-platform, distributed IRC client based on the Qt4 framework
Summary(pl.UTF-8):	
Name:		quassel
Version:	0.4.1
Release:	0.1
License:	GPL
Group:		Applications/Communications
Source0:	http://www.quassel-irc.org/pub/%{name}-%{version}.tar.bz2
# Source0-md5:	bf89e3ff2e12c64d9cf8b1445e46039f
URL:		http://www.quassel-irc.org/
BuildRequires:	automoc4
BuildRequires:	cmake
BuildRequires:	gettext-devel
BuildRequires:	kde4-kdepimlibs-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl.UTF-8

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DLIB_INSTALL_DIR=%{_libdir} \
	-DCMAKE_BUILD_TYPE=%{!?debug:release}%{?debug:debug} \
	-DWITH_KDE=ON \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
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
%{_iconsdir}/hicolor/48x48/apps/quassel.png
%{_pixmapsdir}/quassel.png
%{_desktopdir}/kde4/quassel.desktop
%{_desktopdir}/kde4/quasselclient.desktop
