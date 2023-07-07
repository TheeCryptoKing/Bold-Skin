from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, UniqueConstraint, ForeignKey
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates
from flask_login import UserMixin, LoginManager
# from config import db, bcrypt, ma
import datetime
import uuid
import re
from config import db, bcrypt



class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    ################################## Main Attributes
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    
    ############################# DateTime Specfics
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    ######################## FK
    # role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    
    #################### Relationships 
    # Uorders = db.relationship("Order", backref='user_order')
    # Ucart = db.relationship("Cart", backref='user_cart')
    # Upayment = db.relationship("Payment", backref='user_payment')
    # Ureview = db.relationship("Review", backref='user_reviews')
    # Ucomments = db.relationship("Comment", backref='user_comments')
    # Uaddresses = db.relationship("Address", backref='user_addresses')
    ############ Validation & Seriaization
    # serialize_rules
    # @validations('')


class Product(db.Model, SerializerMixin):
    __tablename__ = 'products'
    ######################## Main Attributes
    id = db.Column(db.Integer, primary_key=True)
    p_name = db.Column(db.String, nullable=False)
    p_description = db.Column(db.String, nullable=False)
    p_price = db.Column(db.Integer, nullable=False)
    p_image = db.Column(db.String, nullable=False)
    p_image_2 = db.Column(db.String, nullable=True)
    p_background = db.Column(db.String, nullable=True)
    ####################### DateTime Specfics
    ####################### FK
    # category_id = db.Column(db.Integer, db.ForeignKey('category.id')) 
    ########################### Relationships 
    # product_order_quantity = db.relationship("Product", backref="product_order_list")
    # cartItems = db.relationship("CartItem", backref='cartProducts')
    # product_reviews = db.relationship("Review", backref="reviewOfProducts")
    ######################## Validation & Serialization
    # serialize_rules
    # @validations('')

class Category(db.Model, SerializerMixin):
    __tablename__ = 'categories'
    ######################## Main Attributes
    id = db.Column(db.Integer, primary_key=True)
    categories = db.Column(db.String)
    ####################### Relationships
    # Backref = automatically adds a new attribute to the target table's model, which provides access to related objects from the source table. 
    # products = db.relationship("Product", backref="product_category")  
    ######################## Validation & Serialization
    # serialize_rules
    # @validations('')

class Order(db.Model, SerializerMixin):
    __tablename__ = 'orders'
    ######################## Main Attributes
    id = db.Column(db.Integer, primary_key=True)
    order_total = db.Column(db.Integer)
    order_status = db.Column(db.String)
    ####################### DateTime Specfics
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    ####################### FK
    # user_id = db.Column(db.Integer, db.ForeignKey(users.id))
    ########################### Relationships
    # order_items_list = db.relationship("OrderItems", backref='orderedItems')
    ######################## Validation & Serialization
    # serialize_rules
    # @validations('')

class OrderItems(db.Model, SerializerMixin):
    __tablename__ = 'order_items'
    ######################## Main Attributes
    id = db.Column(db.Integer, primary_key=True)
    num_of_items = db.Column(db.Integer, nullable=True)
    items_price = db.Column(db.Integer, nullable=True)
    ####################### DateTime Specfics
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    ####################### Relationships
    # order_id = db.Column(db.Integer, db.ForeignKey('orders.id')) 
    # product_id = db.Column(db.Integer, db.ForeignKey('products.id')) 
    ######################## Validation & Serialization
    # serialize_rules
    # @validations('')

class OrderStatus(db.Model, SerializerMixin):
    __tablename__ = 'order_status'
    ######################## Main Attributes
    id = db.Column(db.Integer, primary_key=True)
    current_status = db.Column(db.String, nullable=True)
    ####################### DateTime Specfics
    ####################### Relationships
    ######################## Validation & Serialization
    # serialize_rules
    # @validations('')


class Cart(db.Model, SerializerMixin):
    __tablename__ = 'cartstuff'
    ######################## Main Attributes
    id = db.Column(db.Integer, primary_key=True)
    ####################### DateTime Specfics
    ####################### FK
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    ########################### Relationships
    # cartItems = db.relationship("CartItem", backref='cartQuantity')
    ######################## Validation & Serialization
    # serialize_rules
    # @validations('')


class CartItem(db.Model, SerializerMixin):
    __tablename__ = 'cart_items'
    ######################## Main Attributes
    id = db.Column(db.Integer, primary_key=True)
    cart_quantity = db.Column(db.Integer, nullable=True)
    ####################### DateTime Specfics
    ####################### FK
    # cart_id = = db.Column(db.Integer, db.ForeignKey('cartstuff.id')) 
    # product_id = = db.Column(db.Integer, db.ForeignKey('products.id'))
    ########################### Relationships
    ######################## Validation & Serialization
    # serialize_rules
    # @validations('')



#################### Advanced ####################
class Payment(db.Model, SerializerMixin):
    __tablename__ = 'payments'
    ######################## Main Attributes
    id = db.Column(db.Integer, primary_key=True)
    card_number = db.Column(db.Integer, nullable=True)
    cardholder_name = db.Column(db.String, nullable=True)
    expiration_month = db.Column(db.Integer, nullable=True)
    expiration_year = db.Column(db.Integer, nullable=True)
    cvv = db.Column(db.Integer, nullable=True)
    ####################### DateTime Specfics
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    ####################### Relationships
    # user_id = db.Column(db.ForeignKey, backref='users.id')
    ######################## Validation & Serialization
    # serialize_rules
    # @validations('')

class Review(db.Model, SerializerMixin):
    __tablename__ = 'reviews'
    ######################## Main Attributes
    id = db.Column(db.Integer, primary_key=True)
    review_rating = db.Column(db.String, nullable=False) 
    review_text = db.Column(db.String, nullable=False)
    ####################### DateTime Specfics
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    ####################### FK
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    ####################### Relationships
    # comment = db.relationship("Comment", backref='review_comment')
    ######################## Validation & Serialization
    # serialize_rules
    # @validations('')

class Comment(db.Model, SerializerMixin):
    __tablename__ = 'comments'
    ######################## Main Attributes
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    user_comment = db.Column(db.String, nullable=True)
    ####################### DateTime Specfics
    ####################### Relationships
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id')) 
    # review_id = db.Column(db.Integer, db.ForeignKey('reviews.id')) 
    ######################## Validation & Serialization
    

class Address(db.Model, SerializerMixin):
    __tablename__ = 'addresses'
    ######################## Main Attributes
    id = db.Column(db.Integer, primary_key=True)
    address_1 = db.Column(db.String, nullable=False)
    address_2 = db.Column(db.String, nullable=False)
    address_city = db.Column(db.String, nullable=False)
    address_state = db.Column(db.String, nullable=False)
    address_postal = db.Column(db.Integer, nullable=False)
    addess_type_of = db.Column(db.String, nullable=False)
    ####################### DateTime Specfics
    ####################### Relationships
    # user_id = db.Column(db.ForeignKey, backref='users.id')
    ######################## Validation & Serialization
    # serialize_rules
    # @validations('')

class Role(db.Model, SerializerMixin):
    __tablename__ = 'roles'
    ######################## Main Attributes
    id = db.Column(db.Integer, primary_key=True)
    roles = db.Column(db.String, nullable=True)
    ####################### Relationships
    # users = db.relationship("User", backref="user_roles") 
    ######################## Validation & Serialization
    # serialize_rules
    # @validations('')
    