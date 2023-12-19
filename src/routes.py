from src.resources.insert_product_resource import InsertProductResource
from src.resources.delete_product_resource import DeleteProductResource
from src.resources.update_product_resource import UpdateProductResource


def insert_product_route(api):
    api.add_resource(InsertProductResource, '/insert_product', endpoint='insert_product')

def delete_product_route(api):
    api.add_resource(DeleteProductResource, '/delete_product', endpoint='delete_product')

def update_product_route(api):
    api.add_resource(UpdateProductResource, '/update_product', endpoint='update_product')   