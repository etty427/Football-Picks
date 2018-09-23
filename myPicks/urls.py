from django.contrib import admin
from django.urls import path


from weeklyPicks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path("<int:pick_id>/", views.pick, name='pick'),
    path("<int:user_id/addPick", views.addPick, name="addpick")
]
