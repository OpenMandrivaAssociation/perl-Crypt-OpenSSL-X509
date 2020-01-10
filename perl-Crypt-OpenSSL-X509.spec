%define _disable_lto 1

%define upstream_name	 Crypt-OpenSSL-X509
%define upstream_version 1.806

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	4

Summary:	Perl extension to OpenSSL's X509 API
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/D/DA/DANIEL/Crypt-OpenSSL-X509-%{upstream_version}.tar.gz
Patch2:		Crypt-OpenSSL-X509-1.806-Fix-condition-negation.patch
BuildRequires:	openssl-devel
BuildRequires:	perl(Module::Install)
BuildRequires:	perl(YAML)
BuildRequires:	perl-devel


%description
This is a Perl extension to OpenSSL's X509 API. It implements a large majority
of OpenSSL's useful X509 API.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%autopatch -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CC=gcc CFLAGS="%optflags"

%check
%make test

%install
%makeinstall_std

%clean 

%files
%doc Changes README TODO certs
%{perl_vendorarch}/Crypt
%{perl_vendorarch}/auto/Crypt
%{_mandir}/*/*

