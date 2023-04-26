# This is a Timor-Leste Geodata

Follow instruction below to start using **timor_geodata** on you django project

### First Method 
On you Django project directory, run git submodule command below to add this repo to your Django project as gitsubmodule:

```
git submodule add git@github.com:marobo/timor_geodata.git
```

To include the app in your project, we need to add a reference to its configuration class in the **INSTALLED_APPS** setting. 

The **TimorGeodataConfig** class is in the `timor_geodata/apps.py` file, so its dotted path is **timor_geodata.apps.TimorGeodataConfig**. 

Edit the `mysite/settings.py` file and add that dotted path to the **INSTALLED_APPS** setting. It’ll look like this:


```
INSTALLED_APPS = [
    'timor_geodata',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
]
```

After this configuration, Now Django knows to include the `timor_geodata` an a app. 

Let’s run another command to apply the migrations from that app:

```
./manage.py migrate
```

### Second Method 
Otherwise we can just clone this repo into our Django project and run this as an app

Run git command below to clone this repo into your existing Djangoproject:

```
git clone git@github.com:marobo/timor_geodata.git
```

cd into `timor_geodata` directory and then delete git from this repo. 
This is to prevent to not run multiple git repo in our project.

```
cd timor_geodata
rm -rf .git
```

Add this `timor_geodata` app into your installation app on your Django project `settings.py` as instruction in number 1.
and then run `./manage.py migrate`

### Import Timor Geodata from Shapefiles
Run command below to import Timor Geodata into your database

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
./manage.py import_suco_shapefiles
```

Import Aldeias
```
./manage.py import_aldeia_shapefiles
```

### Test
Runserver and then check
```
./manage.py runserver
```

Visit the site and see the geodata display in admin

[http://127.0.0.1:8000/admin/timor_geodata/
](http://127.0.0.1:8000/admin/timor_geodata)

