from bs4 import BeautifulSoup
import requests
import logging

format_str = '%(name)s:%(levelname)s:%(message)s'
logging.basicConfig(format=format_str, level=logging.INFO)
logger = logging.getLogger('crawler')


def get_html(url: str) -> str:
    """
    Извлича и връща HTML съдържанието от даден URL адрес.

    Аргументи:
        url (str): URL адресът на уеб страницата.

    Връща:
        str: HTML съдържанието на уеб страницата или None, ако възникне грешка.
    """
    try:
        response = requests.get(url, timeout=8)
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to get HTML: {url}")
        logger.exception(e)
        return None

    if response.ok:
        return response.text
    else:
        logger.error(f"Failed to get HTML: {url}")
        return None



def save_html(html: str, filename: str) -> None:
    """
    Записва HTML съдържанието във файл.

    Аргументи:
        html (str): HTML съдържанието за записване.
        filename (str): Име на файла, в който да се запише HTML съдържанието.

    Връща:
        None
    """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)
    except OSError as e:
        logger.error(f"Failed to save HTML: {filename}")
        logger.exception(e)



    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)


if __name__ == '__main__':
    url = "https://www.jarcomputers.com/Laptopi_cat_2.html?ref=c_1"
    try:
        html = get_html(url)
    except Exception as e:
        logger.error(f"Failed to fetch HTML for: {url}")
        logger.exception(e)

    if html:
        save_html(html, "output.html")
        logger.info("HTML saved to output.html")
    else:
        logger.error("Failed to save HTML")

with open("output.html", "r", encoding="utf-8") as f:
    html_code = f.read()