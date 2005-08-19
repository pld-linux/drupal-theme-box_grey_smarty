%define		themename box_grey_smarty
Summary:	Drupal Theme Box_grey_smarty
Name:		drupal-theme-%{themename}
Version:	4.6.0
Release:	0.5
Epoch:		0
License:	GPL v2
Group:		Applications/WWW
Source0:	http://drupal.org/files/projects/%{themename}-%{version}.tar.gz
# Source0-md5:	5b6cf02791e36c7a9b97686c270dbd46
URL:		http://drupal.org/node/13811
Requires:	drupal >= 4.6.0
Requires:	drupal-themeengine-smarty >= 4.6.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_themedir		%{_datadir}/drupal/themes
%define		_themehtmldir	%{_datadir}/drupal/htdocs/themes

%description
A port of the original box_grey theme for the Smarty template engine.

%prep
%setup -q -n %{themename}
rm -f LICENSE.txt # GPL v2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_themehtmldir},%{_themedir}}/%{themename}

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

%files
%defattr(644,root,root,755)
%doc *.txt
%{_themedir}/%{themename}
%{_themehtmldir}/%{themename}
