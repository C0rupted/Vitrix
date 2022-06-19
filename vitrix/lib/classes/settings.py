import json

try:
    settings_file = open("user/settings.json", "r")
except:
    settings_file = open("vitrix/user/settings.json", "r")

settings = json.loads(settings_file.read()) # dict


# read the json settings file
def sread(a: str, b: str): # sread('gameplay_settings', 'fov')
    return settings[a][b]

def swrite(a: str, b: str, c: str): # swrite('gameplay_settings', 'fov', 80)
    #############################################
    #### Removed this because it doesn't work####
    #############################################

    # with open("user/settings.json", "r+") as wsettings:
    #     ndsettings = json.load(wsettings)
    #     temp = ndsettings['gameplay_settings']
    #     to_write = temp['fov'] = c
    #     wsettings.seek(0)
    #     json.dump(to_write, wsettings, indent=4)
    #     wsettings.truncate()
    pass


def set_fov(fov: int):
    swrite('gameplay_settings', 'fov', str(fov))


def get_fov():
    return int(sread('gameplay_settings', 'fov'))
