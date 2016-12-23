#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Sphinx
Version  : 1.4.8
Release  : 27
URL      : http://pypi.debian.net/Sphinx/Sphinx-1.4.8.tar.gz
Source0  : http://pypi.debian.net/Sphinx/Sphinx-1.4.8.tar.gz
Summary  : Python documentation generator
Group    : Development/Tools
License  : Python-2.0
Requires: Sphinx-bin
Requires: Sphinx-python
BuildRequires : Jinja2
BuildRequires : MarkupSafe
BuildRequires : Pygments
BuildRequires : Sphinx
BuildRequires : docutils-python
BuildRequires : nose
BuildRequires : pbr
BuildRequires : pip
BuildRequires : py
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
This whole directory is there to test html_static_path.

%package bin
Summary: bin components for the Sphinx package.
Group: Binaries

%description bin
bin components for the Sphinx package.


%package python
Summary: python components for the Sphinx package.
Group: Default
Provides: sphinx-python
Requires: Jinja2
Requires: Pygments
Requires: docutils-python

%description python
python components for the Sphinx package.


%prep
%setup -q -n Sphinx-1.4.8

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sphinx-apidoc
/usr/bin/sphinx-autogen
/usr/bin/sphinx-build
/usr/bin/sphinx-quickstart

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
