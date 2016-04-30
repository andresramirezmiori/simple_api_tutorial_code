# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include
from rest_framework import routers

from blog.api import PostViewSet, ComentarioViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comentarios', ComentarioViewSet)

urlpatterns = patterns('',
    url(r'^api/v1/', include(router.urls)),
)


