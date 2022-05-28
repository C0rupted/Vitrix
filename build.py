import os
import time
import shutil
import datetime
import platform
import subprocess

from os.path import join

sep = os.path.sep

def run(command, output=1):
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, 
                            stderr=subprocess.STDOUT)
    if output == 1:
        while proc.poll() is None:
            temp = str(proc.stdout.readline()).split("'")
            temp = temp[1].split(sep)
            print(temp[0])
    commandResult = proc.wait()
    if commandResult == 0:
        return True
    else:
        print("\nERROR")
        exit()


def print_seperator():
    columns = str(os.get_terminal_size()).split("=")[1].split(",")[0]
    print()
    print("-" * int(columns))
    print()



dir_path = os.path.dirname(os.path.realpath(__file__))
build_path = join(dir_path, "build")
d = datetime.datetime.now()

if platform.system() == "Linux":
    operating_sys = "linux"
elif platform.system() == "Windows":
    operating_sys = "windows"
else:
    print("Sorry, Vitrix doesn't support your platform just yet. :(")

print("\nBuild Path:        " + build_path)
print_seperator()



print("Preparing...\n")
try:
    shutil.rmtree(build_path)
except:
    os.mkdir(build_path)
os.chdir(dir_path)

print("Done!")

print_seperator()



start_time = time.time()
print("Building...\n\n")

with open(join(dir_path, "requirements.txt")) as file:
    packages = file.readlines()

if operating_sys == "linux":
    from venvctl import VenvCtl

    VenvCtl.create_venv(name="python-env", packages=packages,
                        output_dir=build_path)
    shutil.rmtree(join(build_path, "builds"))
    shutil.rmtree(join(build_path, "reports"))
    shutil.copy(join("data", "linux", "vitrix.sh"), "build")
    shutil.copy(join("data", "linux", "singleplayer.sh"), "build")
    shutil.copy(join("data", "linux", "multiplayer.sh"), "build")


if operating_sys == "windows":
    from zipfile import ZipFile

    with ZipFile(join(dir_path, "data", "windows", "python-windows.zip"), "r") as zip:
        zip.extractall(build_path)
    

    shutil.copy(join("data", "windows", "vitrix.bat"), "build")
    shutil.copy(join("data", "windows", "singleplayer.bat"), "build")
    shutil.copy(join("data", "windows", "multiplayer.bat"), "build")


shutil.copytree(join(dir_path, "vitrix"), join(build_path, "vitrix"), 
            ignore=shutil.ignore_patterns("__pycache__"))
os.remove(f"{build_path}{sep}vitrix{sep}.unbuilt")

pkg_name = f"Vitrix-vX.X.X-{operating_sys}"


shutil.make_archive(pkg_name, "zip", build_path)



d = datetime.datetime.now()

print_seperator()
print("Build Successfully Completed!")
print("Finished On:     " + d.strftime("%I:%M %p %A %B %Y"))
print(f"\nTotal Build Time:      {str(time.time() - start_time)} seconds")