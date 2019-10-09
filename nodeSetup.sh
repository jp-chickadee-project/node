#!/bin/bash
echo "Enter a name for this node [Example name: node1]"
read -p "---->" name;
echo "Initializing $name"
echo "Adding user pi to dialout"
usermod -a -G dialout pi
cd /home/pi
echo "Downloading git"
apt install -y git
echo "Enabling push down button"
echo 'dtoverlay=gpio-shutdown, gpio_pin=3' >> /boot/config.txt
echo "Installing rpi.gpio"
apt install -y rpi.gpio
echo "installing numpy"
apt install -y python3-numpy
echo "Installing pip3"
apt install -y python3-pip
echo "Installing pyserial"
#pip3 install -y pyserial
apt-get install -y python3-serial
echo "Enabling serial UART"
sed -i -e 's/ console=serial0,115200//g' /boot/cmdline.txt
echo 'enable_uart=1' >> /boot/config.txt
echo "Enabling SPI"
echo 'dtparam=spi=on' >> /boot/config.txt
echo "Downloading LMIC"
git clone https://github.com/jp-chickadee-project/lmic-rpi-lora-gps-hat.git
chown -R pi:pi lmic-rpi-lora-gps-hat
cd /home/pi/lmic-rpi-lora-gps-hat.git
git checkout $name
cd /home/pi
echo "Downloading Mastercode"
git clone https://github.com/jp-chickadee-project/MasterCode.git
chown -R pi:pi MasterCode
echo "Adding MastaCode.py to /etc/rc.local"
sed -i '$i \python3 /home/pi/MasterCode/mastaCode.py &\n' /etc/rc.local
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
sed -i -e "s/raspberrypi/$name/g" /etc/hostname
sed -i -e "s/raspberrypi/$name/g" /etc/hosts
echo "Installing fail2ban"
apt install -y fail2ban
apt install figlet
cd /home/pi/node
./login_setup.sh
mv brain.service /lib/systemd/system
systemctl daemon-reload
systemctl enable brain.service
shutdown -r +1
rm /home/pi/node/login_setup.sh
rm -- $0
