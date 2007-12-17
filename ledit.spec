%define name	ledit
%define version	1.11
%define release	%mkrel 3

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	BSD like
Summary:	Line editor
Group:		Editors
Source:		http://caml.inria.fr/distrib/bazar-ocaml/%{name}.tar.bz2
Patch0:		%{name}-1.11.makefile.patch.bz2
Patch1:		%{name}-1.11.camlp4.patch.bz2
BuildRequires:	ocaml
BuildRequires:	camlp4
BuildRequires:	ncurses-devel

%description 
Ledit is a line editor, allowing to use control commands like in emacs
or in shells (bash, tcsh). To be used with interactive commands. It is
written in Ocaml and Camlp4 and uses the library unix.cma.

%prep
%setup -q
%patch0
%patch1
mv ledit.l.tpl ledit.1.tpl

%build
make

%install
rm -rf %{buildroot}
make \
	BINDIR=%{buildroot}%{_bindir} \
	MANDIR=%{buildroot}%{_mandir} \
	install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
