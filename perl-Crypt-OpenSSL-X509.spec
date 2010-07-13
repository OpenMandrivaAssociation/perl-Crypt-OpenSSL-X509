%define upstream_name	 Crypt-OpenSSL-X509
%define upstream_version 1.2

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Perl extension to OpenSSL's X509 API
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/D/DA/DANIEL/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	libopenssl-devel
BuildRequires:	perl(Module::Install)
BuildRequires:	perl(YAML)
BuildRequires:	perl-devel

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This is a Perl extension to OpenSSL's X509 API. It implements a large majority
of OpenSSL's useful X509 API.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README TODO certs
%{perl_vendorarch}/Crypt
%{perl_vendorarch}/auto/Crypt
%{_mandir}/*/*
