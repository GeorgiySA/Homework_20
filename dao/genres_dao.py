from dao.model.genre_model import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Genre).all()

    def get_one(self, bid):
        return self.session.query(Genre).get(bid)

    def create(self, genre_d):
        ent = Genre(**genre_d)

        self.session.add(ent)
        self.session.commit()

        return ent

    def update(self, genre_d):
        genre = self.get_one(genre_d.get("id"))
        genre.name = genre_d.get("name")

        self.session.add(genre)
        self.session.commit()

    def delete(self, rid):
        genre = self.get_one(rid)

        self.session.delete(genre)
        self.session.commit()