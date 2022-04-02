# Setting Up A Vitrix Server

Vitrix servers are places to play and communicate with your friends. Setting up a server is easy.

First of all, make sure you have cloned Vitrix or downloaded the [zip](https://github.com/ShadityZ/Vitrix/archive/refs/heads/master.zip).
Make sure your terminal's working directory is where you cloned/extracted Vitrix.
```
cd /path/to/Vitrix
```
Then, make sure you have python ```3.9.7``` installed, as it is the only tested version of python for Vitrix. Then starting the Vitrix server is
as easy as running the following command:
```
python server/server.py
```
Then you have succesfully started your Vitrix server! On Linux, you can check the IP address by running: ```ifconfig```. If you get an error, saying,
```
Command 'ifconfig' not found
```
then simply run:
```
apt install net-tools
```
and try again. On Windows, it is as simple as running, ```ipconfig /all``` and finding the section labeled: ```IPv4 Address: ```. By default, the
server will used port ```26822```, if you would like to change it, simply edit line 13 ```server.py```, to ```PORT = <number>```. Be sure to replace the 
```<number>``` to the port number you would like.
