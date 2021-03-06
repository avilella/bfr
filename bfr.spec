Summary: nonblocking 8-bit-clean pipe buffer
Name: bfr
Version: 1.6
Release: 1
Copyright: GPL
Group: Utilities/File
Source: http://glines.org:8000/bin/pk/bfr-1.6.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Packager: Andreas Metzler <ametzler@logic.univie.ac.at>

%description
bfr's purpose is to buffer data.  It buffers from its standard input
and/or a list of files of your choosing, and allows this data to flow
to its standard output at whatever rate that end can handle.  Its 
useful for any situation in which its beneficial to have I/O occur in
a detached yet smooth fashion.

%changelog

* Thu Jun 19 2003 Mark Glines <mark@glines.org>
  updated Source: URL
* Sat Jan 13 2001 Mark Glines <paranoid@deathsdoor.com>
  changed the sourcefile to .tar.gz, so "rpm -ta" should work with it
  released 0.99.9
* Fri Dec 22 2000 Mark Glines <paranoid@deathsdoor.com>
  minor changes to specfile for auto-creating from autoconf
* Fri Dec 22 2000 Andreas Metzler <ametzler@logic.univie.ac.at>
  Built rpm.

%prep
%setup

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr --mandir=%{_mandir}
make

%clean
rm -rf %{buildroot}

%install
make DESTDIR=${RPM_BUILD_ROOT} install-strip
gzip -9 %{buildroot}%{_mandir}/man1/bfr.1

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
/usr/bin/*
%{_mandir}/man1/*


