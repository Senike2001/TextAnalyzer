# Documentation du Projet

## 1. Répertoire `text_analyzer/`
Ce répertoire contient le code source principal de l'application.

- **`__init__.py`** :  
  - Un fichier vide qui indique à Python que ce répertoire est un package.  
  - Permet d'importer les modules contenus dans le répertoire (`analyzer.py`).

- **`analyzer.py`** :  
  - Contient le script principal de l'application.  
  - Définit la fonction `analyze_text()` qui :  
    - Compte les mots et les caractères dans un texte donné.  
    - Identifie les "mots clés" de plus de 5 caractères.  
  - Ce fichier peut être exécuté directement pour tester le programme (`__main__`).

---

## 2. Répertoire `text_analyzer/tests/`
Ce répertoire contient les tests unitaires pour le projet.

- **`__init__.py`** :  
  - Indique à Python que ce répertoire est un package.  
  - Nécessaire pour découvrir les tests avec l’outil `unittest`.

- **`test_analyzer.py`** :  
  - Contient les tests unitaires pour le fichier `analyzer.py`.  
  - Utilise le module Python `unittest`.  
  - Vérifie que la fonction `analyze_text()` retourne les résultats attendus.  
  - Ces tests permettent de s’assurer que les modifications dans le code n'introduisent pas de régressions.

---

## 3. Fichier `requirements.txt`
- **Rôle** : Liste les dépendances nécessaires au projet.  
- **Contenu** :  
  - `flake8` pour le linting (analyse de la qualité du code).  
  - `unittest` pour l'exécution des tests.

### Utilisation :
```bash
pip install -r requirements.txt
