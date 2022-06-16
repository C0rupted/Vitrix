import json, os

if os.getcwd().split(os.path.sep)[-1] == 'vitrix':
    settings_path = "user/settings.json"
else:
    settings_path = "vitrix/user/settings.json"

settings_file = open("vitrix/user/settings.json", "r")
settings = json.loads(settings_file.read()) # dict

# read the json settings file
def sread(a: str, b: str): # sread('gameplay_settings', 'fov')
    return settings[a][b]

def swrite(a: str, b: str, c: str): # swrite('gameplay_settings', 'fov', 80)
    settings[a][b] = c
    with open(settings_path, "w") as file:
        json.dump(settings, file)

