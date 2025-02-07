#
# spec file for package python-requests-glob
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           python-requests-glob
Version:        1.0.0
Release:        0
Summary:        File transport adapter for Requests
License:        Apache-2.0
URL:            https://github.com/dashea/requests-file
Source:         requests_glob-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests-file >= 1.0.0}
BuildRequires:  %{python_module glob2 >= 0.1}
BuildRequires:  %{python_module sortedcontainers >= 1.0.0}
# /SECTION
BuildRequires:  fdupes
Requires:  python-glob2
Requires:       python-requests-file >= 1.0.0
Requires:       python-sortedcontainers >= 1.0.0
BuildArch:      noarch
%python_subpackages

%description
Requests-Glob
=============

Requests-Glob is a transport adapter for use with the `Requests`_ Python
library to allow local filesystem access via glob:\/\/ URLs.

To use:

.. code-block:: python

    import requests
    from requests_glob import GlobAdapter

    s = requests.Session()
    s.mount('glob://', GlobAdapter())

    resp = s.get('glob:///glob_expression')

Features
--------

- Will open and read local files
- Might set a Content-Length header
- That's about it

Also, url can contain query information, such as glob (yes - default, no),
glob_include_hidden (no - default, yes), glob_recursive (yes - default, no)

No encoding information is set in the response object, so be careful using
Response.text: the chardet library will be used to convert the file to a
unicode type and it may not detect what you actually want.

EACCES is converted to a 403 status code, and ENOENT is converted to a
404. All other IOError types are converted to a 400.

Contributing
------------

Contributions welcome! Feel free to open a pull request against
https://github.com/dashea/requests-glob

License
-------

To maximise compatibility with Requests, this code is licensed under the Apache
license. See LICENSE for more details.

.. _`Requests`: https://github.com/kennethreitz/requests


%prep
%autosetup -p1 -n requests_glob-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%{python_sitelib}/requests_glob.py
%pycache_only %{python_sitelib}/__pycache__/requests_glob.*.py*
%license LICENSE
%doc README.rst
%{python_sitelib}/requests_glob-%{version}.dist-info

%changelog
