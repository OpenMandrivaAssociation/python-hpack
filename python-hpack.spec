%define module	hpack

Name:		python-hpack
Version:	4.1.0
Release:	1
Summary:	Pure-Python HPACK header compression
Group:		Development/Python
License:	MIT
URL:		https://github.com/python-hyper/hpack
Source0:	%{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
This module contains a pure-Python HTTP/2 header encoding (HPACK) logic
for use in Python programs that implement HTTP/2. It also contains a
compatibility layer that automatically enables the use of nghttp2 if
it’s available.

%files
%doc CONTRIBUTORS.rst README.rst
%{python_sitelib}/%{module}/
%{python_sitelib}/%{module}-%{version}.dist-info
