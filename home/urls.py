from django.contrib import admin
from django.urls import path, include
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name="home"),
    path('index',views.index,name="index"),
    path('gallery',views.gallery,name="gallery"),
    path('package/<str:package>/', views.order, name="order.package"),
    path("contact", views.contact, name="contact"),
    path("success", views.success, name="success"),
    path("failed", views.failed, name="failed"),
    path("maingallery", views.maingallery, name="maingallery"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)