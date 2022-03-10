# Building (WIP - THIS ARTICLE IS INCOMPLETE)
## Installing prerequisites
First of all, you should go set up Vitrix, if you haven't already.<br>
Then, go ahead and install [Nuitka](https://nuitka.net/), it is the compiler we're going to be using to build Vitrix: (You will also need ```imageio```)
```
pip3 install nuitka imageio
```
Now ```cd``` into the directory where you have cloned Vitrix:
```
cd path/to/Vitrix/
```
Finally to build, run:
```
python -m nuitka --standalone --onefile --windows-icon-from-ico=logo.png main.py
```
This will give you a file. If you're on Windows, it will be ```main.exe```. On Linux or MacOS, it will be ```main.bin```. It is recommended you rename it to ```Vitrix-(version)-(OS)```. Be sure to replace the ```(version)``` with the actual version and ```(OS)``` with the OS it is built for. If you have any problems with the build process, please create an issue on the [issues page](https://github.com/ShadityZ/Vitrix/issues).
