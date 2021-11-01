class Database:
    __instance__ = None

    def __init__(self):
        with open("token.cfg", "r") as file:
            self.CONNECTION_STRING = file.read()

        from pymongo import MongoClient
        self.client = MongoClient(self.CONNECTION_STRING)

        # return self.client['user_shopping_list']

    @staticmethod
    def get_instance():
        if Database.__instance__ is None:
            Database.__instance__ = Database().client

        return Database.__instance__


if __name__ == "__main__":
    db = Database.get_instance()
    print("Connected to MongoDB Atlas")
