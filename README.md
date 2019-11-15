# node
# nodeSetup.sh
Use the most up-to date image for Rasbian lite

CHANGE THE PASSWORD FIRST with the `passwd` command

Setup internet:

`sudo raspi-config`

Make sure the system is updated:
```
sudo apt-get update
sudo apt-get -y upgrade
```

Now install the node software:

```
sudo apt-get install -y  git
git clone https://github.com/jp-chickadee-project/node.git
sudo ./node/nodeSetup.sh
```
 

