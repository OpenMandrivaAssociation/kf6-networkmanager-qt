%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
%define major %(echo %{version}|cut -d. -f1-2)

%define libname %mklibname KF6NetworkManagerQt
%define devname %mklibname KF6NetworkManagerQt -d
#define git 20240217

Name: kf6-networkmanager-qt
Version: 6.13.0
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/frameworks/networkmanager-qt/-/archive/master/networkmanager-qt-master.tar.bz2#/networkmanager-qt-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/frameworks/%{major}/networkmanager-qt-%{version}.tar.xz
%endif
Summary: Qt wrapper for the NetworkManager DBus API
URL: https://invent.kde.org/frameworks/networkmanager-qt
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Network)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(libnm) >= 1.4.0
Requires: %{libname} = %{EVRD}

%description
Qt wrapper for the NetworkManager DBus API

%package -n %{libname}
Summary: Qt wrapper for the NetworkManager DBus API
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Qt wrapper for the NetworkManager DBus API

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
Requires: pkgconfig(libnm) >= 1.4.0
Requires: pkgconfig(gio-2.0)

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Qt wrapper for the NetworkManager DBus API

%prep
%autosetup -p1 -n networkmanager-qt-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_datadir}/qlogging-categories6/*

%files -n %{devname}
%{_includedir}/KF6/NetworkManagerQt
%{_libdir}/cmake/KF6NetworkManagerQt
%{_libdir}/qt6/doc/KF6NetworkManagerQt.*

%files -n %{libname}
%{_libdir}/libKF6NetworkManagerQt.so*
%{_qtdir}/qml/org/kde/networkmanager
