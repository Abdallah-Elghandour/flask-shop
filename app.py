from flask import Flask
from flask_restful import Api
from flask_marshmallow import Marshmallow
from src.routes import insert_product_route, delete_product_route
from src.routes import update_product_route
app = Flask(__name__)
ma = Marshmallow(app)
api = Api(app)

insert_product_route(api)
delete_product_route(api)
update_product_route(api)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=4000, debug=True)
