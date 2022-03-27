from flask import Flask, render_template
from flask_restx import Api

from config import Config
from project.setup_db import db
from project.views import directors_ns
from project.views import users_ns
from project.views import movies_ns
from project.views import genres_ns
from project.views import auth_ns

api = Api(title="Flask Course Project 3", doc="/docs")


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    @app.route('/')
    def index():
        return render_template('index.html')

    db.init_app(app)
    api.init_app(app)

    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(users_ns)
    api.add_namespace(movies_ns)
    api.add_namespace(auth_ns)

    return app


#
# from flask import Flask, Config, render_template
# from flask_cors import CORS
# from flask_restx import Api
#
#
#
# from project.setup_db import db
# from project.views import genres_ns
# from project.views import directors_ns
# from project.views import users_ns
# from project.views import movies_ns
# from project.views import auth_ns
#
# api = Api(
#     authorizations={
#         "Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}
#     },
#     title="Flask Course Project 3",
#     doc="/docs",
# )
#
# # Нужно для работы с фронтендом
# cors = CORS()
#
#
# def create_app(config_obj):
#     app = Flask(__name__)
#     app.config.from_object(config_obj)
#     register_extensions(app)
#
#     @app.route('/')
#     def index():
#         return render_template('index.html')
#     return app
#
# def register_extensions(app):
#     cors.init_app(app)
#     db.init_app(app)
#     api.init_app(app)
#     # Регистрация эндпоинтов
#     api.add_namespace(genres_ns)
#     api.add_namespace(directors_ns)
#     api.add_namespace(users_ns)
#     api.add_namespace(movies_ns)
#     api.add_namespace(auth_ns)
#
#     return app
#
