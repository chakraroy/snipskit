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

sudo apt-get install snips-watch

sudo reboot
```

#### Build your Snips assistant from the [Snips Console](https://console.snips.ai)

Goto the Snips Console, create an account if you do not already have one.</br>
Start creating your assistant, choice the language, device, wake word.</br>
And then build some bundles of what intents your assistant has to learn about.</br>


#### Download and install your assistant onto the Pi
**copy** the downloaded assistant file from your computer to the pi. This command is run from your computer not the Pi. It will copy the file from the location provided to the Pi's home directory

`scp <folder_location>/assistant_proj########.zip pi@raspberrypi.local:/home/pi/assistant.zip`


**remove** old assistant if you have installed one previously

`sudo rm -rf /usr/share/snips/assistant`


**install** the newly downloaded assistant from the console

`sudo unzip /home/pi/assistant.zip -d /usr/share/snips`

*I have included my demo assistant file used in the video here*
_____

#### Setup the python code to 'do something' when the intent is detected

Install some extra needed python libraries 
```
sudo apt-get install python-setuptools
sudo apt-get install python-dev
sudo pip install wheel
sudo pip install paho-mqtt
sudo pip install spidev
```
When I tried to install paho-mqtt and spidev with `sudo` I ran into problems, but works fine without `sudo`

To control the LEDs on the Respeaker mic HAT we need to enable SPI
`sudo raspi-config` 

We are going to make this a *service* on the Pi so it loads after a reboot
```
git clone https://github.com/oziee/snipskit.git
sudo cp pixel.service /lib/systemd/system/pixel.service
chmod +x pixel.py
sudo systemctl enable pixel.service
sudo systemctl start pixel.service
sudo systemctl status pixel.service
```
This service file has coded that the pixel.py file is located in the /home/pi/snipskit directory (you can change it to where every you like as long as thats changed in the service file)

This copies the service file to the Pis service directory, we change the pixel.py file to have execution permission and then enable/start the service and check its status to make sure its working or if there was a problem





