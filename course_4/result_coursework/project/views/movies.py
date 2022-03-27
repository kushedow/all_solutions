from flask_restx import abort, Namespace, Resource

from project.exceptions import ItemNotFound
from project.services import MoviesService
from project.setup_db import db
from project.tools.security import admin_required

movies_ns = Namespace("movies")


@movies_ns.route("/")
class MoviesView(Resource):
    # @admin_required
    @movies_ns.response(200, "OK")
    def get(self):
        """Get all movies"""
        return MoviesService(db.session).get_all_movies()


@movies_ns.route("/<int:movie_id>")
class MovieView(Resource):
    # @admin_required
    @movies_ns.response(200, "OK")
    @movies_ns.response(404, "Movie не найдено")
    def get(self, movie_id: int):
        """Get movie by id"""
        try:
            return MoviesService(db.session).get_item_by_id(movie_id)
        except ItemNotFound:
            abort(404, message="Movie not found")
