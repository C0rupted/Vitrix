import os
import time
import shutil
import datetime
import platform
import subprocess



def run(command, output=1):
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, 
                            stderr=subprocess.STDOUT)
    if output == 1:
        while proc.poll() is None:
            temp = str(proc.stdout.readline()).split("'")
            temp = temp[1].split("\\")
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
build_path = dir_path + "/build"
d = datetime.datetime.now()
vitrix_ver = d.strftime("%m-%Y")

if platform.system() == "Linux":
    operating_sys = "linux"
elif platform.system() == "Windows":
    #operating_sys = "windows"
    print("Sorry, Vitrix doesn't support your platform just yet. :(")
elif platform.system() == "Darwin":
    #operating_sys = "mac"
    print("Sorry, Vitrix doesn't support your platform just yet. :(")
else:
    print("Sorry, Vitrix doesn't support your platform just yet. :(")

print("\nBuild Path:        " + build_path)
print_seperator()



print("Preparing...\n")

shutil.rmtree(build_path)
os.chdir(dir_path)

print("Done!")

print_seperator()



start_time = time.time()
print("Building...\n\n")

with open(dir_path + "/requirements.txt") as file:
    packages = file.readlines()

if operating_sys == "linux":
    from venvctl import VenvCtl

    VenvCtl.create_venv(name="python-env", packages=packages,
                        output_dir=build_path)
    shutil.rmtree(build_path + "/builds")
    shutil.rmtree(build_path + "/reports")
    shutil.copy("data/linux/vitrix.sh", "build")


shutil.copytree(dir_path + "/vitrix", build_path + "/src", 
                ignore=shutil.ignore_patterns("__pycache__"))

pkg_name = "Vitrix_" + vitrix_ver + "_" + operating_sys


shutil.make_archive(pkg_name, "zip", build_path)



d = datetime.datetime.now()

print_seperator()
print("Build Successfully Completed!")
print("Finished On:     " + d.strftime("%I:%M %p %A %B %Y"))
print("\nTotal Build Time:      " + str(time.time() - start_time) + " seconds")