#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Catalyst
%define		pnam	Component-InstancePerContext
%include	/usr/lib/rpm/macros.perl
Summary:	Catalyst::Component::InstancePerContext - Return a new instance a component on each request
Name:		perl-Catalyst-Component-InstancePerContext
Version:	0.001001
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	dd3e9c804cb7f8d6755132d92b26a80a
URL:		http://search.cpan.org/dist/Catalyst-Component-InstancePerContext/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Catalyst
BuildRequires:	perl-Moose
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Return a new instance a component on each request

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Catalyst/Component/*.pm
%{_mandir}/man3/*
