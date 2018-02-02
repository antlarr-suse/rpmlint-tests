Name:		desktopfile-bad-unicode
Version:	0
Release:	0
Group:          Development/Tools/Building
Summary:	Lorem ipsum
License:	GPL-2.0+
BuildRoot:	%_tmppath/%name-%version-build
Url:            http://www.opensuse.org/
BuildArch:      noarch

%description
Lorem ipsum dolor sit amet, consectetur adipisici elit, sed
eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim
ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
aliquid ex ea commodi consequat. Quis aute iure reprehenderit in
voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint obcaecat cupiditat non proident, sunt in culpa qui
officia deserunt mollit anim id est laborum.

%prep
%build

%install
install -d -m 755 %buildroot/%_datadir/applications

echo -e "#! /bin/bash\ntrue" > rpmlint-test
install -d -m 755 %buildroot/%_bindir/
install -m 755 rpmlint-test %buildroot/%_bindir/

cat > %buildroot/%_datadir/applications/rpmlint-test.desktop <<'EOF'
[Desktop Entry]
Name=rpmlint-test
Name[de]=rpmlint-test umlaut ��� 
Exec=rpmlint-test %F
Icon=rpmlint-test
Type=Application
GenericName=rpmlint testcase
EOF


%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%{_bindir}/rpmlint-test
%{_datadir}/applications/

%changelog
* Mon Jan 22 2018 stefan.bruens@rwth-aachen.de
- dummy

