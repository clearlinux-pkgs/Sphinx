#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x102C2C17498D6B9E (i.tkomiya@gmail.com)
#
Name     : Sphinx
Version  : 1.6.3
Release  : 42
URL      : https://pypi.debian.net/Sphinx/Sphinx-1.6.3.tar.gz
Source0  : https://pypi.debian.net/Sphinx/Sphinx-1.6.3.tar.gz
Source99 : https://pypi.debian.net/Sphinx/Sphinx-1.6.3.tar.gz.asc
Summary  : Python documentation generator
Group    : Development/Tools
License  : BSD-3-Clause-Clear
Requires: Sphinx-bin
Requires: Sphinx-python
Requires: Babel
Requires: Jinja2
Requires: Pygments
Requires: Whoosh
Requires: alabaster
Requires: colorama
Requires: docutils
Requires: html5lib
Requires: imagesize
Requires: pytest
Requires: python-mock
Requires: requests
Requires: setuptools
Requires: simplejson
Requires: six
Requires: snowballstemmer
BuildRequires : Jinja2
BuildRequires : MarkupSafe
BuildRequires : Pygments
BuildRequires : Sphinx
BuildRequires : Whoosh
BuildRequires : docutils-python
BuildRequires : nose
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
Sphinx is a tool that makes it easy to create intelligent and beautiful
        documentation for Python projects (or other documents consisting of multiple
        reStructuredText sources), written by Georg Brandl.  It was originally created
        for the new Python documentation, and has excellent facilities for Python
        project documentation, but C/C++ is supported as well, and more languages are
        planned.
        
        Sphinx uses reStructuredText as its markup language, and many of its strengths
        come from the power and straightforwardness of reStructuredText and its parsing
        and translating suite, the Docutils.

%package bin
Summary: bin components for the Sphinx package.
Group: Binaries

%description bin
bin components for the Sphinx package.


%package python
Summary: python components for the Sphinx package.
Group: Default
Provides: sphinx-python

%description python
python components for the Sphinx package.


%prep
%setup -q -n Sphinx-1.6.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1503080471
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1503080471
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
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
/usr/lib/python2*/*
/usr/lib/python3*/*
