from project.config import DevelopmentConfig
from project.dao.models import Genre, User, Director, Movie
from project.server.server import create_app, db

app = create_app(DevelopmentConfig)


@app.shell_context_processor
def shell():
    return {
        "db": db,
        "Genre": Genre,
        "User": User,
        "Director": Director,
        "Movie": Movie,
    }


if __name__ == '__main__':
    app.run(port=8000)