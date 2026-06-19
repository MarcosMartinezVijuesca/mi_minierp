from django.contrib import admin
from .models import Cliente, Producto, EstadoPedido


@admin.register(Cliente) #Registra el modelo Cliente en el panel de admin
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nif', 'nombre', 'email', 'telefono') #Columnas que se veran en la tabla del admin
    search_fields = ('nif', 'nombre', 'email') #Campos sobre los que se puede buscar


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin): #Registra el modelo Producto en el panel de admin
    list_display = ('id', 'sku', 'nombre', 'precio')
    search_fields = ('sku', 'nombre')


@admin.register(EstadoPedido) #Registra el modelo Estado para pedidos
class EstadoPedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)