Name:           lua-luaposix-source
Version:        2.0
Release:        1%{?autorelease}
Summary:        Dummy package

BuildRequires:  lua-posix
BuildRequires:  perl
BuildRequires:  perl-RPM2


License:        LGPL
URL:            http://luarocks.org
Source0:        lua-luaposix.pl
BuildArch:      noarch

%description
%{summary}.

%(perl %{SOURCE0} %{lua_version})

%changelog
* Fri Mar 07 2025 tyk <fijik19@gmail.com> - 1.0-1
- Initial release
