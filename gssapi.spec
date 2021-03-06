#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gssapi
Version  : 1.7.2
Release  : 7
URL      : https://files.pythonhosted.org/packages/e4/4d/03fcc6a2d052920336069df97866d7b506556ed9f3a5ee2ca1e0cbad45d4/gssapi-1.7.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/e4/4d/03fcc6a2d052920336069df97866d7b506556ed9f3a5ee2ca1e0cbad45d4/gssapi-1.7.2.tar.gz
Summary  : Python GSSAPI Wrapper
Group    : Development/Tools
License  : ISC
Requires: gssapi-license = %{version}-%{release}
Requires: gssapi-python = %{version}-%{release}
Requires: gssapi-python3 = %{version}-%{release}
Requires: decorator
BuildRequires : buildreq-distutils3
BuildRequires : decorator
BuildRequires : krb5-dev

%description
Python-GSSAPI
        =============

%package license
Summary: license components for the gssapi package.
Group: Default

%description license
license components for the gssapi package.


%package python
Summary: python components for the gssapi package.
Group: Default
Requires: gssapi-python3 = %{version}-%{release}

%description python
python components for the gssapi package.


%package python3
Summary: python3 components for the gssapi package.
Group: Default
Requires: python3-core
Provides: pypi(gssapi)
Requires: pypi(decorator)

%description python3
python3 components for the gssapi package.


%prep
%setup -q -n gssapi-1.7.2
cd %{_builddir}/gssapi-1.7.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635738086
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gssapi
cp %{_builddir}/gssapi-1.7.2/LICENSE.txt %{buildroot}/usr/share/package-licenses/gssapi/dcebddb4fa716078a910d0fa8b5761106c76738e
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gssapi/dcebddb4fa716078a910d0fa8b5761106c76738e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
