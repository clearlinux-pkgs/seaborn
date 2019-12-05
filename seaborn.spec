#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : seaborn
Version  : 0.9.0
Release  : 18
URL      : https://files.pythonhosted.org/packages/7a/bf/04cfcfc9616cedd4b5dd24dfc40395965ea9f50c1db0d3f3e52b050f74a5/seaborn-0.9.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/7a/bf/04cfcfc9616cedd4b5dd24dfc40395965ea9f50c1db0d3f3e52b050f74a5/seaborn-0.9.0.tar.gz
Summary  : seaborn: statistical data visualization
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: seaborn-python3
Requires: seaborn-license
Requires: seaborn-python
Requires: matplotlib
Requires: numpy
Requires: pandas
Requires: scipy
BuildRequires : buildreq-distutils3

%description
seaborn: statistical data visualization
=======================================
<div class="row">
<a href=https://seaborn.pydata.org/examples/anscombes_quartet.html>
<img src="https://seaborn.pydata.org/_static/anscombes_quartet_thumb.png" height="135" width="135">
</a>

%package license
Summary: license components for the seaborn package.
Group: Default

%description license
license components for the seaborn package.


%package python
Summary: python components for the seaborn package.
Group: Default
Requires: seaborn-python3

%description python
python components for the seaborn package.


%package python3
Summary: python3 components for the seaborn package.
Group: Default
Requires: python3-core

%description python3
python3 components for the seaborn package.


%prep
%setup -q -n seaborn-0.9.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533051484
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/seaborn
cp LICENSE %{buildroot}/usr/share/doc/seaborn/LICENSE
cp licences/HUSL_LICENSE %{buildroot}/usr/share/doc/seaborn/licences_HUSL_LICENSE
cp licences/SIX_LICENSE %{buildroot}/usr/share/doc/seaborn/licences_SIX_LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/seaborn/LICENSE
/usr/share/doc/seaborn/licences_HUSL_LICENSE
/usr/share/doc/seaborn/licences_SIX_LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
