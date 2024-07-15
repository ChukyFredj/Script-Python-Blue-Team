# Outil de Surveillance Réseau

Ce script Python est conçu pour surveiller et analyser le trafic réseau sur une interface spécifiée. Il collecte des informations sur les paquets, les connexions, et les statistiques de transfert de données.

## Fonctionnalités

- **Surveillance du Réseau:** Capture les paquets sur une interface réseau spécifiée.
- **Statistiques de Trafic:** Calcule et affiche les statistiques de trafic réseau, y compris le nombre total de paquets et les connexions principales.
- **Informations sur les Connexions:** Affiche les cinq connexions les plus fréquentes.
- **Statistiques d'E/S:** Affiche les statistiques de transfert de données (octets envoyés et reçus).

## Prérequis

- Python 3.x
- Bibliothèque `psutil`
- Bibliothèque `scapy`

Vous pouvez installer les bibliothèques requises en utilisant pip :
```sh
pip install psutil scapy
```

## Utilisation

### Arguments de Ligne de Commande

- `-i` ou `--interface` : Spécifie l'interface réseau à surveiller (obligatoire).
- `-d` ou `--duration` : Spécifie la durée de la surveillance en secondes (optionnel, par défaut : 60 secondes).

### Exemple d'Exécution

Pour exécuter le script et surveiller l'interface `eth0` pendant 60 secondes, utilisez la commande suivante :

```sh
python network_monitor.py -i eth0 -d 60
```

### Liste des Interfaces Réseau

Si l'interface spécifiée n'est pas trouvée, le script affichera la liste des interfaces réseau disponibles.


## Avertissements

- Assurez-vous d'avoir les permissions nécessaires pour surveiller l'interface réseau spécifiée.
- L'utilisation de ce script peut nécessiter des privilèges d'administrateur/root, selon votre système d'exploitation et votre configuration réseau.
