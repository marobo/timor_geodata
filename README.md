# This is a Timor-Leste Geodata
## Get started
Follow instruction below to start using **timor_geodata** on you django project
### 1. Use this as git submodule on your project

On you local project directory, run git submodule command below to add this repo on your project as gitsubmodule:

```
git submodule add git@github.com:marobo/timor_geodata.git
```

Add the `timor_geodata` app onto installation app on your `settings.py`

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    ......
    'timor_geodata',
    ......
]
```

After configuration on settings, run `./manage.py migrate` to apply migrations

```
./manage.py migrate
```

### 2. Otherwise you can just clone this repo onto your project and run this as an app

run git command below to clone this repo onto your project:

```
git clone git@github.com:marobo/timor_geodata.git
```

cd into `timor_geodata` folder and then delete git from this repository. 
After you deleted `.git` folder, this `timor_geodata` folder isn't looks like as git repo anymore.
So that prevent as to not run multiple git repo in our project.

```
cd timor_geodata
rm -rf .git
```
After done this step, add this `timor_geodata` app onto installation app on your `settings.py` as instruction above
and then run `./manage.py migrate`

### 3. Import shapefiles
Run command below to import shapefiles into you database

Import Districts or Municipalities
```
./manage.py import_district_shapefiles
```

Import Sudistricts or Administrative Post
```
./manage.py import_subdistrict_shapefiles
```

Import Sucos
```
./manage.py import_shapefiles
```

Import Aldeias
```
./manage.py import_aldeia_shapefiles
```
