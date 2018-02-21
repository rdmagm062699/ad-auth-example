class User:
    def __init__(self, data):
        self.__data = data

    def is_authenticated(self):
        return self.__access_token is not None

    def is_active(self):
        return is_authenticated()

    def is_anonymous(self):
        return is_authenticated()

    def get_id(self):
        return self.__data['id']

    def data(self):
        return self.__data
