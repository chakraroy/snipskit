# snipskit

### Update the Raspberry Pi
_____
```
sudo apt-get update
sudo apt-get upgrade
```

### Install git and pip to install from github and other python libs we will need
_____
```
sudo apt-get install python-pip
sudo apt-get install python-git
```

### Download the Respeaker driver for the mic
_____
```
git clone https://github.com/respeaker/seeed-voicecard.git
cd seeed-voicecard
sudo ./install.sh 2mic
```

### Install Snips Voice Platform
_____
```
sudo apt-get install -y dirmngr
sudo bash -c  'echo "deb https://raspbian.snips.ai/$(lsb_release -cs) stable main" > /etc/apt/sources.list.d/snips.list'
sudo apt-key adv --keyserver pgp.mit.edu --recv-keys D4F50CDCA10A2849

sudo apt-get update
sudo apt-get install -y snips-platform-voice

sudo reboot
```

#### Build your Snips assistant from the [Snips Console](https://console.snips.ai)

Goto the Snips Console, create an account if you do not already have one.</br>
Start creating your assistant, choice the language, device, wake word.</br>
And then build some bundles of what intents your assistant has to learn about.</br>


#### Download and install your assistant onto the Pi
**copy** the downloaded assistant file from your computer to the pi

`scp <folder_location/assistant.zip pi@raspberrypi.local:/home/pi/assistant.zip`


**remove** old assistant if you have installed one previously

`rm -rf /usr/share/snips/assistant`


**install** the newly downloaded assistant from the console

`unzip /home/pi/assistant.zip -d /usr/share/snips`

#### Setup the python code to 'do something' when the intent is detected
_____
Install some extra needed python libraries 
```
sudo pip install paho-mqtt
sudo pip install spidev
```

To control the LEDs on the Respeaker mic HAT we need to enable SPI
`sudo raspi-config` 

We are going to make this a *service* on the Pi so it loads after a reboot
```
sudo cp pixel.service /lib/systemd/system/pixel.service
chmod +x pixel.py
sudo systemctl enable pixel.service
sudo systemctl start pixel.service
sudo systemctl status pixel.service
```
This copies the service file to the Pis service directory, we change the pixel.py file to have execution permission and then enable/start the service and check its status to make sure its working or if there was a problem





