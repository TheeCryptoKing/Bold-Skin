from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, UniqueConstraint, ForeignKey
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates
from flask_login import UserMixin
from config import db, bcrypt, ma
import datetime
import uuid


class Users(db.Model, SerializerMixin): 
    pass

class Shop(db.Model, SerializerMixin):
    pass

class Products(db.Model, SerializerMixin):
    pass

class Order(db.Model, SerializerMixin):
    pass

class OrderItems(db.Model, SerializerMixin):
    pass

class OrderStatus(db.Model, SerializerMixin):
    pass

class Cart(db.Model, SerializerMixin):
    pass

class CartItems(db.Model, SerializerMixin):
    pass

#################### Advanced ####################
class Payments(db.Model, SerializerMixin):
    pass

class Reviews(db.Model, SerializerMixin):
    pass

class Comments(db.Model, SerializerMixin):
    pass

class Addresses(db.Model, SerializerMixin):
    pass