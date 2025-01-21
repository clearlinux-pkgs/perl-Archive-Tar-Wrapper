#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v18
# autospec commit: f35655a
#
Name     : perl-Archive-Tar-Wrapper
Version  : 0.42
Release  : 37
URL      : https://cpan.metacpan.org/authors/id/H/HA/HAARG/Archive-Tar-Wrapper-0.42.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/H/HA/HAARG/Archive-Tar-Wrapper-0.42.tar.gz
Summary  : "API wrapper around the 'tar' utility"
Group    : Development/Tools
License  : GPL-3.0
Requires: perl-Archive-Tar-Wrapper-license = %{version}-%{release}
Requires: perl-Archive-Tar-Wrapper-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(File::Which)
BuildRequires : perl(IPC::Run)
BuildRequires : perl(Log::Log4perl)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
Archive::Tar::Wrapper - API wrapper around the 'tar' utility
SYNOPSIS
use Archive::Tar::Wrapper;

%package dev
Summary: dev components for the perl-Archive-Tar-Wrapper package.
Group: Development
Provides: perl-Archive-Tar-Wrapper-devel = %{version}-%{release}
Requires: perl-Archive-Tar-Wrapper = %{version}-%{release}

%description dev
dev components for the perl-Archive-Tar-Wrapper package.


%package license
Summary: license components for the perl-Archive-Tar-Wrapper package.
Group: Default

%description license
license components for the perl-Archive-Tar-Wrapper package.


%package perl
Summary: perl components for the perl-Archive-Tar-Wrapper package.
Group: Default
Requires: perl-Archive-Tar-Wrapper = %{version}-%{release}

%description perl
perl components for the perl-Archive-Tar-Wrapper package.


%prep
%setup -q -n Archive-Tar-Wrapper-0.42
cd %{_builddir}/Archive-Tar-Wrapper-0.42
pushd ..
cp -a Archive-Tar-Wrapper-0.42 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Archive-Tar-Wrapper
cp %{_builddir}/Archive-Tar-Wrapper-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Archive-Tar-Wrapper/bea8d3c5dd72ed5e84cfc4b02cf19cf41d0e86cf || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Archive::Tar::Wrapper.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Archive-Tar-Wrapper/bea8d3c5dd72ed5e84cfc4b02cf19cf41d0e86cf

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
