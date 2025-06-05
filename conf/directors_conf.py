from unittest.mock import MagicMock
import pytest

from dao.model.director_model import Director
from dao.directors_dao import DirectorDAO

@pytest.fixture()  # Фикстура, имитирующая модель режиссера
def director_dao():
    director_dao = DirectorDAO()

    # Исправил имена режиссёров
    Q_Tarantino = Director(name="Quentin Tarantino")
    T_Sheridan = Director(name="Taylor Sheridan")
    V_Weinstock = Director(name="Vladimir Weinstock")

    # Исправил возвращаемые ответы
    director_dao._get_all = MagicMock(return_value=[Q_Tarantino, T_Sheridan,
                                                    V_Weinstock])
    director_dao.get_one = MagicMock(return_value=T_Sheridan)
    director_dao.create = MagicMock(return_value=Director(name="V_Weinstock"))
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()

    return director_dao