# Generated by rust2rpm 10
%bcond_without check
%global debug_package %{nil}

%global crate version-sync

Name:           rust-%{crate}
Version:        0.8.1
Release:        6%{?dist}
Summary:        Simple crate for ensuring that version numbers in README files are updated when the crate version changes

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/version-sync
Source:         %{crates_source}
# Initial patched metadata
# - Bump pulldown-cmark to 0.6, https://github.com/mgeisler/version-sync/pull/79
Patch0:         version-sync-fix-metadata.diff
# * Fix tests with toml 0.5.3+, https://github.com/mgeisler/version-sync/commit/33dc77fda8c5d993abee4e6c31c7526408877003
Patch0001:      0001-markdown_deps-handle-test-output-from-toml-0.5.3.patch

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Simple crate for ensuring that version numbers in README files are updated when
the crate version changes.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc README.md
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 06 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.1-5
- Fix tests with new toml

* Fri Sep 13 19:03:49 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.8.1-4
- Bump pulldown-cmark to 0.6

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 15:38:53 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.1-2
- Update pulldown-cmark to 0.5

* Thu Apr 04 08:15:21 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.1-1
- Update to 0.8.1

* Sun Feb 10 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.0-1
- Update to 0.7.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 10 2018 Josh Stone <jistone@redhat.com> - 0.5.0-8
- Adapt to new packaging

* Tue Sep 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.0-7
- Bump syn to 0.14

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 17 2018 Josh Stone <jistone@redhat.com> - 0.5.0-5
- Bump syn to 0.13

* Thu Mar 08 2018 Josh Stone <jistone@redhat.com> - 0.5.0-4
- Bump syn to 0.12

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.0-2
- Rebuild for rust-packaging v5

* Mon Nov 20 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.0-1
- Update to 0.5.0

* Mon Nov 13 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.0-1
- Initial package
