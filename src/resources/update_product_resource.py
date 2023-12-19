from src.services.update_product_service import UpdateProductService
from src.resources.base_resource import BaseResource

class UpdateProductResource(BaseResource):
    def __init__(self):
        super().__init__()
        self._update_product_service = UpdateProductService()

    def post(self):
        return self._update_product_service.update_product()    