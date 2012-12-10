%define name	ledit
%define version	2.02.1
%define release	%mkrel 1

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	BSD like
Summary:	Line editor
Group:		Editors
Source:		http://pauillac.inria.fr/~ddr/ledit/distrib/src/%{name}-%{version}.tgz
BuildRequires:	ocaml
BuildRequires:	camlp5
BuildRequires:	ncurses-devel
BuildRoot: 	%{_tmppath}/%{name}-%{version}

%description 
Ledit is a line editor, allowing to use control commands like in emacs
or in shells (bash, tcsh). To be used with interactive commands. It is
written in Ocaml and Camlp4 and uses the library unix.cma.

%prep
%setup -q
perl -pi -e 's|\+camlp5|+site-lib/camlp5|' Makefile

%build
make

%install
rm -rf %{buildroot}
make \
	BINDIR=%{buildroot}%{_bindir} \
	MANDIR=%{buildroot}%{_mandir}/man1 \
	install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES LICENSE README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Wed Mar 16 2011 Stéphane Téletchéa <steletch@mandriva.org> 2.02.1-1mdv2011.0
+ Revision: 645250
- update to new version 2.02.1

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.02-1mdv2011.0
+ Revision: 601953
- update to new version 2.02

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 2.01-2mdv2010.0
+ Revision: 429710
- rebuild

* Mon Aug 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.01-1mdv2009.0
+ Revision: 270909
- update to new version 2.01

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 2.00-3mdv2009.0
+ Revision: 248342
- rebuild

* Tue Jan 29 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.00-1mdv2008.1
+ Revision: 159978
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

  + Funda Wang <fwang@mandriva.org>
    - Import ledit



* Mon Aug 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.11-3mdv2007.0
- Rebuild

* Mon May 22 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.11-2mdk
- fix build
- %%mkrel

* Tue Dec 14 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.11-1mdk 
- first mdk release
