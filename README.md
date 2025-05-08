# Alexa Dialog to Web Service

⚠️ **AVERTISSEMENT** ⚠️
Ce code a été généré automatiquement et n'a pas été testé en production. Il est fourni "tel quel" sans garantie de fonctionnement. Il est fortement recommandé de :
- Tester le code dans un environnement de développement avant de le déployer
- Vérifier la sécurité des endpoints et des configurations
- Adapter le code selon vos besoins spécifiques
- Effectuer des tests approfondis avant toute utilisation en production

Ce projet contient une fonction Lambda Alexa qui capture le dialogue de l'utilisateur et le transmet à un endpoint web. La réponse de l'endpoint est ensuite retournée à l'utilisateur.

## Prérequis

- Python 3.8 ou supérieur
- Un compte Amazon Developer
- Un compte AWS
- Un endpoint web fonctionnel

## Installation

1. Clonez ce dépôt
2. Installez les dépendances :
```bash
pip install -r requirements.txt
```

3. Créez un fichier `.env` à la racine du projet avec les variables suivantes :
```
WEB_ENDPOINT=votre_url_endpoint
```

## Configuration Alexa

1. Créez une nouvelle compétence Alexa dans le [Alexa Developer Console](https://developer.amazon.com/alexa)
2. Configurez l'intention `DialogIntent` avec le slot suivant :
   - Nom du slot : `dialog`
   - Type : `AMAZON.SearchQuery`
3. Configurez la Lambda dans AWS :
   - Créez une nouvelle fonction Lambda
   - Copiez le contenu de `lambda_function.py`
   - Configurez le runtime Python 3.8
   - Ajoutez les variables d'environnement nécessaires
4. Liez la Lambda à votre skill Alexa

## Fichiers de Configuration Alexa

Le projet contient deux fichiers de configuration principaux pour la skill Alexa :

### 1. interaction-model.json
Ce fichier définit le modèle d'interaction de la skill :
- Le nom d'invocation ("mon assistant")
- L'intention `DialogIntent` avec son slot `dialog`
- Les exemples d'énoncés pour l'intention
- Les intentions système (Help, Cancel, Stop)

### 2. skill-package/skill.json
Ce fichier contient le manifeste de la skill :
- Les métadonnées de la skill (nom, description, etc.)
- La configuration de l'endpoint Lambda
- Les informations de publication

Pour utiliser ces fichiers :
1. Dans l'Alexa Developer Console, allez dans "Build"
2. Pour le modèle d'interaction :
   - Cliquez sur "JSON Editor"
   - Copiez le contenu de `interaction-model.json`
3. Pour le manifeste :
   - Allez dans "Skill Information"
   - Mettez à jour les informations selon votre configuration
   - Remplacez `REGION`, `ACCOUNT_ID` et `FUNCTION_NAME` dans l'URI de l'endpoint

## Structure du projet

- `lambda_function.py` : Code principal de la fonction Lambda
- `requirements.txt` : Dépendances Python
- `.env` : Variables d'environnement (à créer)
- `interaction-model.json` : Modèle d'interaction Alexa
- `skill-package/skill.json` : Manifeste de la skill

## Format des requêtes/réponses

### Requête vers l'endpoint web
```json
{
    "dialog": "texte de l'utilisateur"
}
```

### Réponse attendue de l'endpoint
```json
{
    "response": "réponse à retourner à l'utilisateur"
}
```

## Déploiement

1. Créez un fichier ZIP contenant :
   - `lambda_function.py`
   - Tous les fichiers du dossier `site-packages` après installation des dépendances
2. Téléchargez le ZIP dans votre fonction Lambda AWS
3. Configurez les variables d'environnement dans la console AWS 