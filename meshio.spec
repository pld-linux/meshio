Name:		meshio
Summary:	Library for the loading of 3D model files
Summary(pl):	Biblioteka do ³adowania plików z modelami 3D
Version:	0.2.0
Release:	0.1
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.3dwm.org/download/%{name}-%{version}.tar.gz
# Source0-md5: 970709a30d5a2139bcdb8b57076841a6
URL:		http://www.3dwm.org/frameset.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libmeshio0

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
Requires:	%{name} = %{version}
Obsoletes:	libmeshio0-devel

%description devel
Development files for meshio.

%description devel -l pl
Pliki nag³ówkowe dla meshio.

%package static
Summary:	Static files for meshio
Summary(pl):	Statyczne biblioteki dla meshio
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static files for libmeshio.

%description static -l pl
Statyczne biblioteki dla meshio.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%build
rm -f missing
%{__aclocal} -I .
%{__libtoolize}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README NEWS
%attr(755,root,root) %{_libdir}/*.so.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/MeshIO

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
