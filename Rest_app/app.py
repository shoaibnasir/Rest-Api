from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
'''
curl -XGET -H "Content-type: application/json" "http://0.0.0.0:5000/message"
curl -v -XPOST -H "Content-type: application/json" -d '{"property":"11","message":"body"}' "http://0.0.0.0:5000/message"
'''
# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init Marshmallow for Serialization/ Deserialization purposes
marsh = Marshmallow(app)


# Product Class / Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    property = db.Column(db.String(150), unique=False, nullable=True)
    message = db.Column(db.Text)

    def __init__(self, property, message):
        self.property = property
        self.message = message


# Product Schema
class ProductSchema(marsh.Schema):
    class Meta:
        fields = ('id', 'property', 'message')


# Init Schema
product_schema = ProductSchema(strict=True)
products_schema = ProductSchema(many=True, strict=True)


# Routes
# Create a Message entry
@app.route('/message', methods=['POST'])
def add_message():
    property = request.json['property']
    message = request.json['message']

    new_message = Product(property, message)
    db.session.add(new_message)
    db.session.commit()

    return product_schema.jsonify(new_message)


# List all received messages
@app.route('/message', methods=['GET'])
def get_messages():
    all_messages = Product.query.all()
    result = products_schema.dump(all_messages)
    return jsonify(result.data)


@app.route('/message/<id>', methods=['GET'])
def get_message(id):
    msg = Product.query.get(id)
    updated_msg = update_message_body(msg)
    return product_schema.jsonify(updated_msg)


# Update a Message entry
@app.route('/message/<id>', methods=['PUT'])
def update_message(id):
    updated_msg = Product.query.get(id)
    property = request.json['property']
    message = request.json['message']
    updated_msg.name = property
    updated_msg.message = message

    db.session.commit()
    return product_schema.jsonify(updated_msg)


def update_message_body(msg):
    updated_msg = Product.query.get(msg.id)
    property = updated_msg.property
    message = updated_msg.message

    updated_msg.property = add_pal_property(msg)
    updated_msg.message = message

    db.session.commit()
    return updated_msg


# Delete a Specific msg by id
@app.route("/message/<id>", methods=["DELETE"])
def delete_msg(id):
    message = Product.query.get(id)
    db.session.delete(message)
    db.session.commit()
    return product_schema.jsonify(message)


'''Helper Functions'''


def is_palindrome(msg):
    message = msg.message
    if message == reverse(message):
        return True
    return False


def reverse(s):
    return s[::-1]


def add_pal_property(msg):
    palindrome = ''
    if 'Palindrome=' not in msg.property:
        if is_palindrome(msg):
            palindrome = '- Palindrome=True'
        else:
            palindrome = '- Palindrome=False'

    return " ".join([msg.property, palindrome])


# Run app server
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
