# Installing Vitrix

**NOTICE:** Vitrix has plans to upload prebuilt applications every month. The next prebuilt will be coming out in this month. 
### Requirements
Vitrix has been official tested on the following platforms:

![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)

And is working on support for:

![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white) 
![Mac OS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0) 
![Raspberry Pi](https://img.shields.io/badge/-RaspberryPi-C51A4A?style=for-the-badge&logo=Raspberry-Pi)

##### Hardware Requirements
- A 1GHz or faster 64-bit processer (essentially any decent processor)
- A minimum 4 GB of RAM (pretty common in most computers)
- At least 30 MB of free disk 

##### Software Requirements
- Python 3

### Instructions - Prebuilts
Prebuilts aren't done yet, but we will be making one soon, so keep an eye out for them. Similarly, 
a build script for users that would like to build vitrix themselves is also coming out soon.

### Instructions - Running Directly
1. First of all, clone the repository using Git SCM:
```
git clone https://github.com/ShadityZ/Vitrix
```
2. ```cd``` into the cloned repository:
```
cd path/to/vitrix
```
4. Install Vitrix's dependencies:
```
pip install -r requirements.txt
```
4. On Linux you will also need to install a few packages. Here is an example for Debian-based distros:
```
sudo apt install python3-tk python-is-python3
```
5. Well done! Now you can run the ```menu.py``` script in the ```vitrix``` folder to start Vitrix.
