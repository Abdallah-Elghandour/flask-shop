from Database.DB import db

product_schema = {
    'validator': {
        '$jsonSchema': {
            'bsonType': 'object',
            'required': ['name', 'price', 'quantity', 'description', 'image'],
            'properties': {
                'name': {
                    'bsonType': 'string',
                    'description': 'must be a string and is required'
                },
                'price': {
                    'bsonType': 'double',
                    'minimum': 0,
                    'description': 'must be a decimal number greater than or equal to 0'
                },
                'quantity': {
                    'bsonType': 'int',
                    'minimum': 0,
                    'description': 'must be an integer greater than or equal to 0'
                },
                'description': {
                    'bsonType': 'string',
                    'description': 'must be a string'
                },
                'image': {
                    'bsonType': 'string',
                    'description': 'must be a string'
                }
            }
        }
    }
}
if 'products' not in db.list_collection_names():
    product_collection = db.create_collection('products', validator=product_schema['validator'])
else:
    product_collection = db["products"]
