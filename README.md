![Logo](https://github.com/VitrixGame/Vitrix/raw/master/logo.png)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/VitrixGame/Vitrix/graphs/commit-activity) [![GitHub license](https://img.shields.io/github/license/VitrixGame/Vitrix.svg)](https://github.com/VitrixGame/Vitrix/blob/master/LICENSE) [![GitHub issues](https://img.shields.io/github/issues/VitrixGame/Vitrix.svg)](https://GitHub.com/VitrixGame/Vitrix/issues/) [![GitHub pull-requests](https://img.shields.io/github/issues-pr/VitrixGame/Vitrix.svg)](https://GitHub.com/VitrixGame/Vitrix/pull/) [![Github all releases](https://img.shields.io/github/downloads/VitrixGame/Vitrix/total.svg)](https://GitHub.com/VitrixGame/Vitrix/releases/) [![GitHub forks](https://img.shields.io/github/forks/VitrixGame/Vitrix.svg?style=social&label=Fork&maxAge=2592000)](https://GitHub.com/VitrixGame/Vitrix/network/) [![GitHub stars](https://img.shields.io/github/stars/VitrixGame/Vitrix.svg?style=social&label=Star&maxAge=2592000)](https://GitHub.com/VitrixGame/Vitrix/stargazers/)

Vitrix is an open-source FPS video game coded in python

## Table of contents
- [Usage](#usage)
  - [Game](#game)
  - [Server](#server)
- [Installing](#installing)
  - [Requirements](#requirements)
      - [Hardware Requirements](#hardware-requirements)
      - [Software Requirements](#software-requirements)
  - [Instructions](#instructions)
- [Building](#building)

## Usage
### Game
You can start the Vitrix Launcher by running the ```main.py``` file in the root directory. Inside the launcher, you can click the ```start``` button, to run Vitrix. It will open a small window, where you can type your desired username. IP address and port options are in the proceeding input fields.

### Server
Starting your own server is simple.
1. Navigate to the project root.
2. ```cd``` into the ```server``` directory:
```
cd server
```
3. And run the ```server.py``` script:
```
python server.py
```
By default the server uses port ```26822```. The IP address can be found using a tool such as [Angry IP Scanner](https://angryip.org/). The server will print its output to the console, so any crashes will be detailed.

## Installing
**NOTICE:** Vitrix has plans to upload prebuilt applications every month. Until March, we will not make a prebuilt application. Until then, we recommend you install Python to run Vitrix 
### Requirements
Vitrix has been official tested on the following platforms:

![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)

And is working on support for:

![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white) ![Mac OS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0)

##### Hardware Requirements
- A 1GHz or faster 64-bit processer (essentially any decent processor)
- A minimum 4 GB of RAM (pretty common in most computers)
- At least 30 MB of free disk 

##### Software Requirements
- Python 3

### Instructions
1. First of all, clone the repository using Git SCM:
```
git clone https://github.com/VitrixGame/Vitrix
```
2. ```cd``` into the cloned repository
3. Install Vitrix's dependencies:
```
pip install -r requirements.txt
```
4. On Linux you will also need to install the python3-tk package. Here is an example for Ubuntu:
```
sudo apt install python3-tk
```
5. Well done! Now you can run the ```main.py``` script in the repository folder to start Vitrix Launcher.

## Building
This section is a WIP