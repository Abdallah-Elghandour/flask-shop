from Database.schema import product_collection
from flask import request

class UpdateProductService:
    def __init__(self):
        pass

    def update_product(self):
        product_data = request.get_json()
        result = product_collection.update_one({'name': product_data['name']}, {'$set': product_data['update']})
        return {'modified_count': str(result.modified_count)}, 200