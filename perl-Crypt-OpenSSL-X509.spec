%define _disable_lto 1

%define upstream_name	 Crypt-OpenSSL-X509
Name:       perl-%{upstream_name}
Version:    2.1.3
Release:	2

Summary:	Perl extension to OpenSSL's X509 API
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/dsully/perl-crypt-openssl-x509
Source0:	https://cpan.metacpan.org/authors/id/J/JO/JONASBN/Crypt-OpenSSL-X509-%{version}.tar.gz
Patch2:		Crypt-OpenSSL-X509-1.806-Fix-condition-negation.patch
BuildRequires:	make
BuildRequires:	openssl-devel
BuildRequires:	perl(Module::Install)
BuildRequires:	perl(YAML)
BuildRequires:	perl-devel


%description
This is a Perl extension to OpenSSL's X509 API. It implements a large majority
of OpenSSL's useful X509 API.

%prep
%setup -q -n %{upstream_name}-%{version}
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

