import settings
import os

from django.conf.urls.defaults import *
from django.contrib import admin

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