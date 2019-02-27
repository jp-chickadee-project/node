#!/bin/bash
echo "Initializing $1"
echo "Adding user pi to dialout"
usermod -a -G dialout pi
cd /home/pi
echo "Downloading git"
apt install git
echo "Installing rpi.gpio"
apt install rpi.gpio
echo "Installing pip3"
apt install python3-pip
echo "Installing pyserial"
pip3 install pyserial
echo "Enabling serial UART"
sed -i -e 's/ console=serial0,115200//g' /boot/cmdline.txt
echo 'enable_uart=1' >> /boot/config.txt
echo "Enabling SPI"
echo 'dtparam=spi=on' >> /boot/config.txt
echo "Downloading LMIC"
git clone https://github.com/wklenk/lmic-rpi-lora-gps-hat.git
chown -R pi:pi lmic-rpi-lora-gps-hat
echo "Downloading WiringPi"
git clone git://git.drogon.net/wiringPi
chown -R pi:pi wiringPi
echo "Installing WiringPi"
cd /home/pi/wiringPi
git pull origin
./build
cd /home/pi
echo "Enabling SSH."
systemctl enable ssh
echo "Changing keyboard layout"
sed -i -e 's/XKBLAYOUT="gb"/XKBLAYOUT="us"/g' /etc/default/keyboard
echo "Changing Hostname"
sed -i -e "s/raspberrypi/$1/g" /etc/hostname
sed -i -e "s/raspberrypi/$1/g" /etc/hosts
echo "Installing fail2ban"
reboot
