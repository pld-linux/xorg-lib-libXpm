Summary:	X Pixmap library
Summary(pl):	Biblioteka X Pixmap
Name:		xorg-lib-libXpm
Version:	3.5.4.2
Release:	0.1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC4/lib/libXpm-%{version}.tar.bz2
# Source0-md5:	7a2590a8d7377952573747fad44acc2e
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
Obsoletes:	libXpm
Obsoletes:	xpm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Pixmap library.

%description -l pl
Biblioteka X Pixmap.

%package devel
Summary:	Header files for libXpm library
Summary(pl):	Pliki nag³ówkowe biblioteki libXpm
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libX11-devel
Obsoletes:	libXpm-devel
Obsoletes:	xpm-devel

%description devel
X Pixmap library.

This package contains the header files needed to develop programs that
use libXpm.

%description devel -l pl
Biblioteka X Pixmap.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libXpm.

%package static
Summary:	Static libXpm library
Summary(pl):	Biblioteka statyczna libXpm
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
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
Summary(pl):	Programy u¿ytkowe dla X Pixmap
Group:		X11/Development/Tools
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	xpm-progs

%description utils
X Pixmap utilities.

%description utils -l pl
Programy u¿ytkowe dla X Pixmap.

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
%doc AUTHORS CHANGES COPYING ChangeLog FAQ.html README.html
%attr(755,root,root) %{_libdir}/libXpm.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXpm.so
%{_libdir}/libXpm.la
%{_includedir}/X11/xpm.h
%{_pkgconfigdir}/xpm.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libXpm.a

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cxpm
%attr(755,root,root) %{_bindir}/sxpm
%{_mandir}/man1/cxpm.1x*
%{_mandir}/man1/sxpm.1x*
