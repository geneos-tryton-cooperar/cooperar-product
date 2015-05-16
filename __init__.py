from trytond.pool import Pool
from .product import Template

def register():
    Pool.register(
        Template,
        module='cooperar-product', type_='model')
