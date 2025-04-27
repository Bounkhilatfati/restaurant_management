# 🍽️ Restaurant Management System - Django Project

Une application web complète pour gérer les plats, les catégories et les commandes dans un restaurant.  
Projet réalisé dans le cadre de l'évaluation du semestre.

---

## 🌟 Fonctionnalités

### 🔧 Pour l'Administrateur
- Gérer les **Catégories** (CRUD)
- Gérer les **Plats** (CRUD)
- Gérer les **Commandes** (CRUD)
- Visualiser le **coût total** d'une commande
- Interface **responsive** et moderne avec Bootstrap

### 👨‍🍳 Pour le Staff
- Visualiser tous les plats par catégorie
- Créer une nouvelle commande avec plusieurs plats et quantités

---

## 🚀 Technologies Utilisées

- **Backend** : Django 5
- **Frontend** : Bootstrap 5, HTML/CSS
- **Base de données** : SQLite
- **Gestion des images** : Django Media (ImageField)

---

## 📋 Prérequis

- Python 3.10+
- Pip
- Git (pour cloner le repo)

---

## 🛠️ Installation

1. **Cloner le dépôt**
```bash
git clone https://github.com/ton-username/restaurant-django.git
cd restaurant-django
```
2.Créer un environnement virtuel et installer les dépendances
   ```bash
   python -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   ```

3. Appliquer les migrations et lancer le serveur
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

4. Accédez à l'application à l'adresse [http://localhost:8000](http://localhost:8000)


## 📊 Modèles de la Base de Données

Le système utilise Django avec les modèles suivants:

- **Category**: Représente une catégorie de plats (exemple : Entrées, Plats principaux, Desserts)
- **Dish**: Représente un plat individuel, avec son nom, sa description, son prix et sa catégorie associée
- **Order** : Représente une commande effectuée par un client, contenant plusieurs plats
- **OrderItem** : Représente l'association entre un plat et une commande avec la quantité demandée

## 📱 Responsive Design

L'application est entièrement responsive et s'adapte à tous les appareils:
- Ordinateurs de bureau
- Tablettes
- Smartphones

## 🙏 Remerciements

- Tous les contributeurs au projet
- L'université pour son soutient

