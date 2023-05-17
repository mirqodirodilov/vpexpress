import sqlite3



class Tablitsa:
    def __init__(self, path_to_db="china.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table(self):
        sql = """CREATE TABLE IF NOT EXISTS users(
 		id integer PRIMARY KEY,
		user_id integer,
		username varchar(60),
		lang varchar(15),
		video TEXT,
		description TEXT,
		russ TEXT
        )"""
        self.execute(sql, commit=True)


    def create_client(self):
        sql = """CREATE TABLE IF NOT EXISTS clients(
        id integer PRIMARY KEY,
        A Text,
        B Text,
        C Text,
        D Text
        )"""
        self.execute(sql, commit=True)



    def update_lang(self, lang, user_id):
        sql = '''UPDATE users SET lang = ? WHERE user_id = ?'''
        self.execute(sql, parameters=(lang, user_id), commit=True)



    def select_lang(self, user_id):
        sql = '''SELECT lang FROM users WHERE user_id = ?'''
        return self.execute(sql, parameters=(user_id,), fetchone=True)


    def update_video(self,video_id,user_id):
    	sql = '''UPDATE users SET video = ? WHERE user_id = ?'''
    	self.execute(sql, parameters=(video_id, user_id), commit=True)


    def update_text(self,text_desc,admin):
    	sql = '''UPDATE users SET description = ? WHERE user_id = ?'''
    	self.execute(sql, parameters=(text_desc, admin), commit=True)


    def update_textrus(self,russ_text,admin):
    	sql = '''UPDATE users SET russ = ? WHERE user_id = ?'''
    	self.execute(sql, parameters=(russ_text, admin), commit=True)

    def select_desc(self,admin):
    	sql = '''SELECT description FROM users WHERE user_id = ?'''
    	return self.execute(sql,parameters=(admin,),fetchone=True)

    def select_ru_desc(self,admin):
    	sql = '''SELECT russ FROM users WHERE user_id = ?'''
    	return self.execute(sql,parameters=(admin,),fetchone=True)


    def select_video(self,admin):
    	sql = '''SELECT video FROM users WHERE user_id = ?'''
    	return self.execute(sql, parameters=(admin,), fetchone=True)

    def select_main(self,admin):
    	sql = '''SELECT * FROM users WHERE user_id = ?'''
    	return self.execute(sql,parameters=(admin,),fetchone=True)

        ##############################################################################BAZA EXCEL

    def insert_db_A(self,A):
        sql = '''INSERT INTO clients (A) VALUES (?)'''
        return self.execute(sql,parameters=(A,))



    def select_clients(self,shtrix):
        sql = '''SELECT * FROM clients WHERE A = ?'''
        return self.execute(sql,parameters=(shtrix,),fetchone=True)