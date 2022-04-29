import json

settings_file = open("../user/settings.json", "r").read()

settings = json.load(settings_file)