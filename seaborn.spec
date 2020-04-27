#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : seaborn
Version  : 0.10.1
Release  : 23
URL      : https://files.pythonhosted.org/packages/df/0e/817bea5f24e32cb014bf984f443bac54ab6c90ffc1ba0ca442065a7266b8/seaborn-0.10.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/df/0e/817bea5f24e32cb014bf984f443bac54ab6c90ffc1ba0ca442065a7266b8/seaborn-0.10.1.tar.gz
Summary  : seaborn: statistical data visualization
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: seaborn-license = %{version}-%{release}
Requires: seaborn-python = %{version}-%{release}
Requires: seaborn-python3 = %{version}-%{release}
Requires: matplotlib
Requires: numpy
Requires: pandas
Requires: scipy
BuildRequires : buildreq-distutils3
BuildRequires : matplotlib
BuildRequires : numpy
BuildRequires : pandas
BuildRequires : scipy

%description
seaborn: statistical data visualization
=======================================
<div class="row">

%package license
Summary: license components for the seaborn package.
Group: Default

%description license
license components for the seaborn package.


%package python
Summary: python components for the seaborn package.
Group: Default
Requires: seaborn-python3 = %{version}-%{release}

%description python
python components for the seaborn package.


%package python3
Summary: python3 components for the seaborn package.
Group: Default
Requires: python3-core
Provides: pypi(seaborn)
Requires: pypi(matplotlib)
Requires: pypi(numpy)
Requires: pypi(pandas)
Requires: pypi(scipy)

%description python3
python3 components for the seaborn package.


%prep
%setup -q -n seaborn-0.10.1
cd %{_builddir}/seaborn-0.10.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588008384
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/seaborn
cp %{_builddir}/seaborn-0.10.1/LICENSE %{buildroot}/usr/share/package-licenses/seaborn/491703eed0053aa6099241cbd04ca8120528087f
cp %{_builddir}/seaborn-0.10.1/licences/HUSL_LICENSE %{buildroot}/usr/share/package-licenses/seaborn/3284262e860227419fea272a5ab2a954dae740c0
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/seaborn/3284262e860227419fea272a5ab2a954dae740c0
/usr/share/package-licenses/seaborn/491703eed0053aa6099241cbd04ca8120528087f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
