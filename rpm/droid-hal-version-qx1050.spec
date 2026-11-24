%define device qx1050
%define vendor fxtec
%define vendor_pretty F(x)tec
%define device_pretty Pro1-X

%define native_build 1
# Vibration through the AW86224 driver's ff-memless interface
%define have_ffmemless 1
# RGB notification LED on the PMI632
%define have_led 1

%include droid-hal-version/droid-hal-version.inc
