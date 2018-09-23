from django.contrib import admin

from .models import Pick, User

#@admin.register(Pick)
class PickAdmin(admin.ModelAdmin):
     list_display = ['name','pick1','pick2','pick3','pick4','pick5','pick6','pick7','pick8','pick9','pick10','pick11','pick12','pick13','pick14','pick15','pick16','totalPtsMonday'] 
  
     def __str__(self):
         return 'User: ' + self.name

admin.site.register(Pick)
admin.site.register(User)