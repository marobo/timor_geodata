# This is Timor-Leste Geodata for running in Django Project

Follow instruction below to start using **timor_geodata** on your django project

# Notes

Maybe, this is can be only running when your django project is running postgresSQL database

- The latest version of postgresSQL has more tools for geo data, visit this [https://postgresapp.com/documentation/](https://postgresapp.com/documentation/)
  
- GeoDjango requirements - https://docs.djangoproject.com/en/5.0/ref/contrib/gis/install/#homebrew

- Installing PostGIS - https://docs.djangoproject.com/en/5.0/ref/contrib/gis/install/postgis/#creating-a-spatial-database
  

### First Method 
On your Django project directory, run git submodule command below to get this repo in your Django project as gitsubmodule:

```
git submodule add git@github.com:marobo/timor_geodata.git
```

To include the app in your project, we need to add a reference to its configuration class in the **INSTALLED_APPS** section in `setting.py`. 

Edit the `mysite/settings.py` file and add the `timor_geodata` app and `'django.contrib.gis',` to the **INSTALLED_APPS** setting. It’ll look like this:


```
INSTALLED_APPS = [
    'timor_geodata', # New
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis', # New
]
```

The **TimorGeodataConfig** class is in the `timor_geodata/apps.py` file, so its dotted path is **timor_geodata.apps.TimorGeodataConfig**. 

Change the default db engine to postgis
```
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'databasename_db',
    }
}
```

After this configuration, Now Django knows the `timor_geodata` as an app in this project.

Let’s run another command to apply the migrations from that app:

```
./manage.py migrate
```

### Second Method 
Clone this repository into your existing Django project by copy and paste the command below two your terminal and press ENTER:

```
git clone git@github.com:marobo/timor_geodata.git
```

cd into `timor_geodata` directory and then delete git from this repo to prevent runnging multiple git repo in the project.

```
cd timor_geodata
rm -rf .git
```

Add this `timor_geodata` app into your installation app on your Django project `settings.py` as in first instruction methor.

and then run `./manage.py migrate` to apply the migrations from `timor_geodata` app

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

Runserver and check
```
./manage.py runserver
```

Visit the site and see the geodata display in the admin

[http://127.0.0.1:8000/admin/timor_geodata/
](http://127.0.0.1:8000/admin/timor_geodata)

