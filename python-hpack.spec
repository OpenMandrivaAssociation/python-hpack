%define module	hpack

Name:		python-%{module}
Version:	3.0.0
Release:	%mkrel 3
Summary:	Pure-Python HPACK header compression
Group:		Development/Python
License:	MIT
URL:		http://hyper.rtfd.org/
Source0:	https://pypi.io/packages/source/h/hpack/%{module}-%{version}.tar.gz
BuildArch:	noarch

%description
This module contains a pure-Python HTTP/2 header encoding (HPACK) logic
for use in Python programs that implement HTTP/2. It also contains a
compatibility layer that automatically enables the use of nghttp2 if
it’s available.

%package -n	python3-%{module}
Summary:	Pure-Python HPACK header compression
Group:		Development/Python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(setuptools)
%{?python_provide:%python_provide python3-%{module}}

%description -n	python3-%{module}
This module contains a pure-Python HTTP/2 header encoding (HPACK) logic
for use in Python programs that implement HTTP/2. It also contains a
compatibility layer that automatically enables the use of nghttp2 if
it’s available.

This is the Python 3 version of the package.

%prep
%setup -q -n %{module}-%{version}

# Remove bundled egg-info
rm -rf %{module}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{module}
%doc CONTRIBUTORS.rst HISTORY.rst LICENSE README.rst
%{python3_sitelib}/%{module}/
%{python3_sitelib}/%{module}-%{version}-py%{python3_version}.egg-info/
