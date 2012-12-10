Name:           mairix
Version:        0.23
Release:        1
Summary:        A program for indexing and searching email messages

Group:          Networking/Mail
License:        GPLv2
URL:            http://www.rc0.org.uk/mairix
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:         mairix-0.23-build.patch

BuildRequires:  bison flex bzip2-devel zlib-devel

%description
mairix is a program for indexing and searching email messages
stored in Maildir, MH or mbox folders.

%prep
%setup -q
%patch0 -p1 -b .build

find -type f ! -name configure -a ! -name mkversion | xargs chmod 644
for i in ACKNOWLEDGEMENTS NEWS; do
  iconv -f iso8859-1 -t utf8 -o ${i}{_,} && touch -r ${i}{,_} && mv -f ${i}{_,}
done

%build
# fool the configure macro :-(
touch configure.ac 
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ACKNOWLEDGEMENTS COPYING NEWS README dotmairixrc.eg
%{_bindir}/mairix
%{_mandir}/man1/mairix.1*
%{_mandir}/man5/mairixrc.5*



%changelog
* Wed Feb 01 2012 Bogdano Arendartchuk <bogdano@mandriva.com> 0.23-1
+ Revision: 770516
- replaced the botched build patch with another that builds on 0.23
- new version 0.23

* Wed Mar 16 2011 Stéphane Téletchéa <steletch@mandriva.org> 0.22-1
+ Revision: 645305
- update to new version 0.22

* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.21-2mdv2011.0
+ Revision: 620290
- the mass rebuild of 2010.0 packages

* Mon Jul 27 2009 Bogdano Arendartchuk <bogdano@mandriva.com> 0.21-1mdv2010.0
+ Revision: 400655
- imported package mairix


* Mon Jul 27 2009 Bogdano Arendartchuk <bogdano@mandriva.com>
- Ported package to Mandriva Linux

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Aug 29 2008 Miroslav Lichvar <mlichvar@redhat.com> 0.21-2
- fix building with new rpm

* Wed Mar 05 2008 Miroslav Lichvar <mlichvar@redhat.com> 0.21-1
- initial release
