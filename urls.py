import settings
import os

from django.conf.urls.defaults import *
from django.contrib import admin

from elsewhere.functions import fill_db

admin.autodiscover()

urlpatterns = patterns('elsewhere.views',
    (r'^$', 'example'),
)

if settings.DEBUG:

    CUR_DIR = os.path.dirname(__file__)
    IMG_PATH = 'img/'
    IMG_DIR = os.path.join(CUR_DIR, "img")

    urlpatterns += patterns('django.views',
        url(r'^%s(?P<path>.*)' % IMG_PATH, 'static.serve', {'document_root': IMG_DIR}, name='elsewhere_img')
    )

# fill the database if it hasn't been filled already
fill_db()