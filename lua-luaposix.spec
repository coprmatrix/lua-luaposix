%define luarocks_pkg_name luaposix
%define luarocks_pkg_version 33.4.0-1
%define luarocks_pkg_prefix luaposix-33.4.0-1
%define luarocks_pkg_major 33.4.0
%define luarocks_pkg_minor 1

Name: lua-luaposix
Version: %{luarocks_pkg_major}
Release: %{luarocks_pkg_minor}
Summary: Lua bindings for POSIX
Url: http://github.com/luaposix/luaposix/
License: MIT/X11
Source0: luaposix-33.4.0-1.tar.gz
Source1: luaposix-33.4.0-1.rockspec
BuildRequires: lua-rpm-macros
Requires(postun): alternatives
Requires(post): alternatives
Provides: %{luadist %{luarocks_pkg_name} = %{luarocks_pkg_version}}
%define luarocks_pkg_build() %{_require_luadist}export USER='' ; lua%{1} build-aux/luke PREFIX=%{_prefix} all ; lua%{1} build-aux/luke PREFIX=.lua%{1} INST_LIBDIR=.lua%{1}/lib INST_LUADIR=.lua%{1}/lua install ; create_luarock --srcdir .lua%{1} --rockspec '%{luarocks_pkg_rockspec}' --outdir .luarocks/lua%{1} 
%global __luarocks_requires %{_bindir}/true
%global __luarocks_provides %{_bindir}/true
Requires: %{luadist lua >= 5.1, < 5.5}
Requires: %{luadist bit32}
%{?luarocks_subpackages:%luarocks_subpackages -f}

%description
      A library binding various POSIX APIs. POSIX is the IEEE Portable
      Operating System Interface standard. luaposix is based on lposix.
   

%prep
%autosetup -p1 -n %{luarocks_pkg_prefix}
%luarocks_prep

%generate_buildrequires
%{?luarocks_buildrequires_echo}
%if %{with check}
%luarocks_generate_buildrequires -c -b
%else
%luarocks_generate_buildrequires -b 
%endif
echo python3-lua.rock

%build
%{?custom_build}
%if %{defined luarocks_subpackages_build}
%{luarocks_subpackages_build}
%else
%if %{defined luarocks_pkg_build}
%luarocks_pkg_build %{lua_version}
%else
%luarocks_build --local
%endif
%endif

%install
%{?custom_install}
%if %{defined luarocks_subpackages_install}
%{luarocks_subpackages_install}
%else
%if %{defined luarocks_pkg_install}
%luarocks_pkg_install %{lua_version}
%else
%luarocks_install %{luarocks_pkg_prefix}.*.rock
%endif
%endif
%{?lua_generate_file_list}

%check
%if %{with check}
%{?luarocks_check}
%endif

%files %{?lua_files}%{!?lua_files:-f lua_files.list}