from app import db


class User(db.DynamicDocument):
    email = db.StringField(required=True, unique=True)
    # hash_pw = db.BinaryField(required=True)
    password = db.BinaryField()
    firstname = db.StringField(default='')
    lastname = db.StringField(default='')

    books = db.ListField(db.ObjectIdField())

    city = db.StringField()

    meta = {'collection': 'users'}

    @classmethod
    def users_count(cls) -> int:
        return User.objects().count()


class Book(db.DynamicDocument):
    _id = db.StringField(max_length=20)
    isbn = db.StringField(required=True)
    title = db.StringField()
    language = db.StringRield()

    amazon_url = db.StringField(default=None)
    goodreads_url = db.StringField(default=None)

    meta = {'collection': 'books'}

    @classmethod
    def books_count(cls) -> int:
        return Book.objects().count()
