from django.db import models #orm de Django para crear modelos/tablas


class Cliente(models.Model):
    """
    Modelo maestro que representa a los clientes de la empresa.
    El campo nif representa el identificador fiscal del cliente,
    que puede ser un NIF si es una persona física o un CIF si es una empresa.
    En ambos casos es único.
    """
    nif = models.CharField(max_length=20, unique=True) # Identificador fiscal único, no pueden existir dos clientes con el mismo NIF/CIF
    nombre = models.CharField(max_length=150) # Nombre del cliente o razón social de la empresa
    email = models.EmailField(blank=True) # Email opcional, Django valida el formato automáticamente
    telefono = models.CharField(max_length=20, blank=True) # Teléfono opcional

    def __str__(self):
        # Representación textual del cliente en el panel admin
        return f"{self.nombre} ({self.nif})"

    class Meta:
        # Define cómo se muestra el modelo en el panel admin
        verbose_name = "Cliente"          # Nombre singular
        verbose_name_plural = "Clientes"  # Nombre plural


class Producto(models.Model):
    """
    Modelo maestro que representa los productos del catálogo.
    Existe de forma independiente aunque nadie lo haya pedido.
    """
    sku = models.CharField(max_length=50, unique=True) # Código único del producto, no pueden existir dos productos con el mismo SKU
    nombre = models.CharField(max_length=150) # Nombre descriptivo del producto
    precio = models.DecimalField(max_digits=10, decimal_places=2) # Precio con hasta 10 dígitos y 2 decimales

    def __str__(self):
        # Representación textual del producto en el panel admin
        return f"{self.nombre} ({self.sku})"

    class Meta:
        # Define cómo se muestra el modelo en el panel admin
        verbose_name = "Producto"          # Nombre singular
        verbose_name_plural = "Productos"  # Nombre plural


class EstadoPedido(models.Model):
    """
    Modelo maestro que representa los posibles estados de un pedido.
    Actúa como tabla de referencia con valores fijos.
    """
    ESTADOS = [
        ('BORRADOR', 'Borrador'),       # Pedido en preparación
        ('CONFIRMADO', 'Confirmado'),   # Pedido aceptado por el cliente
        ('FACTURADO', 'Facturado'),     # Factura emitida al cliente
        ('COBRADO', 'Cobrado'),         # Pago recibido
    ]
    nombre = models.CharField(max_length=20, choices=ESTADOS, unique=True) # Solo acepta los 4 valores definidos en ESTADOS

    def __str__(self):
        # Muestra el nombre legible del estado en lugar del código interno
        return self.get_nombre_display()

    class Meta:
        # Define cómo se muestra el modelo en el panel admin
        verbose_name = "Estado de Pedido"          # Nombre singular
        verbose_name_plural = "Estados de Pedido"  # Nombre plural