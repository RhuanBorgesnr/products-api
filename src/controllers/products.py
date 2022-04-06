
from flask import Flask
from flask_restx import Api, Resource
from src.server.instance import server



app, api  = server.app, server.api

products_db = [
    {'id': 0, 'name': 'Fruit Bowl Açai', 'price': 15.99 },
    {'id': 1, 'name': 'Fruit Bowl Morango com Banana', 'price': 16.99},
    {'id': 2, 'name': 'Fruit Bowl Manga com Maracuja', 'price': 13.99},
    {'id': 3, 'name': 'Sanduiche Frango Grelhado', 'price': 14.99},
    {'id': 4, 'name': 'Sanduiche Salpicão', 'price': 11.99},
    {'id': 5, 'name': 'Sanduiche Pernil Suino', 'price': 15.49},
    {'id': 6, 'name': 'Sanduiche Rangu de Carne', 'price': 16.99}
    
]

@api.route('/products')
class ProductsList(Resource):
    def get(self, ):
        return products_db

    def post(self, ):
        response = api.payload
        products_db.append(response)
        return response, 200
        
        