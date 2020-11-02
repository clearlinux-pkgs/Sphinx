#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x102C2C17498D6B9E (i.tkomiya@gmail.com)
#
Name     : Sphinx
Version  : 3.3.0
Release  : 143
URL      : https://files.pythonhosted.org/packages/e7/66/e9bc0151c3d796f2623a28f9596a0b24865976418cdbae2efd6c6a8d6ca5/Sphinx-3.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/e7/66/e9bc0151c3d796f2623a28f9596a0b24865976418cdbae2efd6c6a8d6ca5/Sphinx-3.3.0.tar.gz
Source1  : https://files.pythonhosted.org/packages/e7/66/e9bc0151c3d796f2623a28f9596a0b24865976418cdbae2efd6c6a8d6ca5/Sphinx-3.3.0.tar.gz.asc
Summary  : Python documentation generator
Group    : Development/Tools
License  : MIT
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
Sphinx
        ========

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
%setup -q -n Sphinx-3.3.0
cd %{_builddir}/Sphinx-3.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604342143
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Sphinx
cp %{_builddir}/Sphinx-3.3.0/LICENSE %{buildroot}/usr/share/package-licenses/Sphinx/65a5b77947ac426cc1fa580237fdb3e6c5486196
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
/usr/share/package-licenses/Sphinx/65a5b77947ac426cc1fa580237fdb3e6c5486196

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
