import sqlite3
from settings import db_path
from abc import ABC , abstractmethod


class Base_model(ABC):

    table = ''

    def __init__(self , id = None):
        self.isValid = True
        self.id = id

    @abstractmethod
    def objects():
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def del_by_id(self):
        pass

class After(Base_model):

    table = "afters_name"

    def __init__(self, afters_name , id = None):
        super().__init__(id)

        self.afters_name = afters_name

    @property
    def afters_name(self):
        return self.__afters_name

    @afters_name.setter
    def afters_name(self, afters_name):
        if isinstance(afters_name , str):
            self.__afters_name = afters_name
        else:
            self.__afters_name = "no after name"
            self.isValid = False

    def objects():
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            query = f"""Select *From {After.table}"""
            res = []
            for row in cursor.execute(query):
                res.append(After(row[1], row[0]))
            return res

    def save(self):
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(f"""INSERT INTO {After.table} (afters_name)
                    VALUES ("{self.afters_name}")""")

            self.id = cursor.lastrowid

    def update(self):
        with sqlite3.connect(db_path) as conn:
            conn.execute(f"""Update {After.table} set 
            afters_name = "{self.afters_name} "
            Where Id = {self.id}""")

            conn.commit()

    def del_by_id(id):
        try:
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
                query = f"""Delete From {After.table} Where id = {id}"""

                cursor.execute(query)
                conn.commit()
        except:
            print("Bog'lanishda xatolik")

    def __str__(self):
        return f"{self.id}, {self.afters_name}"


class Literature(Base_model):

    table = "folk_literature"

    def __init__(self,folk_literature, id = None):
        super().__init__(id)

        self.folk_literature = folk_literature

    @property
    def folk_literature(self):
        return self.__folk_literature

    @folk_literature.setter
    def folk_literature(self, folk_literature):
        if isinstance(folk_literature, str):
            self.__folk_literature = folk_literature
        else:
            self.__folk_literature = "no folk literature"
            self.isValid = False

    def objects():
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            query = f"""Select *From {Literature.table}"""
            res = []
            for row in cursor.execute(query):
                res.append(Literature(row[1], row[0]))
            return res

    def save(self):
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(f"""INSERT INTO {Literature.table} (folk_literature) 
                    VALUES ("{self.folk_literature}")""")

            self.id = cursor.lastrowid

    def update(self):
        with sqlite3.connect(db_path) as conn:
            conn.execute(f"""Update {Literature.table} set 
            folk_literature = "{self.folk_literature}"
            Where Id = {self.id}""")

            conn.commit()

    def del_by_id(id):
        try:
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
                query = f"""Delete From {Literature.table} Where Id = {id}"""

                cursor.execute(query)
                conn.commit()
        except:
            print("Bog'lanishda xatolik bor")

    def __str__(self):
        return f"{self.id}, {self.folk_literature}"


class Genre(Base_model):

    table = "genre"

    def __init__(self, genre , id = None):
        super().__init__(id)

        self.genre = genre

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, genre):
        if isinstance(genre, str):
            self.__genre = genre
        else:
            self.__genre = "no genere"
            self.isValid = False

    def objects():
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            query = f"""Select *From {Genre.table}"""
            res = []
            for row in cursor.execute(query):
                res.append(Genre(row[1], row[0]))
            return res

    def save(self):
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(f"""INSERT INTO {Genre.table} (genre) 
                    VALUES ("{self.genre}")""")

            self.id = cursor.lastrowid

    def update(self):
        with sqlite3.connect(db_path) as conn:
            conn.execute(f"""Update {Genre.table} set 
            genre = "{self.genre}"
            Where Id = {self.id}""")

            conn.commit()

    def del_by_id(id):
        try:
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
                query = f"""Delete From {Genre.table} Where Id = {id}"""

                cursor.execute(query)
                conn.commit()
        except:
            print("Bog'lanishda xatolik bor")

    def __str__(self):
        return f"{self.id}, {self.genre}"


class Publishing(Base_model):

    table = "publishing"

    def __init__(self, publishing , id = None):
        super().__init__(id)

        self.publishing = publishing

    @property
    def publishing(self):
        return self.__publishing

    @publishing.setter
    def publishing(self, publishing):
        if isinstance(publishing , str):
            self.__publishing = publishing
        else:
            self.__publishing = "no publishing"

    def objects():
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            query = f"""Select *From {Publishing.table}"""
            res = []
            for row in cursor.execute(query):
                res.append(Publishing(row[1], row[0]))
            return res

    def save(self):
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(f"""INSERT INTO {Publishing.table} (publishing) 
                    VALUES ("{self.publishing}")""")

            self.id = cursor.lastrowid

    def update(self):
        with sqlite3.connect(db_path) as conn:
            conn.execute(f"""Update {Publishing.table} set 
            publishing = "{self.publishing}"
            Where Id = {self.id}""")

            conn.commit()

    def del_by_id(id):
        try:
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
                query = f"""Delete From {Publishing.table} Where Id = {id}"""

                cursor.execute(query)
                conn.commit()
        except:
            print("Bog'lanishda xatolik bor")

    def __str__(self):
        return f"{self.id}, {self.publishing}"


class Book_shop(Base_model):

    table = "book_shop"

    def __init__(self, name, price, amount, after, literature, genre, publishing, id = None):
        super().__init__(id)

        self.name = name
        self.price = price
        self.amount = amount
        self.after = after
        self.literature = literature
        self.genre = genre
        self.publishing = publishing

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name , str):
            self.__name = name
        else:
            self.__name = "no name"
            self.isValid = False

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if isinstance(price , int):
            self.__price = price
        else:
            self.__price = 0
            self.isValid = False

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount):
        if isinstance(amount , int):
            self.__amount = amount
        else:
            self.__amount = 0
            self.isValid = False

    @property
    def after(self):
        return self.__after

    @after.setter
    def after(self, after):
        if isinstance(after , int):
            self.__after = after
        else:
            self.__after = 0
            self.isValid = False

    @property
    def after_obj(self):
        for item in After.objects():
            if item.id == self.after:
                return item

    @property
    def literature(self):
        return self.__literature

    @literature.setter
    def literature(self, literature):
        if isinstance(literature , int):
            self.__literature = literature
        else:
            self.__literature = 0
            self.isValid = False

    @property
    def literature_obj(self):
        for item in Literature.objects():
            if item.id == self.literature:
                return item

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, genre):
        if isinstance(genre , int):
            self.__genre = genre
        else:
            self.__genre = 0
            self.isValid = False

    @property
    def genre_obj(self):
        for item in Genre.objects():
            if item.id == self.genre:
                return item

    @property
    def publishing(self):
        return self.__publishing

    @publishing.setter
    def publishing(self, publishing):
        if isinstance(publishing , int):
            self.__publishing = publishing
        else:
            self.__publishing = 0
            self.isValid = False

    @property
    def publishing_obj(self):
        for item in Publishing.objects():
            if item.id == self.publishing:
                return item

    def objects():
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            query = f"""Select *From {Book_shop.table} order by name"""
            res = []
            for row in cursor.execute(query):
                res.append(Book_shop(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[0]))
            return res

    def save(self):
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(f"""
            INSERT INTO {Book_shop.table} (name, price, amount, afters_name, folk_literature, genre, publishing)
            VALUES ("{self.name}", {self.price}, {self.amount}, {self.after}, {self.literature}, {self.genre}, {self.publishing})""")

            self.id = cursor.lastrowid

    def update(self):
        with sqlite3.connect(db_path) as conn:
            conn.execute(f"""
            Update {Book_shop.table} set
            name = "{self.name}",
            price = {self.price},
            amount = {self.amount},
            afters_name = {self.after},
            folk_literature = {self.literature},
            genre = {self.genre},
            publishing = {self.publishing}
            Where Id = {self.id}""")

            conn.commit()

    def del_by_id(id):
        try:
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
                query = f"""
                Delete  From {Book_shop.table} Where Id = {id}"""

                cursor.execute(query)
                conn.commit()
        except:
            print("Bog'lanishda xatolik")

    def __str__(self):
        return f"{self.name}, {self.price}, {self.amount}, {self.literature}, {self.genre}, {self.publishing}"


class User(Base_model):

    table = "users"

    def __init__(self , first_name , last_name , user_name, password = "" , id = None):
        super().__init__(id)
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        if isinstance(first_name , str):
            self.__first_name = first_name
        else:
            self.__first_name = "No first name"
            self.isValid = False

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        if isinstance(last_name , str):
            self.__last_name = last_name
        else:
            self.__last_name = "No last name"
            self.isValid = False

    @property
    def user_name(self):
        return self.__user_name

    @user_name.setter
    def user_name(self, user_name):
        if isinstance(user_name , str):
            self.__user_name = user_name
        else:
            self.__user_name = "No user name"
            self.isValid = False

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if isinstance(password , str):
            self.__password = password
        else:
            self.__password = "No passwod"
            self.isValid = False

    def objects():
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            query = f"""Select *From {User.table}"""
            res = []
            for row in cursor.execute(query):
                res.append(User(row[1], row[2], row[3], row[4], row[0]))
            return res

    def save(self):
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(f"""
            INSERT INTO {User.table} (first_name, last_name, user_name, password)
            VALUES ("{self.first_name}"," {self.last_name}", "{self.user_name}", "{self.password}")""")

            self.id = cursor.lastrowid

    def update(self):
        with sqlite3.connect(db_path) as conn:
            conn.execute(f"""Update {User.table} set
                        first_name = "{self.first_name}",
                        last_name = "{self.last_name}",
                        user_name = "{self.user_name}",
                        password = "{self.password}"
                        Where Id = {self.id}""")

            conn.commit()

    def set_password(self, password):
        import hashlib
        encoded = hashlib.sha256()
        encoded.update(password.encode('ascii'))

        with sqlite3.connect(db_path) as conn:
            conn.execute(f"""Update {User.table} set password = "{encoded.hexdigest()}" Where id = {self.id}""")

    def del_by_id(id):
        try:
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
                query = f"""
                Delete  From {User.table} Where Id = {id}"""

                cursor.execute(query)
                conn.commit()
        except:
            print("Bog'lanishda xatolik")

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.user_name}, {self.password}"

