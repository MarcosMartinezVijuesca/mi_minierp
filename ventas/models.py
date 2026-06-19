from django.db import models #orm de Django para crear modelos/tablas
from django.db.models import CheckConstraint, Q
from core.models import Cliente, Producto, EstadoPedido
from decimal import Decimal


class Pedido(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.RESTRICT # Impide borrar un cliente que tiene pedidos
    )
    estado = models.ForeignKey(
        EstadoPedido,
        on_delete=models.RESTRICT # Impide borrar un estado que tiene pedidos
    )
    fecha = models.DateField(auto_now_add=True) # Se rellena automáticamente al crear el pedido

    def __str__(self):
        # Representación textual del pedido en el panel admin
        return f"Pedido #{self.id} - {self.cliente}"

    class Meta:
        # Define cómo se muestran los nombres del pedido en el panel admin
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"


class LineaPedido(models.Model):
    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE, #borra las lineas si se borra el pedido
        related_name='lineas'
    )
    producto = models.ForeignKey(
        Producto,
        on_delete=models.RESTRICT #impide borrar productos que ya tienen linea de pedido
    )
    cantidad = models.PositiveIntegerField() # Solo acepta valores positivos (> 0)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, help_text="Precio al momento de la venta")
    #Precio guardado en la linea. Importante porque podría cambiar en el futuro, así mantiene en precio que tenia al momento de la venta
       
    def __str__(self):
        # Representación textual de la línea en el panel admin
        return f"{self.cantidad}x {self.producto} (Pedido #{self.pedido.id})"
    
    @property
    def total_price(self): 
        #Propiedad calculada, no se guarda directamente en la bbdd
        #Multiplica precio por cantidad y redondea a 2 decimales
        return (self.precio_unitario * self.cantidad).quantize(Decimal('0.01'))
    
    class Meta:
        #Define como se muestran los nombres de las lineas de pedido en el panel de admin
        verbose_name = "Línea de Pedido" #Nombre singular
        verbose_name_plural = "Líneas de Pedido" #Nombre plural
        # Crea la regla de que la cantidad debe ser mayor que 0 en la bbdd.
        constraints = [
            CheckConstraint(
                condition=Q(cantidad__gt=0),
                name='cantidad_positiva'
            )
        ]

    
