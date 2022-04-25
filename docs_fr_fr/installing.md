# Installer Vitrix

**NOTICE:** Vitrix à pour projet de sortir une version par mois. La prochaine version sortira ce mois-ci. 

### Requirements
Vitrix a été testé officielement sur ces plateformes:

![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)


Les plateformes suivantes sont compatibles, mais encore en développement _MAJEUR_:


![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white) 


Et nous travaillons sur la compatibilité pour:

![Mac OS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0) 
![Raspberry Pi](https://img.shields.io/badge/-RaspberryPi-C51A4A?style=for-the-badge&logo=Raspberry-Pi)

##### Conditions matérielles
- Un processeur 64-bit à 1 GHz ou plus (La plupart des processeurs)
- Un minimum de 4 GO de RAM (plûtot commun dans la plupart des ordinateurs)
- Au moins 30 mo d'espace disque

##### Conditions logicielles
- Python 3

### Instructions - Pré-construites
Les versions pré-construites viennent avec Python 3.9 préinstallé, Vous n'avez donc pas besoin d'installer Python pour jouer a Vitrix ! Vous pouvez les trouver sur la page "Releases" https://github.com/ShadityZ/Vitrix/releases

Quand vous aurez trouvé la dernière version, vous remarquerez qu'il y a plusieurs options. Vous pouvez télécharger celle qui a le nom de votre OS dans le nom du fichier. (exemple: ```Vitrix-vx.x.x-[nom de l'OS].zip```) Puis extrayez le fichier .zip et lancer le fichier ```vitrix``` à l'intérieur!
### Instructions - Lancer directement (Git)
1. D'abord, clonez le dépôt en utilisant Git SCM ou télécharger le fichier [zip](https://github.com/ShadityZ/Vitrix/archive/refs/heads/master.zip):
```
git clone https://github.com/ShadityZ/Vitrix
```
2. Quand vous l'aurez téléchargé, extrayez le, ```cd``` dans le dépôt/zip extrait:
```
cd chemin/a/vitrix/
```
4. Installer les dépendances de Vitrix:
```
pip install -r requirements.txt
```
4. Sur linux vous aurez également besoin d'installer quelques packages:
```
sudo apt/dnf/yum install python3-tk python-is-python3
```
5. Bon travail ! Vous pouvez maintenant lancer le script ```menu.py``` dans le dossier ```vitrix``` pour lancer Vitrix Vitrix.
