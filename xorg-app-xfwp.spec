Summary:	xfwp application - X firewall proxy
Summary(pl.UTF-8):	Aplikacja xfwp - proxy X dla firewalli
Name:		xorg-app-xfwp
Version:	1.0.2
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xfwp-%{version}.tar.bz2
# Source0-md5:	eeb558aad30a8b2bc1f1f0e919ea6f38
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-xtrans-devel
BuildRequires:	xorg-proto-xproxymanagementprotocol-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The X firewall proxy (xfwp) is an application layer gateway proxy
that may be run on a network firewall host to forward X traffic
across the firewall. Used in conjunction with the X server Security
extension and authorization checking, xfwp constitutes a safe, simple,
and reliable mechanism both to hide the addresses of X servers located
on the Intranet and to enforce a server connection policy. xfwp cannot
protect against mischief originating on the Intranet; however, when
properly configured it can guarantee that only trusted clients
originating on authorized external Internet hosts will be allowed
inbound access to local X servers.

%description -l pl.UTF-8
xfwp (X firewall proxy) to bramka proxy w warstwie aplikacyjnej, którą
można uruchomić na komputerze będącym firewallem sieciowym w celu
przekazywania ruchu X poprzez zaporę. W połączeniu z rozszerzeniem
Security serwera X oraz sprawdzaniem autoryzacji xfwp tworzy
bezpieczny, prosty i niezawodny mechanizm zarówno do ukrywania adresów
serwerów X położonych w intranecie, jak i wymuszania polityki
bezpieczeństwa. xfwp nie może zabezpieczyć przed szkodami z wewnątrz
intranetu, ale odpowiednio skonfigurowany może zagwarantować, że tylko
zaufani klienci łączący się z autoryzowanych komputerów w Internecie
będą mogli połączyć się z lokalnymi serwerami X.

%prep
%setup -q -n xfwp-%{version}

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
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/xfwp
%{_mandir}/man1/xfwp.1x*
