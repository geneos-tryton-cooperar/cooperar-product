from trytond.pool import PoolMeta
from trytond.model import ModelView, ModelSQL, fields

__all__ = ['Template']
__metaclass__ = PoolMeta

class Template(ModelSQL, ModelView):
    "Product Template"
    __name__ = "product.template"

    suma_cuotas = fields.Boolean('Suma Cuotas')
 