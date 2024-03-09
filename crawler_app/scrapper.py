from bs4 import BeautifulSoup
import mysql.connector

# Отваряне на HTML файла
with open("output.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Създаване на BeautifulSoup обект
soup = BeautifulSoup(html_code, "html.parser")

# Намиране на всички елементи с продукти
products = soup.select(".sProduct")

# Информация за свързване
db_host = "localhost"
db_user = "root"
db_password = "Julia132293@"

# Свързване с базата данни
connection = mysql.connector.connect(
    host=db_host, user=db_user, password=db_password, database="laptop_base"
)

# Итерация през продуктите
for product in products:
    model_element = product.select_one(".short_title.fn a")
    model = model_element.text.split(" ")[1] if model_element else "Няма информация"
    
    screen_size_element = product.select_one(".pprop li:nth-child(3) span")
    screen_size = float(screen_size_element.text) if (screen_size_element and screen_size_element.text.isdigit()) else 0
    
    price_element = product.select_one(".row-price .price")
    price = float(price_element.text.replace(" лв", "").replace(",", ".")) if (price_element and price_element.text.replace(" лв", "").replace(",", ".").replace(".", "", 1).isdigit()) else 0

    # Вмъкване на данните в базата данни
    cursor = connection.cursor()
    sql = "INSERT INTO products (model, screen_size, price) VALUES (%s, %s, %s)"
    values = (model, screen_size, price)
    cursor.execute(sql, values)
    connection.commit()
    cursor.close()

# Затваряне на връзката с базата данни
connection.close()
