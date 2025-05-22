# 📚 Book Author Manager

Application web Django pour gérer une bibliothèque de livres et d’auteurs, avec une interface utilisateur responsive grâce à Bootstrap.

## ✨ Fonctionnalités

- Affichage de la liste des livres avec image de couverture, auteur et genre
- Détail d’un livre
- Liste et détail des auteurs
- Modèles Django (livre, auteur, genre…)
- Interface claire avec Bootstrap 

## 🛠️ Technologies utilisées

- Python 3.10.1
- Django 5.2.1
- Bootstrap 
- HTML/CSS (template Django)
- SQLite

## 🚀 Installation (en local)

```bash
# Clone du repo
git clone https://github.com/hugo59400/book-author-manager.git
cd book-author-manager

# Création de l'environnement virtuel
python -m venv env
env\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
