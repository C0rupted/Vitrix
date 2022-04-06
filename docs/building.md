# Building

Building will allow you create portable binaries for your operating system, essentially apps that don't require python installed to run. Building Vitrix 
is really easy, as there is a script to automate all of it! 

### NOTE: At the moment, only Linux is supported. Windows and MacOS support will be coming soon.

First, make sure your terminal has the vitrix folder selected as the main working folder, then just execute the ```build.py``` script:
```
cd /path/to/Vitrix

python build.py
```

A zip file will be output in the root folder of the Vitrix repository. It will be something like: ```Vitrix_04-22_linux.zip```
Most issues with the build script has been fixed, but Windows support is a WIP, so don't expect it to fire up without any bugs.

If you have any problems with the build process, please create an issue on the [issues page](https://github.com/ShadityZ/Vitrix/issues).
