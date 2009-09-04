%define name	ledit
%define version	2.01
%define release	%mkrel 2

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
