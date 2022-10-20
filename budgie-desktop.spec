%define girname %mklibname %{name}-gir
%define devname %mklibname -d %{name}

%define major 0
%define libraven %mklibname raven %{major}
%define libbudgietheme %mklibname budgietheme %{major} 
%define libbudgieplugin %mklibname budgie-plugin %{major} 
%define libbudgieprivate %mklibname budgie-private %{major} 

%global optflags %{optflags} -Wno-error -Wno-implicit-function-declaration

Name:           budgie-desktop
Version:        10.6.4
Release:        3
Summary:        GTK3 Desktop Environment
License:        GPL-2.0+ AND LGPL-2.1
Group:          Graphical desktop/Budgie
Url:            https://solus-project.com/budgie/
Source0:        https://github.com/BuddiesOfBudgie/budgie-desktop/releases/download/v%{version}/budgie-desktop-v%{version}.tar.xz

BuildRequires:  git
BuildRequires:  gtk-doc
BuildRequires:  cmake
BuildRequires:  intltool
BuildRequires:  meson >= 0.41.2
BuildRequires:  vala-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  gnome-settings-daemon-devel
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gnome-bluetooth-1.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(libgnome-menu-3.0)
BuildRequires:  pkgconfig(libpeas-gtk-1.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(libmutter-11)
BuildRequires:  sassc
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  egl-devel
BuildRequires:  budgie-screensaver
BuildRequires:  budgie-desktop-view

Requires:       budgie-desktop-view
Requires:       budgie-screensaver
Requires:       budgie-control-center
Requires:       gnome-bluetooth3.34
Requires:       gnome-session

Suggests:       materia-gtk-theme
Suggests:       papirus-icon-theme

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

%find_lang %{name}

%files -f %{name}.lang
%doc LICENSE LICENSE.LGPL2.1
%dir %{_datadir}/gnome-session
%dir %{_datadir}/gnome-session/sessions
%{_bindir}/budgie-*
%{_datadir}/applications/budgie-*.desktop
%{_datadir}/budgie/budgie-version.xml
%{_datadir}/glib-2.0/schemas/com.solus-project.*.gschema.xml
%{_datadir}/gnome-session/sessions/budgie-desktop.session
%{_datadir}/icons/hicolor/scalable/*/*.svg
%{_datadir}/backgrounds/budgie/default.jpg
%{_datadir}/xsessions/budgie-desktop.desktop
%{_libdir}/budgie-desktop/
%{_sysconfdir}/xdg/autostart/budgie-desktop-nm-applet.desktop
%{_sysconfdir}/xdg/autostart/budgie-desktop-screensaver.desktop

%files -n %{libraven}
%{_libdir}/libraven.so.*

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

%files -n %{girname}
%{_libdir}/girepository-1.0/Budgie-1.0.typelib
%{_datadir}/gir-1.0/Budgie-1.0.gir
%{_datadir}/glib-2.0/schemas/20_solus-project.budgie.wm.gschema.override

%files docs
%{_datadir}/gtk-doc/html/budgie-desktop/
%{_mandir}/man1/budgie-*
