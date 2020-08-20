from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('predictdrawing', views.predictDrawing, name = "predictDrawing"),
    #url(r'^ads/', include('ads.urls'))
]