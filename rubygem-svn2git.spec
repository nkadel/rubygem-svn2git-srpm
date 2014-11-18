# Generated from svn2git-2.3.2.gem by gem2rpm -*- rpm-spec -*-
%global gemname svn2git

%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}
%global rubyabi 1.8

Summary: A tool for migrating svn projects to git
Name: rubygem-%{gemname}
Version: 2.3.2
Release: 0.1%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/nirvdrum/svn2git
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
Requires: ruby(abi) = %{rubyabi}
Requires: ruby(rubygems) 
BuildRequires: ruby(abi) = %{rubyabi}
BuildRequires: ruby(rubygems) 
BuildRequires: ruby 
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}
# Needed for RHEL 5
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description



%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}


%prep
%setup -q -c -T
mkdir -p .%{gemdir}
gem install --local --install-dir .%{gemdir} \
            --bindir .%{_bindir} \
            --force %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gemdir}
cp -pa .%{gemdir}/* \
        %{buildroot}%{gemdir}/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{geminstdir}/bin -type f | xargs chmod a+x

%files
%dir %{geminstdir}
%{_bindir}/svn2git
%{geminstdir}/bin
%{geminstdir}/lib
%exclude %{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec
%exclude %{gemdir}/gems/%{gemname}-%{version}/MIT-LICENSE
%exclude %{gemdir}/gems/%{gemname}-%{version}/Rakefile
%exclude %{gemdir}/gems/%{gemname}-%{version}/VERSION.yml
%exclude %{gemdir}/gems/%{gemname}-%{version}/svn2git.gemspec
%{gemdir}/gems/%{gemname}-%{version}/test

%files doc
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/ChangeLog.markdown
%doc %{geminstdir}/README.markdown
%doc %{geminstdir}/MIT-LICENSE


%changelog
* Mon Nov 17 2014 Nico Kadel-Garcia <nkadel@gmail.com> - 2.3.2-1
- Initial package
- Reset license files and docs as needed
- Exclude Rakefile and VERSION.yml files as needed
