import sys
import configparser

def perform_quit():
    print("Found cheat. Quitting...")

    with open("ib.cfg", "w") as f:
        f.write("1")
    with open("../ib.cfg", "w") as f:
        f.write("1")
    
    sys.exit(1)

def check_speed(speed: int, valid_speeds: list):
    if speed not in valid_speeds:
        perform_quit()