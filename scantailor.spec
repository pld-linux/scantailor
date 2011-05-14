Summary:	Post-processing tool for scanned pages
Name:		scantailor
Version:	0.9.9.2
Release:	1
License:	GPL v3
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/scantailor/%{name}-%{version}.tar.gz
# Source0-md5:	0944b12c936019fe12269c7a356d60d0
URL:		http://scantailor.sourceforge.net/
BuildRequires:	QtGui-devel
BuildRequires:	QtXml-devel
BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	qt4-qmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An interactive post-processing tool for scanned pages. It performs
operations such as page splitting, deskewing, adding/removing borders,
and others. You give it raw scans, and you get pages ready to be
printed or assembled into a PDF or DJVU file. Scanning, optical
character recognition, and assembling multi-page documents are out of
scope of this project.

%prep
%setup -q

%build
export CFLAGS="%{rpmcflags}"
export CXXFLAGS="%{rpmcflags}"
%{__cmake} . \
	-DCMAKE_INSTALL_PREFIX="%{_prefix}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc resources/icons/COPYING
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%lang(bg) %{_datadir}/%{name}/translations/%{name}_bg.qm
%lang(de) %{_datadir}/%{name}/translations/%{name}_de.qm
%lang(fr) %{_datadir}/%{name}/translations/%{name}_fr.qm
%lang(ja) %{_datadir}/%{name}/translations/%{name}_ja.qm
%lang(ru) %{_datadir}/%{name}/translations/%{name}_ru.qm
