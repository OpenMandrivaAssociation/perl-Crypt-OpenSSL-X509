%define upstream_name	 Crypt-OpenSSL-X509
%define upstream_version 1.800.2

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	2

Summary:	Perl extension to OpenSSL's X509 API
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/D/DA/DANIEL/%{upstream_name}-%{upstream_version}.tar.gz
Patch0:     Crypt-OpenSSL-X509-1.800.1-dont-turn-warning-into-errors.patch
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
%patch0 -p 1

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


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.800.2-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sun May 08 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.800.2-1
+ Revision: 672609
- update to new version 1.800.2

* Mon May 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.800.1-1
+ Revision: 662876
- new version

* Fri Jan 07 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.600.0-1mdv2011.0
+ Revision: 629481
- update to new version 1.6

* Sun Dec 26 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.500.0-1mdv2011.0
+ Revision: 625268
- update to new version 1.5

* Thu Sep 02 2010 Jérôme Quelin <jquelin@mandriva.org> 1.400.0-1mdv2011.0
+ Revision: 575392
- update to 1.4

* Sun Aug 08 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.300.0-1mdv2011.0
+ Revision: 567736
- update to new version 1.3

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.200.0-2mdv2011.0
+ Revision: 555720
- rebuild

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.200.0-1mdv2011.0
+ Revision: 551985
- update to 1.2

* Tue Jan 19 2010 Jérôme Quelin <jquelin@mandriva.org> 1.0.0-1mdv2010.1
+ Revision: 493491
- update to 1.0

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.7-3mdv2010.0
+ Revision: 430370
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.7-2mdv2009.0
+ Revision: 268404
- rebuild early 2009.0 package (before pixel changes)

* Tue May 20 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.7-1mdv2009.0
+ Revision: 209322
- update to new version 0.7

* Mon Feb 25 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.6-1mdv2008.1
+ Revision: 174703
- update to new version 0.6

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.5-2mdv2008.1
+ Revision: 152039
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Jul 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.5-1mdv2008.0
+ Revision: 53357
- fix buildrequires
- update to new version 0.5


* Tue Mar 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.4-1mdv2007.0
+ Revision: 133724
- new version
- Import perl-Crypt-OpenSSL-X509

* Fri Sep 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.1-3mdv2007.0
- Rebuild

* Fri Mar 17 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.1-2mdk
- rebuild for new openssl
- spec cleanup

* Wed Aug 17 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.1-1mdk
- new version
- fix source url for rpmbuildupdate

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3-1mdk
- initial Mandriva package

