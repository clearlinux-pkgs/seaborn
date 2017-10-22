#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : seaborn
Version  : 0.8.1
Release  : 2
URL      : https://pypi.python.org/packages/10/01/dd1c7838cde3b69b247aaeb61016e238cafd8188a276e366d36aa6bcdab4/seaborn-0.8.1.tar.gz
Source0  : https://pypi.python.org/packages/10/01/dd1c7838cde3b69b247aaeb61016e238cafd8188a276e366d36aa6bcdab4/seaborn-0.8.1.tar.gz
Summary  : Seaborn: statistical data visualization
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: seaborn-legacypython
Requires: seaborn-python3
Requires: seaborn-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Some of the features that seaborn offers are
        
        - Several built-in themes that improve on the default matplotlib aesthetics
        - Tools for choosing color palettes to make beautiful plots that reveal patterns in your data
        - Functions for visualizing univariate and bivariate distributions or for comparing them between subsets of data
        - Tools that fit and visualize linear regression models for different kinds of independent and dependent variables
        - Functions that visualize matrices of data and use clustering algorithms to discover structure in those matrices
        - A function to plot statistical timeseries data with flexible estimation and representation of uncertainty around the estimate
        - High-level abstractions for structuring grids of plots that let you easily build complex visualizations

%package legacypython
Summary: legacypython components for the seaborn package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the seaborn package.


%package python
Summary: python components for the seaborn package.
Group: Default
Requires: seaborn-legacypython
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
%setup -q -n seaborn-0.8.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1508633072
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1508633072
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
