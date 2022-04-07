
from tokenize import String
from flask_restx import fields


from src.server.instance import server



product = server.api.model('Products', {
    'id': fields.String(description='O Id do registro.'),
    'name': fields.String(required=True, min_length=1,  max_length=100, description='Nome do produto.'),
    'price': fields.Float(description='O Valor do produto.')  

})

