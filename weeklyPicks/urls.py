from django.urls import path


from . import views

urlpatterns = [
  path(r'^', views.index, name='index'),
  path("<int:pick_id>/", views.pick, name='pick'),
]
