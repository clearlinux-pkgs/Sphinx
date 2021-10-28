#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x102C2C17498D6B9E (i.tkomiya@gmail.com)
#
Name     : Sphinx
Version  : 4.2.0
Release  : 166
URL      : https://files.pythonhosted.org/packages/c4/55/38d9661f2eca2a0d4cf891de61d8f9bdc9e8711b473012f36d90009677c5/Sphinx-4.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/c4/55/38d9661f2eca2a0d4cf891de61d8f9bdc9e8711b473012f36d90009677c5/Sphinx-4.2.0.tar.gz
Source1  : https://files.pythonhosted.org/packages/c4/55/38d9661f2eca2a0d4cf891de61d8f9bdc9e8711b473012f36d90009677c5/Sphinx-4.2.0.tar.gz.asc
Summary  : Python documentation generator
Group    : Development/Tools
License  : MIT
Requires: Sphinx-bin = %{version}-%{release}
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
BuildRequires : virtualenv

%description
========
Sphinx
========
.. image:: https://img.shields.io/pypi/v/sphinx.svg
:target: https://pypi.org/project/Sphinx/
:alt: Package on PyPI

%package bin
Summary: bin components for the Sphinx package.
Group: Binaries

%description bin
bin components for the Sphinx package.


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
Provides: pypi(sphinx)
Requires: pypi(alabaster)
Requires: pypi(babel)
Requires: pypi(docutils)
Requires: pypi(imagesize)
Requires: pypi(jinja2)
Requires: pypi(packaging)
Requires: pypi(pygments)
Requires: pypi(requests)
Requires: pypi(setuptools)
Requires: pypi(snowballstemmer)
Requires: pypi(sphinxcontrib_applehelp)
Requires: pypi(sphinxcontrib_devhelp)
Requires: pypi(sphinxcontrib_htmlhelp)
Requires: pypi(sphinxcontrib_jsmath)
Requires: pypi(sphinxcontrib_qthelp)
Requires: pypi(sphinxcontrib_serializinghtml)

%description python3
python3 components for the Sphinx package.


%prep
%setup -q -n Sphinx-4.2.0
cd %{_builddir}/Sphinx-4.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635460493
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

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
