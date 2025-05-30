from unittest.mock import MagicMock
import pytest

from dao.model.director_model import Director
from dao.directors_dao import DirectorDAO

@pytest.fixture()  # Фикстура, имитирующая модель режиссера
def director_dao():
    director_dao = DirectorDAO()

    Abdulla = Director(name="Abdulla")
    Djafar = Director(name="Djafar")
    Hasan = Director(name="Hasan")

    # director_dao.query = MagicMock()
    director_dao._get_all = MagicMock(return_value=[Abdulla, Djafar, Hasan])
    director_dao.get_one = MagicMock(return_value=Djafar)
    director_dao.create = MagicMock(return_value=Director(name="Abdulla"))
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()

    return director_dao