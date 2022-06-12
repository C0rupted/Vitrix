# Setting Up A Vitrix Server

Vitrix servers are places to play and communicate with your friends. Setting up a server is easy.


## Requirements
Vitrix servers should work on any platform that can run Python. However, it is recommended to use Linux as you may encounter some problems with
the Windows 10/11 firewall and port-forwarding, but on Linux, all these steps are easy, and as python comes preinstalled, the firewall problems don't apply.

## Starting your server
1. First of all, make sure you have cloned Vitrix or downloaded the [zip](https://github.com/ShadityZ/Vitrix/archive/refs/heads/master.zip).
Make sure your terminal's working directory is where you cloned/extracted Vitrix.
```
cd /path/to/Vitrix
```
2. Then, make sure you have python ```3.9.7``` installed, as it is the only tested version of python for Vitrix. Then starting the Vitrix server is
as easy as running the following command:
```
python server/server.py
```
#### Finding your Server's IP
Then you have succesfully started your Vitrix server! On Linux, you can check the IP address by running: ```ifconfig```. If you get an error, saying,
```
Command 'ifconfig' not found
```
then simply run:
```
apt/dnf/yum install net-tools
```
and try again. On Windows, it is as simple as running, ```ipconfig /all``` and finding the section labeled: ```IPv4 Address: ```. By default, the
server will used port ```26822```, if you would like to change it, simply edit line 19 ```server.py```, to ```PORT = <number>```. Be sure to replace the 
```<number>``` to the port number you would like.
