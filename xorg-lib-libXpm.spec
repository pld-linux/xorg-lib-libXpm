
#
Summary:	X Pixmap library
Summary(pl):	Biblioteka X Pixmap
Name:		xorg-lib-libXpm
Version:	3.5.2
Release:	0.02
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/lib/libXpm-%{version}.tar.bz2
# Source0-md5:	681b4ceb8de4d7cf6180f05d3b3ef1a5
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	pkg-config
BuildRequires:	xorg-util-util-macros
Obsoletes:	libXpm
Obsoletes:	xpm
BuildRoot:	%{tmpdir}/libXpm-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
X Pixmap library.

%description -l pl
Biblioteka X Pixmap.


%package devel
Summary:	Header files libXpm development
Summary(pl):	Pliki nag³ówkowe do biblioteki libXpm
Group:		X11/Development/Libraries
Requires:	xorg-lib-libXpm = %{version}-%{release}
Requires:	xorg-lib-libX11-devel
Obsoletes:	libXpm-devel
Obsoletes:	xpm-devel

%description devel
X Pixmap library.

This package contains the header files needed to develop programs that
use these libXpm.

%description devel -l pl
Biblioteka X Pixmap.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libXpm.


%package static
Summary:	Static libXpm libraries
Summary(pl):	Biblioteki statyczne libXpm
Group:		Development/Libraries
Requires:	xorg-lib-libXpm-devel = %{version}-%{release}
Obsoletes:	libXpm-static
Obsoletes:	xpm-static

%description static
X Pixmap library.

This package contains the static libXpm library.

%description static -l pl
Biblioteka X Pixmap.

Pakiet zawiera statyczn± bibliotekê libXpm.


%package utils
Summary:	X Pixmap utilities
Summary(pl):	Programy uzytkowe dla X Pixmap
Group:		Development/Libraries
Requires:	xorg-lib-libXpm-devel = %{version}-%{release}
Obsoletes:	xpm-progs

%description utils
X Pixmap utilities.

%description utils -l pl
Programy uzytkowe dla X Pixmap.


%prep
%setup -q -n libXpm-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig


%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ.html README.html
%attr(755,root,wheel) %{_libdir}/libXpm.so.*


%files devel
%defattr(644,root,root,755)
%{_includedir}/X11/xpm.h
%{_libdir}/libXpm.la
%attr(755,root,wheel) %{_libdir}/libXpm.so
%{_pkgconfigdir}/xpm.pc


%files static
%defattr(644,root,root,755)
%{_libdir}/libXpm.a


%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
