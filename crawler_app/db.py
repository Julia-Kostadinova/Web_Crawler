import mysql.connector

class DB:
    def __init__(self, host, user, password, database):
        """
        Инициализира класа DB с информация за свързване с MySQL.

        Args:
            host (str): Адрес на MySQL сървъра.
            user (str): Потребителско име за MySQL.
            password (str): Парола за MySQL.
            database (str): Име на базата данни.
        """
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        """
        Свързва се с MySQL базата данни.
        """
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
            )
        except mysql.connector.Error as e:
            print(f"Error connecting to MySQL: {e}")

 
    