# LLM local minimaliste avec Ollama
Ce petit projet vise à mettre en place un agent conversationnel localement dans une machine virtuelle.<br>
Il peut être implémenté en suivant les grandes lignes de ce README ou mieux encore en utilisant (et modifiant si nécessaire) les fichiers fournis (Vagrantfile et le script de provisionement) mais pour celà il faut avoir Vagrant installé sur la machine hôte.

## Pré-requis :
- Machine hôte avec minimum 16 Go de RAM.
- Hypervisseur de type 2 installé sur la machine hôte.
- Créer une VM avec au moins 8 Go (8192 Mo) de RAM.
- Installer Ubuntu dans la VM (nous avons choisi la version 22.04)

- ### Mise à jour système
    - **Option a** ```apt update && apt upgrade -y```
        - Attention vous aurez une proposition de mise à jour du noyeau recommandée (mais non obligatoire).
    - **Option b** ```apt update```
        - Celà met à jour l'historique des pacquets mais n'upgrade pas les packets. Vous pourrez le faire par la suite. 

- ### Installation de curl
    - ```apt install -y curl```

- ### Installation du LLM Ollama 
    - ```curl -fsSL https://ollama.com/install.sh | sh```

- ### Redémarrage du service LLM
    - ```systemctl restart ollama```

## Lancer Ollama
- Se connecter à la VM en SSH : ```ssh utilisateur@vm```
- Lancer le modèle : ```ollama run llama3```

## Pour Vagrant
Pour ceux d'entre vous utilisant un hypervisseur de type 2 (VMWare Fusion, Virtualbox, UTM ou autre) couplé à **Vagrant** il y a dans ce repo un Vagrantfile et un fichier de provisionnement.
- ### Installation et utilisation du LLM avec Vagrant
    - Création de la VM : 
        - ```vagrant up --provider=Votre_Hypervisseur```
    - Connexion à la VM :
        - ```vagrant ssh llm```
    - Lancement du modèle (ATTENTION ! le premier lancement prends du temps): 
        - ```ollama run llama3```

