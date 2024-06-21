from django.contrib import admin
from blog.models import Noticias

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('title' , 'text','name_user', 'pub_date')
    search_fields = ('title',) #para fazer a pesquisa por titulos 

admin.site.register(Noticias, NoticiaAdmin)