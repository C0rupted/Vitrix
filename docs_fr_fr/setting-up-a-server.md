# Mettre un serveur en place

Les serveurs sont des endroits pour jouer et communiquer avec vos amis. Mettre en place un server est simple.

# Dépendences
Les serveurs Vitrix devraient fonctionner sur n'importe quelle platforme qui supporte Python. Cependant, il est recommendé d'utiliser Linux comme vous pouvez recontrer quelques problèmes avec le pare-feu de Windows 10/11 et la redirection de port, mais sur Linux, toutes ces étapes sont faciles, et comme Python est pré-installé, il n'y a pas de problèmes avec le pare-feu

# Lancer votre serveur
1. Premièrement, soyez sûr que vous avez cloner Vitrix ou téléchargé le .zip. Soyez sûr que le dossier de votre Terminal est celui où vous avez cloné Vitrix.
```
cd /chemin/a/Vitrix
```

2. Then, make sure you have python 3.9.7 installed, as it is the only tested version of python for Vitrix. Then starting the Vitrix server is as easy as running the following command:
Ensuite, soyez sûr d'avoir Python 3.9.7 installé, puisque c'est la seule version testée pour Vitrix. Puis lancez votre serveur Vitrix avec la la commande suivante :
```
python server/server.py
```

# Trouvez l'adresse IP de votre serveur

Et vous avez lancé démarré votre serveur Vitrix ! Sur Linux, vous pouvez vérifier votre adresse IP en utilisant la commande ifconfig. Si vous obtenez une erreur disant,
```
Commande "ifconfig" introuvable.
```
alors éxecutez simplement la commande:
```
apt/dnf/yum install net-tools
```
et réessayez. Sur Windows, vous devez simplement éxecuter ```ipconfig /all``` et trouvez la section: ```Adresse IPv4: ```. Par défaut, le serveur utilisera le port ```26822```, si vous voulez le changer, changez la ligne 19 de ```server.py``` (```PORT = <port>```).
