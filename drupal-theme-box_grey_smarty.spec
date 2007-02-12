%define		themename box_grey_smarty
%define		_ver 4.6
Summary:	Drupal Theme Box_grey_smarty
Summary(pl.UTF-8):	Motyw Box_grey_smarty dla Drupala
Name:		drupal-theme-%{themename}
Version:	%{_ver}.0
Release:	0.9
License:	GPL v2
Group:		Applications/WWW
Source0:	http://drupal.org/files/projects/%{themename}-%{version}.tar.gz
# Source0-md5:	5b6cf02791e36c7a9b97686c270dbd46
URL:		http://drupal.org/node/13811
Requires:	drupal >= %{_ver}
Requires:	drupal-themeengine-smarty >= %{_ver}
Provides:	drupal(theme) = %{_ver}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_drupaldir		%{_datadir}/drupal
%define		_htdocs			%{_drupaldir}/htdocs
%define		_themedir		%{_drupaldir}/themes
%define		_themehtmldir	%{_htdocs}/themes
%define		_cachedir		/var/cache/drupal/smarty

%description
A port of the original box_grey theme for the Smarty template engine.

%description -l pl.UTF-8
Port oryginalnego motywu box_grey dla silnika szablonów Smarty.

%prep
%setup -q -n %{themename}
rm -f LICENSE.txt # GPL v2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_themehtmldir},%{_themedir},%{_cachedir}}/%{themename}

# box_grey_smarty
install *.{css,png}  $RPM_BUILD_ROOT%{_themehtmldir}/%{themename}
install *.tpl $RPM_BUILD_ROOT%{_themedir}/%{themename}
ln -s ../../htdocs/themes/%{themename}/screenshot.png $RPM_BUILD_ROOT%{_themedir}/%{themename}

# theme style box_cleanslate_smarty
install -d $RPM_BUILD_ROOT{%{_themehtmldir}/%{themename}/box_cleanslate_smarty,%{_themedir}}/%{themename}}
install box_cleanslate_smarty/*.{css,png} $RPM_BUILD_ROOT%{_themehtmldir}/%{themename}/box_cleanslate_smarty
ln -s ../../htdocs/themes/%{themename}/box_cleanslate_smarty $RPM_BUILD_ROOT%{_themedir}/%{themename}/box_cleanslate_smarty

%clean
rm -rf $RPM_BUILD_ROOT

%post
# nuke smarty cache. causes side effects on upgrade
rm -f %{_cachedir}/%{themename}/*.php

%preun
if [ "$1" = "0" ]; then
	# kill cache to allow rpm remove the empty directory
	rm -f %{_cachedir}/%{themename}/*.php
fi

%files
%defattr(644,root,root,755)
%doc *.txt
%{_themedir}/%{themename}
%{_themehtmldir}/%{themename}
%dir %attr(770,root,http) %{_cachedir}/%{themename}
