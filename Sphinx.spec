#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x102C2C17498D6B9E (i.tkomiya@gmail.com)
#
Name     : Sphinx
Version  : 2.3.1
Release  : 120
URL      : https://files.pythonhosted.org/packages/d3/32/96bbaccabdb6d0d1cec1067d71bd50cd18e93aed18216eafbe2afb85ac2d/Sphinx-2.3.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/d3/32/96bbaccabdb6d0d1cec1067d71bd50cd18e93aed18216eafbe2afb85ac2d/Sphinx-2.3.1.tar.gz
Source1  : https://files.pythonhosted.org/packages/d3/32/96bbaccabdb6d0d1cec1067d71bd50cd18e93aed18216eafbe2afb85ac2d/Sphinx-2.3.1.tar.gz.asc
Summary  : Free open-source SQL full-text search engine.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: Sphinx-bin = %{version}-%{release}
Requires: Sphinx-license = %{version}-%{release}
Requires: Sphinx-python = %{version}-%{release}
Requires: Sphinx-python3 = %{version}-%{release}
Requires: Babel
Requires: Jinja2
Requires: Pygments
Requires: Whoosh
Requires: alabaster
Requires: colorama
Requires: docutils
Requires: imagesize
Requires: packaging
Requires: python-future
Requires: recommonmark
Requires: requests
Requires: setuptools
Requires: snowballstemmer
Requires: sphinxcontrib-applehelp
Requires: sphinxcontrib-devhelp
Requires: sphinxcontrib-htmlhelp
Requires: sphinxcontrib-jsmath
Requires: sphinxcontrib-qthelp
Requires: sphinxcontrib-serializinghtml
Requires: sphinxcontrib-websupport
Requires: typing
BuildRequires : Babel
BuildRequires : Jinja2
BuildRequires : MarkupSafe
BuildRequires : Pygments
BuildRequires : Sphinx
BuildRequires : Whoosh
BuildRequires : alabaster
BuildRequires : buildreq-distutils3
BuildRequires : colorama
BuildRequires : docutils
BuildRequires : docutils-python
BuildRequires : imagesize
BuildRequires : nose
BuildRequires : packaging
BuildRequires : pluggy
BuildRequires : py
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-future
BuildRequires : recommonmark
BuildRequires : requests
BuildRequires : setuptools
BuildRequires : setuptools-python
BuildRequires : snowballstemmer
BuildRequires : sphinxcontrib-applehelp
BuildRequires : sphinxcontrib-devhelp
BuildRequires : sphinxcontrib-htmlhelp
BuildRequires : sphinxcontrib-jsmath
BuildRequires : sphinxcontrib-qthelp
BuildRequires : sphinxcontrib-serializinghtml
BuildRequires : sphinxcontrib-websupport
BuildRequires : tox
BuildRequires : typing
BuildRequires : virtualenv

%description
:orphan:
Tutorial examples
=================
This directory contains a number of examples used in the tutorials. These are
intended to be increasingly complex to demonstrate the various features of
Sphinx, but should aim to be as complicated as necessary but no more.
Individual sections are referenced by line numbers, meaning if you make changes
to the source files, you should update the references in the documentation
accordingly.

%package bin
Summary: bin components for the Sphinx package.
Group: Binaries
Requires: Sphinx-license = %{version}-%{release}

%description bin
bin components for the Sphinx package.


%package license
Summary: license components for the Sphinx package.
Group: Default

%description license
license components for the Sphinx package.


%package python
Summary: python components for the Sphinx package.
Group: Default
Requires: Sphinx-python3 = %{version}-%{release}
Provides: sphinx-python

%description python
python components for the Sphinx package.


%package python3
Summary: python3 components for the Sphinx package.
Group: Default
Requires: python3-core

%description python3
python3 components for the Sphinx package.


%prep
%setup -q -n Sphinx-2.3.1
cd %{_builddir}/Sphinx-2.3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1577143565
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Sphinx
cp %{_builddir}/Sphinx-2.3.1/LICENSE %{buildroot}/usr/share/package-licenses/Sphinx/af18f178505e4b98db7dcf87908f2536117a2ecd
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sphinx-apidoc
/usr/bin/sphinx-autogen
/usr/bin/sphinx-build
/usr/bin/sphinx-quickstart

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Sphinx/af18f178505e4b98db7dcf87908f2536117a2ecd

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
