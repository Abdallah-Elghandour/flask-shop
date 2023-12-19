from src.resources.base_resource import BaseResource
from src.services.insert_product_service import InsertProductService



class InsertProductResource(BaseResource):
    def __init__(self):
        super().__init__()
        self._insert_product_service = InsertProductService()

    def post(self):
        return self._insert_product_service.insert_product()