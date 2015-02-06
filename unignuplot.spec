%define name unignuplot
%define version 2.0
%define release 9
%define subversion D

Summary:	Simplify the command line interface with GNUPlot
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		System/Libraries
License:	GPL
Source:		%{name}-%{version}.0%{subversion}.tar.bz2

URL:		http://www.fltk.org
BuildRoot:	%_tmppath/%name-%version-%release-root
Requires:	tk, gnuplot
BuildArch:	noarch

%description
UniGNUPlot is a Simple TK/Tcl based program what it's primary goal 
is simplify the command line interface with GNUPlot.
UniGNUPlot is a GNUplot Graphical Front-End as simple as you can 
only type the expresion, some parameter and that's all. 

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q -n %{name}%{subversion}
find -name "*~" | xargs rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p  $RPM_BUILD_ROOT%{_bindir}
mkdir -p  $RPM_BUILD_ROOT%{_datadir}/%{name}/lang

install -m 755 %{name}-%{version}.0%{subversion}.tcl $RPM_BUILD_ROOT%{_bindir}
install -m 755 lang/* $RPM_BUILD_ROOT%{_datadir}/%{name}/lang

#Fixing lang path
perl -pi -e "s|lang/lang_|/usr/share/unignuplot/lang/lang_|g" $RPM_BUILD_ROOT%{_bindir}/%{name}-%{version}.0%{subversion}.tcl

%files
%defattr(-,root,root)
%doc README COPYING CHANGES Doc
%{_bindir}/%{name}-%{version}.0%{subversion}.tcl
%{_datadir}/%{name}/lang/*



%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 2.0-8mdv2010.0
+ Revision: 434544
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.0-7mdv2009.0
+ Revision: 261773
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.0-6mdv2009.0
+ Revision: 255148
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 2.0-4mdv2008.1
+ Revision: 128755
- kill re-definition of %%buildroot on Pixel's request
- import unignuplot


* Mon Dec 19 2005 Erwan Velu <erwan@seanodes.com> 2.0-4mdk
- D release

* Fri Feb 14 2004 Erwan Velu <erwan@mandrakesoft.com> 2.0-3mdk
- Rebuild
* Sat Jan 11 2003 Lenny Cartier <lenny@mandrakesoft.com> 2.0-2mdk
- wrap too long lines in description & summary

* Wed Dec 17 2002 Erwan Velu <erwan@mandrakesoft.com> 2.0-1mdk
- First MDK release
