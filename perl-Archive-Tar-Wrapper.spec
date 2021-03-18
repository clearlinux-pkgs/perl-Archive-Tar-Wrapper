#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Archive-Tar-Wrapper
Version  : 0.38
Release  : 21
URL      : https://cpan.metacpan.org/authors/id/A/AR/ARFREITAS/Archive-Tar-Wrapper-0.38.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/A/AR/ARFREITAS/Archive-Tar-Wrapper-0.38.tar.gz
Summary  : "API wrapper around the 'tar' utility"
Group    : Development/Tools
License  : GPL-3.0
Requires: perl-Archive-Tar-Wrapper-license = %{version}-%{release}
Requires: perl-Archive-Tar-Wrapper-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(File::Which)
BuildRequires : perl(IPC::Run)
BuildRequires : perl(Log::Log4perl)

%description
# NAME
Archive::Tar::Wrapper - API wrapper around the 'tar' utility
# SYNOPSIS
```perl
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
%setup -q -n Archive-Tar-Wrapper-0.38
cd %{_builddir}/Archive-Tar-Wrapper-0.38

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
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
cp %{_builddir}/Archive-Tar-Wrapper-0.38/LICENSE %{buildroot}/usr/share/package-licenses/perl-Archive-Tar-Wrapper/8624bcdae55baeef00cd11d5dfcfa60f68710a02
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Archive::Tar::Wrapper.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Archive-Tar-Wrapper/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.32.1/Archive/Tar/Wrapper.pm
