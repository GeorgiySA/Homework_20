from dao.directors_dao import DirectorDAO
from dao.genres_dao import GenreDAO
from dao.movies_dao import MovieDAO
from service.directors_serv import DirectorService
from service.genres_serv import GenreService
from service.movies_serv import MovieService
from setup_db import db

director_dao = DirectorDAO(session=db.session)
genre_dao = GenreDAO(session=db.session)
movie_dao = MovieDAO(session=db.session)

director_service = DirectorService(dao=director_dao)
genre_service = GenreService(dao=genre_dao)
movie_service = MovieService(dao=movie_dao)
