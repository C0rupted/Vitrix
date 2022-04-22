import sys
import configparser

def perform_quit():
    print("Found cheat. Quitting...")
    options_parser = configparser.ConfigParser()
    options_parser.read("options.ini")

    if "Infos" not in options_parser.sections():
        options_parser.add_section("Infos")
        options_parser.set("Infos", "c", "True")
    else:
        if "c" not in options_parser["Infos"]:
            options_parser.set("Infos", "c", "True")
    sys.exit(1)

def check_speed(speed: int, valid_speeds: list):
    if speed not in valid_speeds:
        perform_quit()