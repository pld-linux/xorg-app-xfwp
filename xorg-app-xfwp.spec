# $Rev: 3390 $, $Date: 2005-08-27 17:42:47 $
#
Summary:	xfwp application
Summary(pl):	Aplikacja xfwp
Name:		xorg-app-xfwp
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/app/xfwp-%{version}.tar.bz2
# Source0-md5:	6a686b6aef33939186147c1037a9ad23
Patch0:		xfwp-man.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-proto-xproxymanagementprotocol-devel
BuildRoot:	%{tmpdir}/xfwp-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
xfwp application.

%description -l pl
Aplikacja xfwp.


%prep
%setup -q -n xfwp-%{version}
%patch0 -p1


%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%attr(755,root,wheel) %{_bindir}/*
%{_mandir}/man1/*.1*
