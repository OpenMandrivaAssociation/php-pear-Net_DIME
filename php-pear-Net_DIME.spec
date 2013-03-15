%define		_class		Net
%define		_subclass	DIME
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.0.2
Release:	5
Summary:	Implements DIME encoding
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Net_DIME/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
Provides an implementation of DIME as defined at
http://search.ietf.org/internet-drafts/draft-nielsen-dime-02.txt

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-2mdv2011.0
+ Revision: 667625
- mass rebuild

* Sun Nov 07 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.2-1mdv2011.0
+ Revision: 594497
- update to new version 1.0.2

* Sun Nov 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.1-4mdv2010.1
+ Revision: 468693
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.1-3mdv2010.0
+ Revision: 426658
- rebuild

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-2mdv2009.1
+ Revision: 321878
- rebuild

* Sun Oct 12 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.1-1mdv2009.1
+ Revision: 292882
- update to new version 1.0.1

* Tue Sep 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.0-1mdv2009.0
+ Revision: 278930
- update to new version 1.0.0

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.3-10mdv2009.0
+ Revision: 224755
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3-9mdv2008.1
+ Revision: 178525
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.3-8mdv2007.0
+ Revision: 82229
- Import php-pear-Net_DIME

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.3-8mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3-7mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3-6mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3-5mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3-4mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3-3mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3-2mdk
- fix spec file to conform with the others

* Thu Jan 20 2005 Pascal Terjan <pterjan@mandrake.org> 0.3-1mdk
- First mdk package

