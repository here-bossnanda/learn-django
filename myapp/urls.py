from django.conf.urls import url
from myapp import views

urlpatterns = [
  url(r'^api/foods$', views.food_list),
  url(r'^api/foods/(?P<pk>[0-9]+)$', views.food_detail)
]
