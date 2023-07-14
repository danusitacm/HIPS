import psycopg2
class DatabaseManager:
    def __init__(self, user, password, host, port, database):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.connection = None
        self.cursor= None
    def connect(self):
        try:
            self.connection = psycopg2.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print("Connection to PostgreSQL was successful")
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL:", error)
    def disconnect(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("PostgreSQL connection is closed")
    def executemany_query(self, query, params=None):
        try:
            if params:
                self.cursor.executemany(query, params)
            else:
                self.cursor.executemany(query)
            self.connection.commit()
            count = self.cursor.rowcount
            print(count, "Record(s) affected")
        except (Exception, psycopg2.Error) as error:
            print("Failed to execute query:", error)
            self.connection.rollback()
    def execute_query(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.connection.commit()
        except (Exception, psycopg2.Error) as error:
            print("Failed to execute query:", error)
            self.connection.rollback()
            
    def get_last_id_from_table(self,query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
            value=self.cursor.fetchone()[0]
            return value
        except (Exception, psycopg2.Error) as error:
            print("Failed to execute query:", error)
    
    def get_data(self,query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
            value=self.cursor.fetchall()
            return value
        except (Exception, psycopg2.Error) as error:
            print("Failed to execute query:", error)
            return None    
    def check_user_has_game(self, user_id, game_id):
        query = "SELECT COUNT(*) FROM user_buy_game WHERE user_id = %s AND game_id = %s"
        self.cursor.execute(query, (user_id, game_id))
        count = self.cursor.fetchone()[0]
        return count > 0