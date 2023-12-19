
from Database.schema import product_collection
from Database.amazonS3 import s3
from flask import request



class InsertProductService:
    def __init__(self):
            pass

    def insert_product(self):
        product_data = request.get_json()
        image_name = product_data['image'].split("\\")[-1]
        s3.upload_file(product_data['image'], 'productsimagesaws', image_name)
        product_data['image'] = f"https://productsimagesaws.s3.amazonaws.com/{image_name}"
        result = product_collection.insert_one(product_data)
        return {'inserted_id': str(result.inserted_id)}, 200