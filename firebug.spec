# TODO
# - make it generic for gecko based browsers (browser-plugins should first support this) and rename accordingly
%define		subver	b7
%define		rel		0.1
Summary:	Firebug extension for Firefox
Name:		firebug
Version:	1.2.0
Release:	0.%{subver}.%{rel}
License:	BSD License
Group:		Development/Languages/PHP
URL:		https://addons.mozilla.org/en-US/firefox/addon/1843
Source0:	https://addons.mozilla.org/downloads/file/34272/%{name}-%{version}%{subver}-fx.xpi
# Source0-md5:	8b8f8eec95418939bd8f72ce1bf3ca46
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# extension id from install.rdf
%define		extensionid		firebug@software.joehewitt.com
%define		extensiondir	%{_datadir}/mozilla-firefox/extensions/%{extensionid}

%description
Firebug integrates with Firefox to put a wealth of development tools
at your fingertips while you browse. You can edit, debug, and monitor
CSS, HTML, and JavaScript live in any web page...

%prep
%setup -qc
rm -f locale/Makefile.in
rm -f locale/jar.mn
rm -f platform/Darwin/chrome.manifest

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{extensiondir}
cp -a chrome.manifest install.rdf $RPM_BUILD_ROOT%{extensiondir}
cp -a build components content defaults icons lite locale skin $RPM_BUILD_ROOT%{extensiondir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*
%dir %{extensiondir}
%{extensiondir}/chrome.manifest
%{extensiondir}/install.rdf
%{extensiondir}/build
%{extensiondir}/components
%{extensiondir}/content
%{extensiondir}/defaults
%{extensiondir}/icons
%{extensiondir}/lite
%{extensiondir}/skin

%dir %{extensiondir}/locale
%{extensiondir}/locale/en-US
%lang(bg) %{extensiondir}/locale/bg
%lang(ca) %{extensiondir}/locale/ca-AD
%lang(cs) %{extensiondir}/locale/cs-CZ
%lang(da) %{extensiondir}/locale/da-DK
%lang(de) %{extensiondir}/locale/de-DE
%lang(es) %{extensiondir}/locale/es-ES
%lang(fr) %{extensiondir}/locale/fr-FR
%lang(hu) %{extensiondir}/locale/hu-HU
%lang(it) %{extensiondir}/locale/it-IT
%lang(ja) %{extensiondir}/locale/ja
%lang(ko) %{extensiondir}/locale/ko-KR
%lang(nl) %{extensiondir}/locale/nl-NL
%lang(pl) %{extensiondir}/locale/pl-PL
%lang(pt) %{extensiondir}/locale/pt-BR
%lang(sk) %{extensiondir}/locale/sk-SK
%lang(tr) %{extensiondir}/locale/tr-TR
%lang(zh_CN) %{extensiondir}/locale/zh-CN
%lang(zh_TW) %{extensiondir}/locale/zh-TW
