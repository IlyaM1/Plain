from pymongo import MongoClient
import concurrent.futures as pool


class Database:
    __instance__ = None

    def __init__(self):
        with open("token.cfg", "r") as file:
            self.CONNECTION_STRING = file.read()

        self.__executor__ = pool.ThreadPoolExecutor(max_workers=10)

        self.client = MongoClient(self.CONNECTION_STRING)

        # return self.client['user_shopping_list']

    @staticmethod
    def get_instance():
        if Database.__instance__ is None:
            Database.__instance__ = Database()

        return Database.__instance__

    def get_all_users(self):
        return self.__executor__.submit(self.client.User.User.find)

    def add_new_user(self, new_user):
        return self.__executor__.submit(self.client.User.User.insert_one, new_user)

    def replace_one_note(self, user, id, new_note, window):
        return self.__executor__.submit(self.client.User[user.username].find_one_and_replace, {'_id': id},
                                        new_note).add_done_callback(lambda _: window.notesUpdate())

    def find_all_notes_of_user(self, user):
        return self.__executor__.submit(self.client.User[user.username].find)

    def insert_one_note(self, user, note, window):
        return self.__executor__.submit(self.client.User[user.username].insert_one, note).add_done_callback(lambda _: window.notesUpdate())

    def get_all_users_executor(self):
        return self.__executor__.submit(Database.get_all_users)


if __name__ == "__main__":
    db = Database.get_instance()
    print("Connected to MongoDB Atlas")
