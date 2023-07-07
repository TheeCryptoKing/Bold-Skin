########################### imports ######################
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

############################### Models #######################
# flask db revision --autogenerate -m 'message'
# flask db upgrade head 


class User(db.Model, SerializerMixin, UserMixin):
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
    # Urole = dbrelationship("Role", backref="user_role")
    # Uorders = db.relationship("Order", back_populates='user')
    # Ucart = db.relationship("Cart", back_populates='user')
    # Upayments = db.relationship("Payment", back_populates='user')
    # Ureviews = db.relationship("Review", back_populates='user')
    # Ucomments = db.relationship("Comment", back_populates='user')
    # Uaddresses = db.relationship("Address", back_populates='user')
    ############ Validation & Seriaization
    # serialize_rules
    # @validations('')

class Product(db.Model, SerializerMixin):
    __tablename__ = 'products'
    ######################## Main Attributes
    id = db.Column(db.Integer, primary_key=True)
    p_name = db.Column(db.String, nullable=False)
    p_description = db.Column(db.Text, nullable=False)
    p_price = db.Column(db.Integer, nullable=False)
    p_image = db.Column(db.String, nullable=False)
    p_image_2 = db.Column(db.String, nullable=True)
    p_background = db.Column(db.String, nullable=True)
    quantity = db.Column(db.Integer, nullable=False, default=50)
    ingredients = db.Column(db.Text)
    ####################### DateTime Specfics
    ####################### FK
    # category_id = db.Column(db.Integer, db.ForeignKey('category.id')) 
    ########################### Relationships 
    # Backref = automatically adds a new attribute to the target table's model, which provides access to related objects from the source table. 
    # category = db.relationship("Product", backref="product_category")
    # cartItems =  db.relationship("CartItem", back_populates="product")
    # Prod_reviews = db.relationship("Review", back_populates="product")
    # order_items = db.relationship("OrderItem", back_populates="product")
    ######################## Validation & Serialization
    # serialize_rules
    # @validations('')

class Category(db.Model, SerializerMixin):
    __tablename__ = 'categories'
    ######################## Main Attributes
    id = db.Column(db.Integer, primary_key=True)
    categories = db.Column(db.String)
    ####################### Relationships
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
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    ########################### Relationships
    # user = db.relationship("User", back_populates="Uorders")
    # order_items = db.relationship("OrderItems", back_populates="orders")
    # status = db.relationship("Order_Status", backref="orderStatus")
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
    ####################### FK
    # order_id = db.Column(db.Integer, db.ForeignKey('orders.id')) 
    # product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    ####################### Relationships
    # orders = db.relationship("Order", back_populates="order_items")
    # product = db.relationship("Product", back_populates="order_items")
    ######################## Validation & Serialization
    # serialize_rules
    # @validations('')

class OrderStatus(db.Model, SerializerMixin):
    __tablename__ = 'order_status'
    ######################## Main Attributes
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String, nullable=False, unique=True)
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
    # user = db.relationship("User", back_populates='Ucart')
    # cartItems = db.relationship("CartItem", back_populates='cartstuff')
    ######################## Validation & Serialization
    # serialize_rules
    # @validations('')


class CartItem(db.Model, SerializerMixin):
    __tablename__ = 'cart_items'
    ######################## Main Attributes
    id = db.Column(db.Integer, primary_key=True)
    cart_quantity = db.Column(db.Integer)
    ####################### DateTime Specfics
    ####################### FK
    # cart_id = = db.Column(db.Integer, db.ForeignKey('cartstuff.id')) 
    # product_id = = db.Column(db.Integer, db.ForeignKey('products.id'))
    ########################### Relationships
    # cart = db.relationship("Cart", back_populates="cart_items")
    # product = db.relationhship("Product", back_populates="cart_items")
    ######################## Validation & Serialization
    # serialize_rules
    # @validations('')



#################### Advanced ####################
class Payment(db.Model, SerializerMixin):
    __tablename__ = 'payments'
    ######################## Main Attributes
    id = db.Column(db.Integer, primary_key=True)
    card_number = db.Column(db.Integer, nullable=False)
    cardholder_name = db.Column(db.String, nullable=False)
    expiration_month = db.Column(db.Integer, nullable=False)
    expiration_year = db.Column(db.Integer, nullable=False)
    cvv = db.Column(db.Integer, nullable=False)
    ####################### DateTime Specfics
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    ####################### FK
    # user_id = db.Column("User",db.ForeignKey('users.id'))
    ####################### Relationships
    # user = db.relationship("User", back_populates='Upayments')
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
    # user = db.relationship("User", back_populates="Ureviews")
    # product = db.relationship("Product", back_populates="Prod_reviews")
    # comments = db.relationship("Comment", back_populates='review', cascade="delete-orphan-all")
    ######################## Validation & Serialization
    # serialize_rules
    # @validations('')

class Comment(db.Model, SerializerMixin):
    __tablename__ = 'comments'
    ######################## Main Attributes
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    user_comment = db.Column(db.String, nullable=True)
    # likes = db.Column(db.Integer, default=0)
    ####################### DateTime Specfics
    # created_at = db.Column(db.DateTime, server_default=db.func.now())
    # updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    ####################### FK
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id')) 
    # review_id = db.Column(db.Integer, db.ForeignKey('reviews.id')) 
    ####################### Relationships
    # review = db.relationship("Review", back_populates="comments")
    # user = db.relationship("User", back_populates="Ucomments")
    ######################## Validation & Serialization
    

class Address(db.Model, SerializerMixin):
    __tablename__ = 'addresses'
    ######################## Main Attributes
    id = db.Column(db.Integer, primary_key=True)
    address_1 = db.Column(db.String, nullable=False)
    address_2 = db.Column(db.String, nullable=True)
    address_city = db.Column(db.String, nullable=False)
    address_state = db.Column(db.String, nullable=False)
    address_postal = db.Column(db.Integer, nullable=False)
    addess_type_of = db.Column(db.String, nullable=False)
    ####################### DateTime Specfics
    ####################### FK
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id')) 
    ####################### Relationships
    # user = db.relationship("User", back_populates="Uaddresses")
    ######################## Validation & Serialization
    # serialize_rules
    # @validations('')

class Role(db.Model, SerializerMixin):
    __tablename__ = 'roles'
    ######################## Main Attributes
    id = db.Column(db.Integer, primary_key=True)
    roles = db.Column(db.String, nullable=True)
    ####################### Relationships
    # users = db.relationship("User", backref="to_be_Admin") 
    ######################## Validation & Serialization
    # serialize_rules
    # @validations('')
    