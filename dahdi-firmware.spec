Name:		dahdi-firmware
Summary:	Non-free firmware for dahdi
Group:		System/Kernel and hardware
Version:	2.6.1
Release:	3
License:	Proprietary
URL:		http://www.asterisk.org/
# firmware extracted from http://downloads.asterisk.org/pub/telephony/dahdi-linux/dahdi-linux-%{version}.tar.gz
Source0:	%{name}-%{version}.tar.xz
BuildArch:	noarch

Requires:	make wget

%description
This package includes the non-free firmwares from the DAHDI tarball as well
as downloading script for the Digium firmwares that are normally downloaded
on 'make install'.

Attention: you need active Internet connection during this package
installation. If Network was unavailable, you can download and install firmware
later by running the following command as root:

  make -C %{_datadir}/%{name} HOTPLUG_FIRMWARE=yes hotplug-install

%prep
%setup -q

%build

%install
install -d -m 755 %{buildroot}%{_datadir}/dahdi
cp xpp/firmwares/*.hex %{buildroot}%{_datadir}/dahdi/
install -D -m 644 firmware/Makefile %{buildroot}%{_datadir}/%{name}/Makefile

%post
make -C %{_datadir}/%{name} HOTPLUG_FIRMWARE=yes hotplug-install

%preun
make -C %{_datadir}/%{name} HOTPLUG_FIRMWARE=yes hotplug-uninstall

%files
%doc xpp/firmwares/LICENSE.firmware
%doc xpp/firmwares/README
%{_datadir}/dahdi/*
%{_datadir}/%{name}/*
