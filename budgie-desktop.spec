%define girname %mklibname %{name}-gir
%define devname %mklibname -d %{name}

%define major 0
%define libraven %mklibname raven %{major}
%define libbudgietheme %mklibname budgietheme %{major} 
%define libbudgieplugin %mklibname budgie-plugin %{major} 
%define libbudgieprivate %mklibname budgie-private %{major} 

%global optflags %{optflags} -Wno-error -Wno-implicit-function-declaration
%global optflags %{optflags} -Wno-incompatible-function-pointer-types

Name:           budgie-desktop
Version:        10.9.2
Release:        8
Summary:        GTK3 Desktop Environment
License:        GPL-2.0+ AND LGPL-2.1
Group:          Graphical desktop/Budgie
Url:            https://solus-project.com/budgie/
Source0:        https://github.com/BuddiesOfBudgie/budgie-desktop/releases/download/v%{version}/budgie-desktop-v%{version}.tar.xz
# FIXME: move this to distro-release
Source100:		budgie-openmandriva.gschema.override

BuildRequires:  git
BuildRequires:  gtk-doc
BuildRequires:  cmake
BuildRequires:  intltool
BuildRequires:  meson >= 0.41.2
BuildRequires:  vala-devel
BuildRequires:  zenity-gtk
BuildRequires:  pkgconfig(alsa)
BuildRequires:  gnome-settings-daemon-devel
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gnome-bluetooth-1.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libgnome-menu-3.0)
BuildRequires:  pkgconfig(libpeas-gtk-1.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(libxfce4windowing-0)
# Mutter was replaced by magpie
#BuildRequires:  pkgconfig(libmutter-12)
BuildRequires:  pkgconfig(libmagpie-0)
BuildRequires:  sassc
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  egl-devel
BuildRequires:  budgie-screensaver
BuildRequires:  budgie-desktop-view

Requires:       %{girname} = %{EVRD}
Requires:       %{libraven} = %{EVRD}
Requires:       %{libbudgieplugin} = %{EVRD}
Requires:       %{libbudgieprivate} = %{EVRD}

Requires:       budgie-session
Requires:       budgie-desktop-view
Requires:       budgie-screensaver
Requires:       budgie-control-center
Requires:       budgie-backgrounds
Requires:       gnome-bluetooth3.34
Requires:       gnome-settings-daemon
Requires:       gsettings-desktop-schemas
Requires:       gnome-keyring
Requires:       networkmanager-applet
Requires:       hicolor-icon-theme
Requires:       materia-gtk-theme
Requires:       papirus-icon-theme
Requires:       xdotool
Requires:       %{_lib}xfce4windowing
Recommends:     switcheroo-control
Recommends:     gnome-terminal

Requires: glib2.0-common
Requires: glib2
Requires: gtk+3

Provides: budgie
Provides: task-budgie
Provides: task-budgie-desktop

%description
Budgie Desktop is the flagship desktop for the Solus Operating System.

%package -n	%{girname}
Summary:        Introspection bindings for the Budgie Desktop
Group:          System/Libraries
Requires:       %{libraven} = %{EVRD}
Requires:       %{libbudgieplugin} = %{EVRD}
Requires:       %{libbudgieprivate} = %{EVRD}

%description -n %{girname}
This package provides GObject Introspection files required for
developing Budgie Applets using interpreted languages, such as Python
GObject Introspection bindings.

%package -n	%{devname}
Summary:        Development files for the Budgie Desktop
Group:          Development/Libraries/GNOME
Requires:       %{name} = %{version}-%{release}
Requires:       %{girname} = %{EVRD}
Requires:       %{libraven} = %{EVRD}
Requires:       %{libbudgieplugin} = %{EVRD}
Requires:       %{libbudgieprivate} = %{EVRD}

%description -n %{devname}
This package provides development files required for software to be
able to use and link against the Budgie APIs, to create their own
applets for the Budgie Panel.

%package docs
Summary:        Documentation files for the Budgie Desktop
Group:          Documentation/HTML

%description docs
This package provides API Documentation for the Budgie Plugin API, in the
GTK-Doc HTML format.

%package -n	%{libraven}
Summary:        Shared library for Raven
Group:          System/Libraries

%description -n %{libraven}
Budgie Desktop Notification Center.

%package -n %{libbudgietheme}
Summary:        Shared library for Budgie theming
Group:          System/Libraries

%description -n %{libbudgietheme}
Budgie theming engine shared library package.

%package -n %{libbudgieplugin}
Summary:        Shared library for Budgie plugins
Group:          System/Libraries

%description -n %{libbudgieplugin}
Shared library for budgie plugins to link against.

%package -n %{libbudgieprivate}
Summary:        Shared library for Budgie plugins
Group:          System/Libraries

%description -n %{libbudgieprivate}
Shared library for budgie plugins to link against.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
#export CC=gcc
#export CXX=g++
%meson
%meson_build

%install
export LANG=en_US.UTF-8
%meson_install

# OpenMandriva style
install -pm 0644 %{SOURCE100} %{buildroot}%{_datadir}/glib-2.0/schemas/budgie-openmandriva.gschema.override

%find_lang %{name}

%files -f %{name}.lang
%doc LICENSE LICENSE.LGPL2.1
%dir %{_datadir}/gnome-session
#dir %{_datadir}/gnome-session/sessions
%{_bindir}/budgie-*
%{_bindir}/org.buddiesofbudgie.BudgieScreenshot
%{_bindir}/org.buddiesofbudgie.sendto
%{_datadir}/applications/org.buddiesofbudgie.*
%{_datadir}/budgie/budgie-version.xml
%{_datadir}/glib-2.0/schemas/com.solus-project.*.gschema.xml
%{_datadir}/gnome-session/sessions/org.buddiesofbudgie.BudgieDesktop.session
%{_datadir}/icons/hicolor/scalable/*/*.svg
%{_datadir}/backgrounds/budgie/default.jpg
%{_datadir}/xsessions/budgie-desktop.desktop
%{_datadir}/xdg-desktop-portal/budgie-portals.conf
%{_libdir}/budgie-desktop/
%{_sysconfdir}/xdg/autostart/org.buddiesofbudgie.BudgieDesktopNmApplet.desktop
%{_sysconfdir}/xdg/autostart/org.buddiesofbudgie.BudgieDesktopScreensaver.desktop
%{_sysconfdir}/xdg/autostart/org.buddiesofbudgie.BudgiePowerDialog.desktop
%{_sysconfdir}/xdg/autostart/org.buddiesofbudgie.sendto-daemon.desktop
%{_datadir}/glib-2.0/schemas/20_solus-project.budgie.wm.gschema.override
%{_datadir}/glib-2.0/schemas/20_buddiesofbudgie.budgie-desktop.notifications.gschema.override
%{_datadir}/glib-2.0/schemas/org.buddiesofbudgie.*
%{_libexecdir}/budgie-desktop/budgie-polkit-dialog
%{_libexecdir}/budgie-desktop/budgie-power-dialog
%{_datadir}/glib-2.0/schemas/budgie-openmandriva.gschema.override

%files -n %{libraven}
%{_libdir}/libraven.so.*
%{_libdir}/libbudgie-raven-plugin.so.*
%{_libdir}/libbudgie-appindexer.so.*

%files -n %{libbudgietheme}
%{_libdir}/libbudgietheme.so.*

%files -n %{libbudgieplugin}
%{_libdir}/libbudgie-plugin.so.*

%files -n %{libbudgieprivate}
%{_libdir}/libbudgie-private.so.*

%files -n %{devname}
%dir %{_includedir}/budgie-desktop
%{_includedir}/budgie-desktop/*.h
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_datadir}/vala/vapi/budgie-1.0.*
%{_datadir}/vala/vapi/budgie-raven-plugin-1.0.deps
%{_datadir}/vala/vapi/budgie-raven-plugin-1.0.vapi

%files -n %{girname}
%{_libdir}/girepository-1.0/BudgieRaven-1.0.typelib
%{_libdir}/girepository-1.0/Budgie-1.0.typelib
%{_datadir}/gir-1.0/Budgie-1.0.gir
%{_datadir}/gir-1.0/BudgieRaven-1.0.gir

%files docs
%{_datadir}/gtk-doc/html/budgie-desktop/
%{_mandir}/man1/budgie-*
%{_mandir}/man1/org.buddiesofbudgie.BudgieScreenshot.1.*
%{_mandir}/man1/org.buddiesofbudgie.sendto.1.*
