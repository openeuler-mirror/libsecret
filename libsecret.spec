%global release_version %%(echo %{version} | awk -F. '{print $1"."$2}')
Name:           libsecret
Version:        0.20.3
Release:        1
Summary:        Library for storing and retrieving passwords and other secrets
License:        LGPLv2+
URL:            https://wiki.gnome.org/Projects/Libsecret
Source0:        http://download.gnome.org/sources/libsecret/%{release_version}/libsecret-%{version}.tar.xz

BuildRequires:  glib2-devel gobject-introspection-devel intltool vala gtk-doc
BuildRequires:  libgcrypt-devel >= 1.2.2 libxslt-devel docbook-style-xsl valgrind-devel

Provides:       bundled(egglib)

%description
A GObject-based library for accessing the Secret Service API of the freedesktop.org
project, a cross-desktop effort to access passwords, tokens and other types of secrets.
libsecret provides a convenient wrapper for these methods so consumers do not have to
call the low-level DBus methods.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	help
Summary:	help package of %{name} that include files

%description	help
document files for %{name}

%prep
%autosetup -p1

rm -rf build/valgrind/


%build
%configure --disable-static
make

%install
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'

%find_lang libsecret

%ldconfig_scriptlets

%files -f libsecret.lang
%license COPYING
%{_libdir}/libsecret-1.so.*
%{_libdir}/girepository-1.0/Secret-1.typelib
%{_bindir}/secret-tool
%doc AUTHORS NEWS README

%files devel
%{_includedir}/libsecret-1/
%{_libdir}/libsecret-1.so
%{_libdir}/pkgconfig/libsecret-1.pc
%{_libdir}/pkgconfig/libsecret-unstable.pc
%{_datadir}/gir-1.0/Secret-1.gir
%{_datadir}/vala/vapi/libsecret-1.deps
%{_datadir}/vala/vapi/libsecret-1.vapi

%files help
%doc %{_mandir}/man1/secret-tool.1.gz
%doc %{_datadir}/gtk-doc/

%changelog
* Sat Aug 22 2020 shixuantong <shixuantong@huawei.com> - 0.20.3-1
- update version to 0.20.3

* Fri Sep 27 2019 openEuler Buildteam <buildteam@openeuler.org> - 0.18.6-4
- Correct requires

* Fri Sep 27 2019 openEuler Buildteam <buildteam@openeuler.org> - 0.18.6-3
- Format BuildRequires

* Fri Sep 27 2019 openEuler Buildteam <buildteam@openeuler.org> - 0.18.6-2
- Adjust requires

* Fri Sep 6 2019 openEuler Buildteam <buildteam@openeuler.org> - 0.18.6-1
- Package init
