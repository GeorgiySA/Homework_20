import pytest

from service.genres_serv import GenreService
from conf.genres_conf import genres_dao

class TestGenreService:

    @pytest.fixture(autouse=True)
    def genre_service(self, genres_dao):
        self.genre_service = GenreService(dao=genres_dao)

    def test_get_all(self):
        genres = self.genre_service.get_all()

        assert len(genres) > 0

    def test_get_one(self):
        genre = self.genre_service.get_one(1)

        assert genre is not None
        assert genre.name is not None

    # Добавил этот тест
    def test_create(self):
        genre_d = {
            "id": 5,
            "name": "Adventure"
        }

        genre = self.genre_service.create(genre_d)

        assert genre is not None
        assert genre.id == 5
        assert genre.name == "Adventure"

    # Добавил этот тест
    def test_update(self):
        genre_d = {
            "id": 1,
            "name": "Comedy"
        }

        genre = self.genre_service.create(genre_d)

        assert genre is not None
        assert genre.id == 1

    # Добавил этот тест
    def test_delete(self):
        res = self.genre_service.delete(1)