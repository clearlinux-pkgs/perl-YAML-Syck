#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-YAML-Syck
Version  : 1.34
Release  : 16
URL      : https://cpan.metacpan.org/authors/id/T/TO/TODDR/YAML-Syck-1.34.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/T/TO/TODDR/YAML-Syck-1.34.tar.gz
Source1  : http://http.debian.net/debian/pool/main/liby/libyaml-syck-perl/libyaml-syck-perl_1.30-1.debian.tar.xz
Summary  : 'Fast, lightweight YAML loader and dumper'
Group    : Development/Tools
License  : GPL-2.0 MIT
Requires: perl-YAML-Syck-license = %{version}-%{release}
Requires: perl-YAML-Syck-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
[![](https://github.com/toddr/YAML-Syck/workflows/linux/badge.svg)](https://github.com/toddr/YAML-Syck/actions) [![](https://github.com/toddr/YAML-Syck/workflows/macos/badge.svg)](https://github.com/toddr/YAML-Syck/actions) [![](https://github.com/toddr/YAML-Syck/workflows/windows/badge.svg)](https://github.com/toddr/YAML-Syck/actions)

%package dev
Summary: dev components for the perl-YAML-Syck package.
Group: Development
Provides: perl-YAML-Syck-devel = %{version}-%{release}
Requires: perl-YAML-Syck = %{version}-%{release}

%description dev
dev components for the perl-YAML-Syck package.


%package license
Summary: license components for the perl-YAML-Syck package.
Group: Default

%description license
license components for the perl-YAML-Syck package.


%package perl
Summary: perl components for the perl-YAML-Syck package.
Group: Default
Requires: perl-YAML-Syck = %{version}-%{release}

%description perl
perl components for the perl-YAML-Syck package.


%prep
%setup -q -n YAML-Syck-1.34
cd %{_builddir}
tar xf %{_sourcedir}/libyaml-syck-perl_1.30-1.debian.tar.xz
cd %{_builddir}/YAML-Syck-1.34
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/YAML-Syck-1.34/deblicense/

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
mkdir -p %{buildroot}/usr/share/package-licenses/perl-YAML-Syck
cp %{_builddir}/YAML-Syck-1.34/COPYING %{buildroot}/usr/share/package-licenses/perl-YAML-Syck/3710975c0e6727079e17c6d1f27948c40729d710
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-YAML-Syck/369b581499a69287a2fc4cc6ebac64ac5a8eaafa
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
/usr/share/man/man3/JSON::Syck.3
/usr/share/man/man3/YAML::Syck.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-YAML-Syck/369b581499a69287a2fc4cc6ebac64ac5a8eaafa
/usr/share/package-licenses/perl-YAML-Syck/3710975c0e6727079e17c6d1f27948c40729d710

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.3/x86_64-linux-thread-multi/JSON/Syck.pm
/usr/lib/perl5/vendor_perl/5.30.3/x86_64-linux-thread-multi/YAML/Dumper/Syck.pm
/usr/lib/perl5/vendor_perl/5.30.3/x86_64-linux-thread-multi/YAML/Loader/Syck.pm
/usr/lib/perl5/vendor_perl/5.30.3/x86_64-linux-thread-multi/YAML/Syck.pm
/usr/lib/perl5/vendor_perl/5.30.3/x86_64-linux-thread-multi/auto/YAML/Syck/Syck.so
