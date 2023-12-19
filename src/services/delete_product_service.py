from Database.schema import product_collection
from flask import request


class DeleteProductService:
    def __init__(self):
        pass

    def delete_product(self):
        product_data = request.get_json()
        result = product_collection.delete_one(product_data)
        return {'deleted_count': str(result.deleted_count)}, 200