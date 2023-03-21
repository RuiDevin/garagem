from django.contrib import admin

from .models import Categoria, Marca, Cor, Veiculo

admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Cor)
admin.site.register(Veiculo)

