from src.resources.base_resource import BaseResource
from src.services.delete_product_service import DeleteProductService 

class DeleteProductResource(BaseResource):
    def __init__(self):
        super().__init__()
        self._delete_product_service = DeleteProductService()

    def post(self):
        return self._delete_product_service.delete_product()