#!/bin/bash

#
cd /home/pi
echo "alias transmit='sudo lmic-rpi-lora-gps-hat/examples/transmit/build/transmit.out'" >> .bashrc
echo "alias brain='sudo python3 ~/MasterCode/brain.py'" >> .bashrc
echo ". node/login.sh" >> .bashrc

echo "this script will now delete itself"
rm -- $0
