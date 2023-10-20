<p align="center">
    <a href="https://github.com/ShadityZ/Vitrix">
        <img src="https://github.com/ShadityZ/Vitrix/raw/master/logo.png" alt="Vitrix logo" align="left">
    </a>
</p>
<p align="center">Vitrix is an open-source FPS video game coded in <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"></a> !
<p align="center">
  <a href="https://github.com/ShadityZ/Vitrix/discussions">
    📣 Discussions</a>
  |
  <a href="https://github.com/ShadityZ/Vitrix/issues/new">
    ❗ Report an error</a>
  |
  <a href="https://github.com/ShadityZ/Vitrix/pulls/new">
    🎁 Submit a feature</a>
  |
  <a href="https://github.com/ShadityZ/Vitrix/graphs/community">
    📈 Community Insights</a>

<p align="center">
    <a href="https://github.com/ShadityZ/Vitrix/stargazers"><img src="https://img.shields.io/github/stars/ShadityZ/Vitrix" alt="stars"></a>
    <a href="https://github.com/ShadityZ/Vitrix/network/members"><img src="https://img.shields.io/github/forks/ShadityZ/Vitrix" alt="forks"></a>
    <a href="https://github.com/ShadityZ/Vitrix/graphs/contributors"><img src="https://img.shields.io/github/contributors/ShadityZ/Vitrix" alt="contributors"></a>
    <a href="https://github.com/ShadityZ/Vitrix/pulls"><img src="https://img.shields.io/github/issues-pr/ShadityZ/Vitrix" alt="prs"></a>
    <a href="https://github.com/ShadityZ/Vitrix/issues"><img src="https://img.shields.io/github/issues/ShadityZ/Vitrix" alt="issues"></a>
    <img src="https://img.shields.io/github/license/ShadityZ/Vitrix" alt="license">
    <br> Check out the Vitrix:   <a href="https://discord.gg/Vpmwn7HEPp"><img src="https://img.shields.io/badge/Discord-%237289DA.svg?style=for-the-badge&logo=discord&logoColor=white"></a>

<p align="center"><strong>Made with :heart: by <a href="https://github.com/ShadityZ">ShadityZ</a></strong> and <a href="https://github.com/ShadityZ/Vitrix/graphs/contributors">contributors</a>


<br><br>

![Vitrix 1.2.0 Singleplayer development version](https://github.com/ShadityZ/Vitrix/raw/dev/screenshot.png)

    
<br>
Everybody knows lots of diffent FPS shooter games, from Fortnite to CS:GO, the list is longly tiresome. So, what's any different about Vitrix? Well first of all, it has a really cool name. Second of all, it is open-source! No more sneaky malware in your closed-source applications, because the code of Vitrix is fully open and accessible to the community! Well? What are you waiting for? Go ahead and download it if you haven't already, and dive into a world of Vitrix fun!

=======
Frequently Asked Questions (FAQ): 

Game Video/Screen Settings: 

Q: Is there a way to change the screen’s dimensions i.e. width and height? 
	A: Yes! Post-cloning the repository, navigate to the /Vitrix/vitrix/menu.py file. Upon inspecting the code, the “window” object has its attribute size set to two parameters (“default_width” and “default_height”). Initializing these to different integer values will alter the game’s screen dimensions.

Q: Is there a way to toggle whether the screen is borderless or whether it displays in a windowed format? 
	A: Yes! Post-cloning the repository, navigate to the /Vitrix/vitrix/menu.py file. Upon inspecting the code, the “window” object has its attribute borderless which is a boolean toggle for whether the screen is windowed or borderless. As of 2/12/2023, the default setting in the source code is borderless.

Q: Is there a way to toggle whether the screen fullscreen?
	A: Yes! Post-cloning the repository, navigate to the /Vitrix/vitrix/menu.py file. Upon inspecting the code, the “window” object has its attribute fullscreen which is a boolean toggle for whether the game’s contents are shown as fullscreen or not. 

In Game Weapons: 

Q: Where can I access source code for the weapons used in game?
A: Navigate to the directory “/Vitrix/vitrix/lib/weapons” to find the python source code for each item and its in game statistics/specifications. 

Q: I see that within each weapon’s class source code that there is a texture variable being initialized to an image path? Where are these images in the repository?
A: Navigate to the directory “/Vitrix/vitrix/assets/textures” to find the images loaded into the game.

Anticheat/Multiplayer Auditing: 

Q: Does Vitrix have anitcheat functionality implemented for its multiplayer gameplay?
A: Indeed! Navigate to the directory “/Vitrix/vitrix/lib/classes” and access the “anticheat.py” file to see built in precautionary user metric audits to see if gameplay is genuine in its origin.

Q: What are the metrics that Vitrix uses to access whether a player is cheating or not? 
A: If user speed within the game is not within a deemed “normal” range, they will be kicked out of the game’s multiplayer session by a function call named “perform_quit()”. If the jump height integer wise does not match up with the original source code’s jump height, they will also be removed from the game. Artificial manipulated levels of player health exceeding 150 also indicate that the player is cheating which results in an automatic disconnect for the game. 

Q: What are the consequences of a player cheating/how does the anticheat python script handle improper/irregular user behavior
A: Through the invocation of the "perform_quit()" function, the player is disconnected from the sever.

Item Functionality: 

Q: What does the first aid kit do/how does it function within the game? 
A: The first aid kit randomly restorces between 50 to 80 health. This is represented in the aid_kit.py file found in the directory "Vitrix/vitrix/lib/items/aid_kit.py" where the class attribute "health_restore" is initlized to a random value between 50 and 80 through the "random.randint(50, 80)" function which is derriven from the random library in python. 

User Interface: 

Q: Where are U.I. related scripts located? 
A: Within the directory "Vitrix/vitrix/lib/UI/"

<br>
<h4>You can find out everything you else you need to know in the <a href="https://github.com/ShadityZ/Vitrix/blob/docs-development/docs/mainpage.md">Official Vitrix Documentation</a>!</h4>

