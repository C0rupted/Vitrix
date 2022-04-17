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

with open(dir_path + "/requirements.txt") as file:
    packages = file.readlines()

if operating_sys == "linux":
    from venvctl import VenvCtl

    VenvCtl.create_venv(name="python-env", packages=packages,
                        output_dir=build_path)
    shutil.rmtree(build_path + "/builds")
    shutil.rmtree(build_path + "/reports")
    shutil.copy("data/linux/vitrix.sh", "build")
    shutil.copy("data/linux/singleplayer.sh", "build")
    shutil.copy("data/linux/multiplayer.sh", "build")
    
    shutil.copytree(dir_path + "/vitrix", build_path + "/src", 
                ignore=shutil.ignore_patterns("__pycache__"))
    os.remove(build_path + "/src/.unbuilt")

if operating_sys == "windows":
    run("python -m ursina.build")

    folders_to_remove = [
        "/src/data",
        "/src/server",
        "/src/test",
        "/src/.github"
    ]

    files_to_remove = [
        "/src/build.pyc",
        "/src/LICENSE",
        "/src/logo.png",
        "/src/requirements.txt",
        "/src/SECURITY.md",
        "/src/README.md",
        "/src/vitrix/.unbuilt",
        "/Vitrix.bat"
    ]


    for item in folders_to_remove:
        shutil.rmtree(build_path + item)

    for item in files_to_remove:
        os.remove(build_path + item)
    
    shutil.copy(dir_path + "/data/windows/vitrix.bat", build_path)
    shutil.copy(dir_path + "/data/windows/singleplayer.bat", build_path)
    shutil.copy(dir_path + "/data/windows/multiplayer.bat", build_path)

pkg_name = "Vitrix_" + vitrix_ver + "_" + operating_sys


shutil.make_archive(pkg_name, "zip", build_path)



d = datetime.datetime.now()

print_seperator()
print("Build Successfully Completed!")
print("Finished On:     " + d.strftime("%I:%M %p %A %B %Y"))
print("\nTotal Build Time:      " + str(time.time() - start_time) + " seconds")