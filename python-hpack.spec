%define module	hpack

Name:		python-%{module}
Version:	4.0.0
Release:	3
Summary:	Pure-Python HPACK header compression
Group:		Development/Python
License:	MIT
URL:		http://hyper.rtfd.org/
Source0:	https://pypi.io/packages/source/h/hpack/%{module}-%{version}.tar.gz

BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(setuptools)
%{?python_provide:%python_provide python3-%{module}}

BuildArch:	noarch

%files
%doc CONTRIBUTORS.rst LICENSE README.rst
%{python_sitelib}/%{module}/
%{python_sitelib}/%{module}-%{version}-py%{python_version}.egg-info/

#----------------------------------------------------------------------------

%description
This module contains a pure-Python HTTP/2 header encoding (HPACK) logic
for use in Python programs that implement HTTP/2. It also contains a
compatibility layer that automatically enables the use of nghttp2 if
it’s available.

%prep
%setup -q -n %{module}-%{version}

# Remove bundled egg-info
rm -rf %{module}.egg-info

%build
%py_build

%install
%py_install
