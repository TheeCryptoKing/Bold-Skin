from random import randint, choice as rc
from sqlalchemy import insert, engine
from datetime import datetime
from faker import Faker
from app import app
from models import (
    db,
    User,
    Product,
    Category,
    Order,
    OrderItems,
    OrderStatus,
    Cart,
    CartItem,
    Payment,
    Review,
    Comment,
    Address,
    Role
)
import pickle
import os
import ipdb
import json
import ast
import csv

fake = Faker()

