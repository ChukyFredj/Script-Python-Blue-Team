# Outil d'Analyse de Fichiers

Ce script Python est conçu pour analyser les fichiers dans un répertoire spécifié. Il effectue diverses vérifications, y compris le calcul du checksum du fichier, la détermination du type de fichier, la vérification d'une potentielle encryption et la vérification de la corruption.

## Fonctionnalités

- **Calculer le Checksum du Fichier:** Calcule le checksum SHA-256 du fichier.
- **Calculer l'Entropie:** Détermine l'entropie d'un fichier pour vérifier une potentielle encryption.
- **Déterminer le Type de Fichier:** Identifie le type de fichier en utilisant la bibliothèque `python-magic`.
- **Vérifier la Corruption du Fichier:** Vérifie si un fichier est corrompu en essayant de le lire.
- **Traiter les Fichiers:** Traite et affiche les informations de chaque fichier dans un répertoire spécifié.

## Prérequis

- Python 3.x
- Bibliothèque `python-magic`

Vous pouvez installer la bibliothèque requise en utilisant pip :
```sh
pip install python-magic
```

## Utilisation

1. **Importer les bibliothèques nécessaires :**
    ```python
    import os
    import hashlib
    import magic
    import math
    from typing import Optional
    ```

2. **Définir les fonctions :**
    - `calculate_file_checksum(filename: str, block_size: int = 65536) -> str`
    - `calculate_entropy(data: bytes) -> float`
    - `check_encryption(file_path: str, threshold: float = 0.9) -> bool`
    - `get_file_type(path: str) -> str`
    - `check_file_corruption(path: str) -> bool`
    - `process_file(path: str) -> Optional[dict]`

3. **Lister les fichiers et traiter chaque fichier dans un répertoire :**
    ```python
    def list_files(directory: str) -> None:
        for root, _, files in os.walk(directory):
            for file in files:
                file_info = process_file(os.path.join(root, file))
                if file_info:
                    print(f"Fichier: {file_info['path']}")
                    print(f"Taille: {file_info['size']} octets")
                    print(f"SHA256: {file_info['checksum']}")
                    print(f"Type: {file_info['type']}")
                    print(f"Potentiellement Encrypté: {'Oui' si file_info['potentially_encrypted'] else 'Non'}")
                    print(f"Corrompu: {'Oui' si file_info['corrupted'] else 'Non'}")
                    print("---")
    ```

4. **Exécuter le script :**
    ```python
    if __name__ == "__main__":
        list_files('/path/to/directory')
    ```

## Exemple

Pour analyser tous les fichiers dans le répertoire `/home/user/documents`, exécutez le script avec la commande suivante :

```sh
python file_analysis.py
```

Remplacez `/path/to/directory` par le chemin réel vers le répertoire que vous souhaitez analyser.

## Fonctions

### `calculate_file_checksum`
Calcule le checksum SHA-256 d'un fichier donné.

### `calculate_entropy`
Calcule l'entropie des données d'un fichier pour déterminer une potentielle encryption.

### `check_encryption`
Vérifie si un fichier est potentiellement encrypté en comparant son entropie à un seuil.

### `get_file_type`
Utilise `python-magic` pour déterminer le type d'un fichier donné.

### `check_file_corruption`
Vérifie si un fichier est corrompu en essayant de le lire.

### `process_file`
Traite un fichier pour recueillir et retourner ses métadonnées.

### `list_files`
Liste et traite tous les fichiers dans 
