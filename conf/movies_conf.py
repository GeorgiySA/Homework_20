from unittest.mock import MagicMock
import pytest

from dao.model.movie_model import Movie
from dao.movies_dao import MovieDAO

@pytest.fixture()  # Фикстура, имитирующая модель фильма
def movies_dao():

    Yellowstone = Movie(id=1, title="Yellowstone", description="Владелец ранчо пытается сохранить землю своих предков. Кевин Костнер в неовестерне от автора «Ветреной реки»",
                               trailer="https://www.youtube.com/watch?v=UKei_d0cbP4", year=2018, rating=8.6, genre_id=17, director_id=1)
    The_Hateful_Eight = Movie(id=2, title="The Hateful Eight", description="США после Гражданской войны. Легендарный охотник за головами Джон Рут по кличке Вешатель конвоирует заключенную.",
                               trailer="https://www.youtube.com/watch?v=lmB9VWm0okU", year=2015, rating=7.8, genre_id=4, director_id=2)
    Django_Unchained = Movie(id=4, title="Django Unchained", description="Эксцентричный охотник за головами, также известный как Дантист, промышляет отстрелом самых опасных преступников.",
                               trailer="https://www.youtube.com/watch?v=2Dty-zwcPv4", year=2012, rating=8.4, genre_id=17, director_id=2)

    movies_dao = MovieDAO()
    movies_dao.get_all = MagicMock(return_value=[Yellowstone, The_Hateful_Eight])
    movies_dao.get_one = MagicMock(return_value=Yellowstone)
    movies_dao.get_by_director = MagicMock(return_value=Yellowstone)
    movies_dao.get_by_genre = MagicMock(return_value=The_Hateful_Eight)
    movies_dao.get_by_year = MagicMock(return_value=Django_Unchained)
    movies_dao.create = MagicMock(return_value=Movie(name="Django_Uncharted"))
    movies_dao.update = MagicMock()
    movies_dao.delete = MagicMock()

    return movies_dao