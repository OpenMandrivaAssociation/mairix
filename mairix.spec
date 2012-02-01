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

