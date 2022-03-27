from sqlalchemy.orm.scoping import scoped_session

from project.dao.models import User


class UserDAO:
    def __init__(self, session: scoped_session):
        self._db_session = session

    def get_by_id(self, pk):
        return self._db_session.query(User).filter(User.id == pk).one_or_none()

    def get_by_email(self, email):
        return self._db_session.query(User).filter(User.email == email).one_or_none()

    def get_all(self):
        return self._db_session.query(User).all()

    def create(self, user_d):
        ent = User(**user_d)
        self._db_session.add(ent)
        self._db_session.commit()
        return ent


    def update(self, new_pd):
        user = self.get_by_id(new_pd.get('id'))
        if user:
            if new_pd.get('password'):
                user.password = new_pd.get('password')
            if new_pd.get('email'):
                user.email = new_pd.get('email')
            if new_pd.get('name'):
                user.name = new_pd.get('name')
            if new_pd.get('surname'):
                user.surname = new_pd.get('surname')
            if new_pd.get('favorite_genre'):
                user.favorite_genre = new_pd.get('favorite_genre')

        self._db_session.add(user)
        self._db_session.commit()


