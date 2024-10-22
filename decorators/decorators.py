from datetime import datetime
import logging


logging.basicConfig(filename="logi.log", level=logging.INFO)

def time_logger(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        logging.info("Время выполнения функции %s составило %s", func.__name__,datetime.now() - start )
        return result
    return wrapper

@time_logger
def print_numb(n):
    print([i for i in range(n* 1000)])

users = [
    {
        "username": "me",
        "role": "admin"
    },
    {
        "username": "he",
        "role": "guest"
    }
]

def check_permissions(func):
    def wrapper(username):
        for dct in users:
            if dct["username"] == username and dct["role"] == "admin":
                result = func(username)
                return result
            else:
                return f"У пользователя {username} нет прав доступа"
    return wrapper

@check_permissions
def user_login(username):
    return f"{username} успешно выполнил вход"

print(user_login("me"))
print(user_login("he"))