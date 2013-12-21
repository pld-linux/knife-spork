Summary:	Chef knife workflow plugin
Name:		knife-spork
Version:	1.3.0
Release:	0.2
License:	GPL v2+ or Ruby
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{name}-%{version}.gem
# Source0-md5:	fa96bacb8c226a3e5d829cfb2d6ae909
URL:		https://github.com/jonlives/knife-spork
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
Requires:	knife >= 11.0.0
Requires:	ruby-app_conf >= 0.4.0
Requires:	ruby-diffy >= 3.0.1
Requires:	ruby-git >= 1.2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A workflow plugin to help many devs work with the same Chef
repo/server.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_vendorlibdir}/%{name}.rb
%{ruby_vendorlibdir}/%{name}
%{ruby_vendorlibdir}/chef/knife/spork-*.rb
