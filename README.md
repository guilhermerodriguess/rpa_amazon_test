# Amazon Web Scraper for Books
Este é um script Python que utiliza Selenium para buscar informações sobre livros na Amazon e salvar os dados coletados em um arquivo CSV.

## Pré-requisitos
Certifique-se de ter Python 3 instalado no seu ambiente. Instale também as seguintes bibliotecas Python necessárias:

```
pip install selenium pandas webdriver_manager
```
## Configuração
O script utiliza o WebDriver do Chrome para automatizar o navegador. Certifique-se de ter o Chrome instalado no seu sistema.

Como usar
1. Clone este repositório:

```
git clone https://github.com/seu-usuario/amazon-books-scraper.git
cd amazon-books-scraper
```
2. Execute o script **rpa_amazon.py**:

```
python rpa_amazon.py
```

Isso iniciará o script que irá acessar a Amazon, buscar livros relacionados a "automação", coletar informações como título, autor, preço, classificação e número de avaliações dos primeiros 8 resultados, e salvar esses dados em um arquivo CSV chamado livros_sobre_automacao.csv.

## Resultados
Após a execução do script, você encontrará um arquivo **livros_sobre_automacao.csv** no diretório atual contendo os seguintes dados:

- **Titulo**: Título do livro encontrado.
- **Autor**: Autor ou autores do livro.
- **Preço**: Preço do livro, formatado como "R$ X,X" quando disponível.
- **Nota**: Classificação do livro.
- **Avaliações**: Número de avaliações recebidas pelo livro.
## Notas adicionais
- Este script foi desenvolvido para fins educacionais e de demonstração de web scraping usando Selenium.
- A Amazon pode alterar sua estrutura HTML a qualquer momento, o que pode afetar a funcionalidade deste script.
