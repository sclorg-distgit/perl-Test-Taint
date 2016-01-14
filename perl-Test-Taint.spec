%{?scl:%scl_package perl-Test-Taint}
%{!?scl:%global pkg_name %{name}}

Summary:        Tools to test taintedness
Name:           %{?scl_prefix}perl-Test-Taint
Version:        1.06
Release:        8%{?dist}
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Test-Taint/
Source0:        http://search.cpan.org/CPAN/authors/id/P/PE/PETDANCE/Test-Taint-%{version}.tar.gz

BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl(base)
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(DynaLoader)
BuildRequires:  %{?scl_prefix}perl(overload)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(Scalar::Util)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(Test::Builder)
BuildRequires:  %{?scl_prefix}perl(Test::More)
BuildRequires:  %{?scl_prefix}perl(Test::Pod) >= 1.14
BuildRequires:  %{?scl_prefix}perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  %{?scl_prefix}perl(Tie::Array)
BuildRequires:  %{?scl_prefix}perl(Tie::Hash)
BuildRequires:  %{?scl_prefix}perl(Tie::Scalar)
BuildRequires:  %{?scl_prefix}perl(Tie::StdArray)
BuildRequires:  %{?scl_prefix}perl(Tie::StdHash)
BuildRequires:  %{?scl_prefix}perl(Tie::StdScalar)
BuildRequires:  %{?scl_prefix}perl(vars)
BuildRequires:  %{?scl_prefix}perl(warnings)

%{?scl:%global perl_version %(scl enable %{scl} 'eval "`%{__perl} -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`%{__perl} -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})

%{?perl_default_filter}

%description
Tainted data is data that comes from an unsafe source, such as the command
line, or, in the case of web apps, any GET or POST transactions. Read the 
perlsec man page for details on why tainted data is bad, and how to untaint
the data.

When you're writing unit tests for code that deals with tainted data, you'll
want to have a way to provide tainted data for your routines to handle, and 
easy ways to check and report on the taintedness of your data, in standard 
Test::More style.

%prep
%setup -q -n Test-Taint-%{version}

%build
%{?scl:scl enable %{scl} '}
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="${RPM_OPT_FLAGS}"
%{?scl:'}
%{?scl:scl enable %{scl} "}
make %{?_smp_mflags}
%{?scl:"}

%install
%{?scl:scl enable %{scl} "}
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
%{?scl:"}
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%files
%doc Changes
%{perl_vendorarch}/Test
%{perl_vendorarch}/auto/Test
%{_mandir}/man3/*

%changelog
* Tue Feb 18 2014 Petr Pisar <ppisar@redhat.com> - 1.06-8
- Build-requires warnings module (bug #1066320)

* Tue Feb 18 2014 Petr Pisar <ppisar@redhat.com> - 1.06-7
- Correct dependencies (bug #1066320)

* Wed Dec 11 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.06-6
- Rebuilt with newer perl516-build
- Resolves: rhbz#1040549

* Thu Nov 21 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1.06-5
- Rebuilt for SCL

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.06-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 20 2013 Petr Pisar <ppisar@redhat.com> - 1.06-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 08 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.06-1
- Upstream update.
- Add missing deps.

* Thu Oct 25 2012 Jitka Plesnikova <jplesnik@redhat.com> - 1.04-19
- Specify all dependencies
- Drop %%defattr, redundant since rpm 4.4
- Fix mixed use of spaces and tabs

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 1.04-17
- Perl 5.16 rebuild

* Sun Jan 22 2012 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.04-16
- Modernize spec.
- Add %%{perl_default_filter}.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.04-14
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.04-12
- 661697 rebuild for fixing problems with vendorach/lib

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.04-11
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 1.04-10
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.04-7
- Rebuild for perl 5.10 (again)

* Sun Feb 10 2008 Ralf Corsépius <rc040203@freenet.de> - 1.04-6
- Rebuild for gcc43.

* Mon Jan 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.04-5
- rebuild for new perl

* Fri Aug 17 2007 Ralf Corsépius <rc040203@freenet.de> - 1.04-4
- Reflect perl-package split.
- Update license tag.

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 1.04-3
- Mass rebuild.

* Mon Feb 20 2006 Ralf Corsepius <rc040203@freenet.de> - 1.04-2
- Rebuild.

* Wed Aug 10 2005 Ralf Corsepius <ralf@links2linux.de> - 1.04-1
- FE submission.

* Sun Mar 20 2005 Ralf Corsepius <ralf@links2linux.de> - 1.04-0.pm.2
- Initial version.
