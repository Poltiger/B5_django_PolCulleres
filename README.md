# Blog M3-UF6 - Django

Projecte de blog desenvolupat amb Django com a part del mòdul M485 Programació, Bloc 6 (POO i persistència en BD).

## Introducció

Aplicació web de blog que permet visualitzar posts, autors i etiquetes. Inclou les seccions:
- Pàgina principal amb els 3 darrers posts
- Llistat complet de posts
- Detall de cada post amb etiquetes
- Llistat d'autors i detall de cada autor
- Llistat d'etiquetes i posts per etiqueta

## Instal·lació ràpida

```bash
# 1. Clona el repositori
git clone <URL_DEL_REPOSITORI>
cd <NOM_DEL_REPO>

# 2. Crea i activa un entorn virtual
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux/Mac

# 3. Instal·la les dependències
pip install -r requirements.txt

# 4. Executa les migracions
python manage.py migrate

# 5. Carrega les dades inicials
python manage.py loaddata blog/fixtures/initial_data.json
```

## Execució del projecte

```bash
python manage.py runserver
```

Accedeix a: [http://127.0.0.1:8000](http://127.0.0.1:8000)

Panel d'administració: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

## Documentació (Pydoc)

Documentació generada automàticament amb Pydoc via GitHub Actions:

📄 [Veure documentació](https://poltiger.github.io/B5_django_PolCulleres/)

| Mòdul | Descripció |
|-------|-----------|
| [blog.models](https://poltiger.github.io/B5_django_PolCulleres/blog.models.html) | Models de la base de dades (Post, Author, Tag) |
| [blog.views](https://poltiger.github.io/B5_django_PolCulleres/blog.views.html) | Vistes de l'aplicació |
| [blog.urls](https://poltiger.github.io/B5_django_PolCulleres/blog.urls.html) | Configuració de les URLs |
| [blog.admin](https://poltiger.github.io/B5_django_PolCulleres/blog.admin.html) | Configuració del panell d'administració |
