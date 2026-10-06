# Video Tracker

## Description
Ce dépôt contient un projet universitaire dédié au suivi et à l'analyse d'éléments dans des flux vidéo (Video Tracking). Développé en Python, le logiciel permet d'importer des vidéos, d'y suivre des points d'intérêt et de générer des graphiques d'analyse à partir des données récoltées. 

L'application a été conçue en respectant strictement l'architecture logicielle Modèle-Vue-Contrôleur (MVC) afin de séparer la logique métier, l'interface utilisateur et le traitement des données.

## Architecture du projet

Le code source est organisé de la manière suivante :

- `VideoTracker/src/` : Contient le code source principal de l'application.
  - `Application.py` : Point d'entrée principal du programme.
  - `models/` : Contient la logique métier et les structures de données (`Video.py`, `Graph.py`, `point.py`, `fileRepo.py`).
  - `views/` : Contient les éléments relatifs à l'interface utilisateur (`view.py`).
  - `controllers/` : Fait le lien entre les modèles et les vues (`Controller.py`).
- `VideoTracker/resources/` : Dossier contenant les ressources multimédias de test (images et vidéos, ex: `compteur.mp4`).
- `VideoTracker/tests/` : Scripts de tests unitaires garantissant la fiabilité du code (ex: `test_FileRepo.py`) et fichiers de données d'exemple (`CSVtest.csv`).
- `.gitlab-ci.yml` : Configuration d'intégration continue historique du projet.

## Prérequis

Pour exécuter ce projet, vous devez disposer de :
- Python 3.7 ou version ultérieure (selon les spécifications du cache d'exécution).
- Les dépendances standards Python requises pour le traitement d'images et l'interface graphique (à installer via votre environnement virtuel).

## Installation et exécution

1. Clonez ce dépôt sur votre machine locale :
   ```bash
   git clone <url-de-votre-depot>
   ```

2. Naviguez vers le répertoire source :
   ```bash
   cd videotracker_gb1-main/VideoTracker/src/
   ```

3. Exécutez l'application :
   ```bash
   python Application.py
   ```

## Contexte
Ce projet a été initialement réalisé dans le cadre de mon cursus universitaire. Il a été migré sur ce compte GitHub pour servir d'archive et de portfolio démontrant mes compétences en développement logiciel orienté objet sous Python.