# Installing Vitrix

**NOTICE:** Vitrix has plans to upload prebuilt applications every month. The next prebuilt will be coming out in this month. 

### Requirements
Vitrix has been official tested on the following platforms:

![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)


The following platforms are supported, but are still in _MAJOR_ development:


![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white) 


And is working on support for:

![Mac OS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0) 
![Raspberry Pi](https://img.shields.io/badge/-RaspberryPi-C51A4A?style=for-the-badge&logo=Raspberry-Pi)

##### Hardware Requirements
- A 1GHz or faster 64-bit processer (essentially any decent processor)
- A minimum 4 GB of RAM (pretty common in most computers)
- At least 30 MB of free disk 

##### Software Requirements
- Python 3

### Instructions - Prebuilts
Prebuilts are packages that come with a bundled Python binary, so you don't have to install Python to use Vitrix! You can find the latest prebuilt on our github releases page: https://github.com/ShadityZ/Vitrix/releases

Once you find the latest release, you'll notice that the release has multiple download options. You can download the one that has your operating system's anme appended on the end. (example: ```Vitrix-v1.x.x-[os name].zip```) Then simply extract the zip file and run the ```vitrix``` file inside!
### Instructions - Running Directly
1. First of all, clone the repository using Git SCM or download the [zip](https://github.com/ShadityZ/Vitrix/archive/refs/heads/master.zip):
```
git clone https://github.com/ShadityZ/Vitrix
```
2. If you have downloaded the zip, extract it, ```cd``` into the cloned repository/extracted zip:
```
cd path/to/vitrix/source
```
4. Install Vitrix's dependencies:
```
pip install -r requirements.txt
```
4. On Linux you will also need to install a few packages:
```
sudo apt/dnf/yum install python3-tk python-is-python3
```
5. Well done! Now you can run the ```menu.py``` script in the ```vitrix``` folder to start Vitrix.
