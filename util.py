import os
import pickle
USERS_FILE = os.path.join(os.getcwd(), "users.dat")

def create_users_file():
    # si no existe la creo
    if not os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, "wb") as db:
                pickle.dump([], db)
        except Exception as e:
            msg = f"No se pudo crear el archivo users.dat > {e.args}"
            print(msg)
create_users_file()

def load_users() -> list:
    try:
        with open(USERS_FILE, "rb") as db:
            return pickle.load(db)
    except Exception as e:
        print(e.args)
        return []

def save_users(users_list:list) -> None:
    try:
        with open(USERS_FILE, "wb") as db:
            pickle.dump(users_list, db)
    except Exception as e:
        print(e.args)

def get_usernames(users_list:list) -> list:
    return [i.username for i in users_list]