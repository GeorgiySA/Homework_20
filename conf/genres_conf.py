from unittest.mock import MagicMock
import pytest

from dao.model.genre_model import Genre
from dao.genres_dao import GenreDAO

@pytest.fixture()  # Фикстура, имитирующая модель жанра
def genres_dao():
    genres_dao = GenreDAO()

    adventures = Genre(name="Adventure")
    comedy = Genre(name="Comedy")
    anime = Genre(name="Anime")

    genres_dao.get_all = MagicMock(return_value=[adventures, comedy, anime])
    genres_dao.get_one = MagicMock(return_value=adventures)
    # genres_dao.create = MagicMock(return_value=Genre(name="comedy"))
    # genres_dao.update = MagicMock()
    # genres_dao.delete = MagicMock()

    return genres_dao
