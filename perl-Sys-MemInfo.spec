%define module Sys-MemInfo
%undefine _debugsource_packages

Name:		perl-%{module}
Version:	0.99
Release:	1
Summary:	Perl module for querying free and used physical memory
URL:		https://metacpan.org/pod/Sys::MemInfo
Source:		https://cpan.org/modules/by-module/Sys/%{module}-%{version}.tar.gz
License:	Perl (Artistic or GPL)
Group:		Development/Perl
BuildRequires:	perl
BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)

%description
Perl module for querying free and used physical memory

%prep
%autosetup -p1 -n %{module}-%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%check
make test

%install
%make_install INSTALLDIRS=vendor

%files
%doc Changes MANIFEST README
%{perl_vendorarch}/*/*
%{_mandir}/man3/*.3pm*
