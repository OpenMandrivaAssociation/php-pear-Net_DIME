%define	_class		Net
%define	_subclass	DIME
%define	modname	%{_class}_%{_subclass}

Summary:	Implements DIME encoding
Name:		php-pear-%{modname}
Version:	1.0.2
Release:	12
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/Net_DIME/
Source0:	http://download.pear.php.net/package/%{modname}-%{version}.tgz
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun):	php-pear
Requires:	php-pear

%description
Provides an implementation of DIME as defined at
http://search.ietf.org/internet-drafts/draft-nielsen-dime-02.txt

%prep
%setup -qc
mv package.xml %{modname}-%{version}/%{modname}.xml

%install
cd %{modname}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages

%files
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{modname}.xml

