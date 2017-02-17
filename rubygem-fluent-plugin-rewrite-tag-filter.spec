# Generated from fluent-plugin-rewrite-tag-filter-1.5.5.gem by gem2rpm -*- rpm-spec -*-
%global gem_name fluent-plugin-rewrite-tag-filter

Name: rubygem-%{gem_name}
Version: 1.5.5
Release: 5%{?dist}
Summary: Fluentd Output filter plugins designed to rewrite tag like mod_rewrite.
Group: Development/Languages
License: ASL 2.0
URL: https://github.com/y-ken/fluent-plugin-rewrite-tag-filter
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
# BuildRequires: rubygem(test-unit) >= 3.1.0
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}
Requires: fluentd

%description
Fluentd Output filter plugin. It has designed to rewrite tag like mod_rewrite.
Re-emmit a record with rewrited tag when a value matches/unmatches with the
regular expression. Also you can change a tag from apache log by domain,
status-code(ex. 500 error), user-agent, request-uri, regex-backreference and
so on with regular expression.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/




# Run the test suite
%check
pushd .%{gem_instdir}

popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/example.conf
%{gem_instdir}/example2.conf
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/fluent-plugin-rewrite-tag-filter.gemspec
%{gem_instdir}/test

%changelog
* Fri Feb 17 2017 Sandro Bonazzola <sbonazzo@redhat.com> - 1.5.5-5
- Shortened Summary

* Wed Jan  4 2017 Rich Megginson <rmeggins@redhat.com> - 1.5.5-4
- change license to ASL 2.0; require fluentd

* Thu Jul 21 2016 Rich Megginson <rmeggins@redhat.com> - 1.5.5-3
- bump rev to rebuild for rhlog

* Thu Jul 21 2016 Rich Megginson <rmeggins@redhat.com> - 1.5.5-2
- Add Provides rubygem(name)

* Thu Jul 21 2016 Rich Megginson <rmeggins@redhat.com> - 1.5.5-1
- Initial package
