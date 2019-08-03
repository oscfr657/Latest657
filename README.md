
# Latest 657 #

A small promo app with VueJs frontend and
Django backend.

## Installation ###
  
### Pip requirements ###

> pip install -r requirements.txt

### Django settings ###

Add to your settings file.

``` Python
SITE_ID = 1
```

add to INSTALLED_APPS

``` Python
    'django.contrib.sites',

    'rest_framework',

    'latest657',
```

Add this restframework settings

``` python
  REST_FRAMEWORK {
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer'
    )
  }
```

### Database configuration ###

> python manage.py migrate
  
### Django url ###

To the django projects' url.py add

``` python
from django.conf.urls import include
```

and

``` python
url(r'^latest/', include(('latest657.urls', 'latest657'), namespace='latest657')),
```

## App as component ##

Create the div

``` html
<div id="latest657" >
  <router-view></router-view>
</div>
```

 where you whant the promo to apear and preferbly put

``` html
<script src="{% static 'js/latest657/dist/build.js' %}"></script>
```

at the bottom of your index.html

## For development ##

> pip install pylint

To the Django settings.py add

``` python
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

To the Django project url.py add

``` python
from django.conf.urls.static import static
```

After the url patterns add, inclding the plus sign in the begining

``` python
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### VueJS app building ###

 > sudo apt-get install npm
  
 In the vue_app directory run:

> npm install

and

> npm run build
