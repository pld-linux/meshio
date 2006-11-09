Summary:	Library for the loading of 3D model files
Summary(pl):	Biblioteka do ³adowania plików z modelami 3D
Name:		meshio
Version:	0.2.0
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.3dwm.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	970709a30d5a2139bcdb8b57076841a6
URL:		http://www.3dwm.org/frameset.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d
Obsoletes:	libmeshio0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MeshIO is a simple C++ library for the loading of 3D model files.
Currently, MeshIO only supports plain .3DS files as well as its native
.RAW format. MeshIO will undergo a major redesign in the future.

%description -l pl
MeshIO jest prost± bibliotek± napisana w C++, s³u¿±c± do ³adowania
plików z modelami 3D. W chwili obecnej, MeshIO wspiera tylko czyste
pliki .3DS oraz swój natywny format .RAW. MeshIO zostanie gruntownie
przeprojektowane w przysz³o¶ci.

%package devel
Summary:	Development files for MeshIO
Summary(pl):	Pliki nag³ówkowe dla MeshIO
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libmeshio0-devel

%description devel
Development files for meshio.

%description devel -l pl
Pliki nag³ówkowe dla meshio.

%package static
Summary:	Static meshio library
Summary(pl):	Statyczna biblioteka meshio
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static meshio library.

%description static -l pl
Statyczna biblioteka meshio.

%prep
%setup -q

cat > acconfig.h <<EOF
#undef MAJOR_VERSION
#undef MINOR_VERSION
#undef PATCH_LEVEL
EOF

%build
rm -f missing
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
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_includedir}/MeshIO

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
