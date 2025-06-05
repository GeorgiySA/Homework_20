import pytest
from unittest.mock import MagicMock

from service.movies_serv import MovieService
from conf.movies_conf import movies_dao

class TestMovieService:

    @pytest.fixture(autouse=True)
    def movie_service(self, movies_dao):
        self.movie_service = MovieService(dao=movies_dao)

    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert len(movies) > 0

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.title is not None
        assert movie.title == "Yellowstone"
        assert movie.id == 1  # Добавил проверку id



    def test_by_director(self):
        movies = self.movie_service.get_by_director_id(2)

        assert movies is not None
        assert movies.title is not None
        assert movies.title == "The Hateful Eight"
        assert movies.id == 2
        assert movies.director_id == 2  # Добавил проверку director_id

    def test_by_genre(self):
        movies = self.movie_service.get_by_genre(1)

        assert movies is not None
        assert movies.title is not None
        assert movies.title == "Yellowstone"
        assert movies.id == 1

    def test_get_by_year(self):
        movie = self.movie_service.get_by_year(2015)

        assert movie is not None
        assert movie.title is not None
        assert movie.title == "The Hateful Eight"
        assert movie.year == 2015  # Добавил проверку director_id

    def test_create(self):
        movie_d = {
            "title": "Yellowstone",
            "description": "Владелец ранчо пытается сохранить землю своих предков. Кевин Костнер в неовестерне от автора «Ветреной реки»",
            "trailer": "https://www.youtube.com/watch?v=UKei_d0cbP4",
            "year": 2018,
            "rating": 8.6,
            "genre_id": 17,
            "director_id": 1
        }

        movie = self.movie_service.create(movie_d)

        assert movie.title is not None
        assert movie.title == "Yellowstone"   # Добавил проверку
        assert movie.year == 2018  # Добавил проверку
        assert movie.rating == 8.6  # Добавил проверку

    def test_update(self):
        movie_d = {
            "id": 4,
            "title": "Django Unchained",
            "description": "Эксцентричный охотник за головами, также известный как Дантист, промышляет отстрелом самых опасных преступников.",
            "trailer": "https://www.youtube.com/watch?v=2Dty-zwcPv4",
            "year": 2012,
            "rating": 8.4,
            "genre_id": 17,
            "director_id": 2
        }

        movie = self.movie_service.update(movie_d)
        assert movie.title is not None   # Добавил проверку
        assert movie.title == "Django Unchained"   # Добавил проверку


    def test_delete(self):  # Исправил этот метод
        result = self.movie_service.delete(1)