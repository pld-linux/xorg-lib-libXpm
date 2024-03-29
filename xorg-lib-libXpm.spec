Summary:	X Pixmap library
Summary(pl.UTF-8):	Biblioteka X Pixmap
Name:		xorg-lib-libXpm
Version:	3.5.17
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/lib/libXpm-%{version}.tar.xz
# Source0-md5:	05b5667aadd476d77e9b5ba1a1de213e
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
# xgettext is used to create pots (although they are not used for anything yet)
BuildRequires:	gettext-tools
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-proto-xproto-devel >= 7.0.17
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
Suggests:	gzip
Suggests:	ncompress
Obsoletes:	libXpm < 1:3.5.2
Obsoletes:	xpm < 1.3.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Pixmap library.

%description -l pl.UTF-8
Biblioteka X Pixmap.

%package devel
Summary:	Header files for libXpm library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libXpm
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libX11-devel
Obsoletes:	libXpm-devel < 1:3.5.2
Obsoletes:	xpm-devel < 1.3.4

%description devel
X Pixmap library.

This package contains the header files needed to develop programs that
use libXpm.

%description devel -l pl.UTF-8
Biblioteka X Pixmap.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXpm.

%package static
Summary:	Static libXpm library
Summary(pl.UTF-8):	Biblioteka statyczna libXpm
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libXpm-static < 1:3.5.2
Obsoletes:	xpm-static < 1.3.4

%description static
X Pixmap library.

This package contains the static libXpm library.

%description static -l pl.UTF-8
Biblioteka X Pixmap.

Pakiet zawiera statyczną bibliotekę libXpm.

%package utils
Summary:	X Pixmap utilities
Summary(pl.UTF-8):	Programy użytkowe dla X Pixmap
Group:		X11/Development/Tools
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	xpm-progs < 1.3.4

%description utils
X Pixmap utilities.

%description utils -l pl.UTF-8
Programy użytkowe dla X Pixmap.

%prep
%setup -q -n libXpm-%{version}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	XPM_PATH_COMPRESS=/usr/bin/compress \
	XPM_PATH_GZIP=/usr/bin/gzip \
	XPM_PATH_UNCOMPRESS=/usr/bin/uncompress

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS.old README.md doc/{FAQ.html,README.html,xpm.PS.gz}
%attr(755,root,root) %{_libdir}/libXpm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXpm.so.4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXpm.so
%{_libdir}/libXpm.la
%{_includedir}/X11/xpm.h
%{_pkgconfigdir}/xpm.pc
%{_mandir}/man3/Xpm*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXpm.a

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cxpm
%attr(755,root,root) %{_bindir}/sxpm
%{_mandir}/man1/cxpm.1*
%{_mandir}/man1/sxpm.1*
