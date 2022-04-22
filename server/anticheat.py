import sys

def check_speed(speed: int, valid_speeds: list):
    if speed not in valid_speeds:
        sys.exit(0)