# Building (WIP - THIS ARTICLE IS INCOMPLETE)
## Installing prerequisites
First of all, you should go set up Vitrix, if you haven't already.<br>
Then, go ahead and install [Nuitka](https://nuitka.net/), it is the compiler we're going to be using to build Vitrix: (You will also need ```imageio```)
```
pip3 install nuitka imageio
```
On Linux, you will also need to install ```patchelf```:
```
apt/dnf/yum install patchelf
```
It's usually best to create a copy of the repository's files and then run the build the copy.
Now ```cd``` into the directory where you have cloned Vitrix:
```
cd path/to/Vitrix/
```
Finally to build, run:
```
python -m nuitka --standalone --onefile --windows-icon-from-ico=logo.png main.py --plugin-enable=pyqt5,numpy --nofollow-import-to=wx
```
If Nuitka ask you a question, just answer ```yes``` or ```y``` and let it proceed.
When the process finshes, you will have an output file and two folders. The output folders will be ```main.dist``` and ```main.build```. However, the file's name varies on different operating systems. If you're on Windows, the file will be ```main.exe```. On Linux and on MacOS, it will be ```main.bin```. 

It is recommended you rename the file to ```Vitrix-(version)-(OS).(extension)```. Be sure to replace the ```(version)``` with the actual version, ```(OS)``` with the OS it is built for and ```(extension)``` with the filename extension. If you have any problems with the build process, please create an issue on the [issues page](https://github.com/ShadityZ/Vitrix/issues).
