# node
# nodeSetup.sh
CHANGE THE PASSWORD FIRST with the `passwd`

Setup internet:

`sudo raspi-config`

```
sudo apt update
sudo apt upgrade
```

Now install the node software:

```
sudo apt install git
git clone https://github.com/jp-chickadee-project/node.git
sudo ./node/nodeSetup.sh
```
 

