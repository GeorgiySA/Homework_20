import pytest

from service.directors_serv import DirectorService
from conf.directors_conf import director_dao

class TestDirectorService:

    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_all(self):
        directors = self.director_service.get_all()

        assert len(directors) > 0

    def test_get_one(self):
        director = self.director_service.get_one(1)

        assert director is not None
        assert director.name is not None

    # Добавил этот тест
    def test_create(self):
        director_d = {
            "id": 2,
            "name": "Quentin Tarantino"
        }

        director = self.director_service.create(director_d)

        assert director is not None
        assert director.id == 2
        assert director.name == "Quentin Tarantino"

    # Добавил этот тест
    def test_update(self):
        director_d = {
            "id": 1,
            "name": "Taylor Sheridan"
        }

        director = self.director_service.create(director_d)

        assert director is not None
        assert director.id == 1

    # Добавил этот тест
    def test_delete(self):
        res = self.director_service.delete(1)

        assert res.status_code == 200
        assert res.status_code == 204