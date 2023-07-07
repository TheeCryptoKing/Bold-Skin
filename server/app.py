#!/usr/bin/env python3
from flask_migrate import Migrate
from flask_restful import Resource
from flask import (
    Flask, 
    request, 
    session, 
    make_response, 
    jsonify, 
    redirect, 
    url_for,
    abort,
    flash,
    Blueprint
    )
from flask_login import (
    LoginManager, 
    login_user, 
    logout_user, 
    login_required, 
    current_user,
    login_fresh,
    )
from flask_bcrypt import generate_password_hash
# from flask_jwt_extended import (
#     create_access_token,
#     get_jwt,
#     get_jwt_identity,
#     unset_jwt_cookies,
#     jwt_required,
# )
from config import app, db, api, Resource
from models import (
    db, 
    User, 
    Payment, 
    Address, 
    Product, 
    Category, 
    Review, 
    Comment, 
    Role, 
    Cart, 
    CartItem, 
    Order, 
    OrderItems, 
    OrderStatus
    )
# import ipdb
import datetime
from datetime import timezone, timedelta, datetime
import traceback

migrate = Migrate(app, db)
login_manager = LoginManager()
login_manager.init_app(app)

