# ethermail
website https://ethermail.io/

Web 3.0 Email Solution setting the standard for anonymous and encrypted wallet-to-wallet communication.

# Environment Setup

You need to install the following environment on your ubuntu

```shell 
pip3 install requests
pip3 install selenium
pip3 install urllib3
adduser vnc
addgroup vnc sudo
sudo apt install ubuntu-desktop -y
wget http://mirror.cs.uchicago.edu/google-chrome/pool/main/g/google-chrome-stable/google-chrome-stable_107.0.5304.68-1_amd64.deb
sudo dpkg -i google-chrome-stable_107.0.5304.68-1_amd64.deb
wget https://chromedriver.storage.googleapis.com/107.0.5304.62/chromedriver_linux64.zip
unzip chromedriver_linux64.zip 
cp chromedriver /usr/local/bin/
mkdir /home/vnc/ethermail /home/vnc/ethermail/tool
chmod 777 -R /home/vnc/ethermail/*
chmod 777 -R /home/vnc/ethermail/
```
# How does it work?

```angular2html
python3 ubuntu.py
```

# what needs attention？
* ubuntu version need > 18.10LTS
* you need set the vnc passwd in the wizard interface
* you need update ethermail.db，For example my table structure
* you need change invite link to youself in line_94
