from crawler_app import crawler
from crawler_app import scrapper
from db import DB

# Дефиниране на информацията за MySQL
db_host = "localhost"
db_user = "root"
db_password = "password"
db_database = "hp_laptops"


db = DB(db_host, db_user, db_password, db_database)

# 1. Извикване на crawler-a
products = crawler.get_products()

# 2. Извикване на scrapper-a
for product in products:
    scrapper.extract_data(product)