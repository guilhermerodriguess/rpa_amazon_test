import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.amazon.com.br/ref=nav_logo")

assert "Amazon" in driver.title, "Página da Amazon não carregou corretamente"
print("Página da Amazon carregada com sucesso")

try:
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys("livros sobre automacao")
    search_box.send_keys(Keys.RETURN)
except Exception as e:
    print("Erro ao tentar encontrar a barra de pesquisa:", e)
    driver.quit()
    exit()

time.sleep(3)

books = []
book_elements = driver.find_elements(By.XPATH, '//div[contains(@class, "s-main-slot")]/div[@data-component-type="s-search-result"]')

for book in book_elements[:8]:
    try:
        title = book.find_element(By.XPATH, './/h2/a/span').text
    except:
        title = "N/A"

    try:
        author_element = book.find_element(By.XPATH, './/div[@class="a-row a-size-base a-color-secondary"]')
        author = author_element.text.replace("Edição Português", "").replace("Edição Inglês", "").replace("por ", "").strip()
    except:
        author = "N/A"

    try:
        price_element = book.find_element(By.XPATH, './/span[@class="a-price-whole"]')
        price_fraction = book.find_element(By.XPATH, './/span[@class="a-price-fraction"]').text

        if price_element.text == "0":
          price_text = book.find_element(By.XPATH, './/div[@data-cy="secondary-offer-recipe"]//span').text.strip()
          price = price_text.replace("Ou R$ ", "").replace(" para comprar", "")
        else:
          price = f"{price_element.text},{price_fraction}"
    except:
        price = "N/A"

    try:
        rating_element = book.find_element(By.XPATH, './/span[@class="a-icon-alt"]')
        rating = rating_element.get_attribute("textContent").split(" ")[0]
    except:
        rating = "N/A"

    try:
        num_reviews = book.find_element(By.XPATH, './/span[@class="a-size-base s-underline-text"]').text
    except:
        num_reviews = "N/A"

    books.append([title, author, price, rating, num_reviews])

driver.quit()

df = pd.DataFrame(books, columns=["Titulo", "Autor", "Preço", "Nota", "Avaliações"])
df = df.sort_values(by="Titulo")
df.to_csv("livros_sobre_automacao.csv", index=False, encoding='utf-8-sig')

print("Dados coletados e salvos em 'livros_sobre_automacao.csv'")
