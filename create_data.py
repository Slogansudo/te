from database_bot import Database


def table():
    menu = f"""
    CREATE TABLE menu(menu_id integer PRIMARY KEY,
    name VARCHAR(20),
    create_date TIMESTAMP DEFAULT now());"""

    category = f"""
    CREATE TABLE category(menu_id integer PRIMARY KEY,
    name VARCHAR(20),
    create_date TIMESTAMP DEFAULT now());"""

    data = {
        "menu": menu,
        "category": category
    }

    for i in data:
        print(f"{i} - {Database.connect(data[i], 'insert')}")
