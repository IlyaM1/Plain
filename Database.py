from pymongo import MongoClient


class Database:
    __instance__ = None

    def __init__(self):
        with open("token.cfg", "r") as file:
            self.CONNECTION_STRING = file.read()

        self.client = MongoClient(self.CONNECTION_STRING)

        # return self.client['user_shopping_list']

    @staticmethod
    def get_instance():
        if Database.__instance__ is None:
            Database.__instance__ = Database().client

        return Database.__instance__

    @staticmethod
    def get_all_users():
        return Database.__instance__.User.User.find()

    @staticmethod
    def add_new_user(new_user):
        return Database.__instance__.User.User.insert_one(new_user)

    @staticmethod
    def replace_one_note(user, id, new_note):
        return Database.__instance__.User[user.username].find_one_and_replace({'_id': id}, new_note)

    @staticmethod
    def find_all_notes_of_user(user):
        return Database.__instance__.User[user.username].find()

    @staticmethod
    def insert_one_note(user, note):
        return Database.__instance__.User[user.username].insert_one(note)


if __name__ == "__main__":
    db = Database.get_instance()
    print("Connected to MongoDB Atlas")
