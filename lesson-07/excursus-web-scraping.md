# Web Scraping
- [Beautiful Soup Docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [*Python Web Scraping Tutorial: Step By Step*](https://oxylabs.io/blog/python-web-scraping)
- [Real Python: *Beautiful Soup: Build a Web Scraper With Python](https://realpython.com/beautiful-soup-web-scraper-python/)
- [*Web Scraping with Python Tutorial: Step By Step Guide*](https://nanonets.com/blog/web-scraping-with-python-tutorial/)
- [Alex The Analyst: *Scraping Data from a Real Website | Web Scraping in Python*](https://youtu.be/8dTpNajxaH0)

## **What is Web Scraping?**

Web scraping is the process of extracting data from websites, often using automated tools like Python scripts. Web scraping involves sending an HTTP request to a website, parsing the HTML response, and extracting specific data elements.

We are going to use the [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) library to extract data from the website. To install it, run the following command in your terminal:

```bash
pip install beautifulsoup4
```

### **Step 1: Inspect the Website**

Before we start writing code, let's inspect the website to understand its structure and identify the data we want to extract.

* Open the website in a web browser and inspect the HTML elements (Developer Tools in Chrome).
* Identify the table we want to extract data from. In this case, it's the first table on the page.
* Notice the `table` tags: <table> and </table>.
* There are two tables on the web site.

**Step 2: Send an HTTP Request**

We'll use the `requests` library to send an HTTP request to the website.
```python
import requests

url = 'https://caredge.com/ranks/maintenance/'
response = requests.get(url)
```
The `response` object contains the HTML content of the webpage.

**Step 3: Parse the HTML**

We'll use the `BeautifulSoup` library to parse the HTML content.
```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(response.content, 'html.parser')
```
The `soup` object is a parsed representation of the HTML content.

**Step 4: Find the Table**

We'll use the `find()` method to locate the table with tag `table`.
```python
table = soup.find('table')  # gives the first table, that is the first element with the tag 'table' ib the page
# or
table = soup.find_all('table')[0] # find_all gives a list of which we want the first element
```
The `table` variable now holds a reference to the first table on the page.

**Step 5: Extract Table Data**

We will skip the first row of the table because it contains column headers. So, we will only extract the data from the remaining rows (tbody).

We'll use a loop to extract each row and column from the table.

We will have to do some data cleaning and conversion. For example, we will remove the `$` and `,` characters from the third column and convert the text to an integer value because we want the data to be numeric.

```python

tbody = table.tbody
table_data = {}

rows = tbody.find_all('tr')
for row in rows:  # we are looping through the rows of the table
    cols = row.find_all('td')  # we are getting a list of all the columns in each row
    # we are ignoring the first column because it contains order numbers, then we are extracting the second column and using that as a key of the dictionary
    # we are cleaning the text in the third column from `$` and `,` characters and converting it from the text to an integer value
    table_data[cols[1].text.strip()] = int(cols[2].text.strip().replace('$', '').replace(',', ''))

```
We initialize an empty dictionary `table_data`. We loop through each row (`tr`) in the tbody using `find_all('tr')`.
For each row, we find all the columns (`td`) using `find_all('td')`.
We then loop through each column (`td`) and extract its text content.
We use this text content as a key in the `table_data` dictionary. If the key is not already present in the dictionary, we create a new list with an empty value.
We append the extracted value to the list associated with the key.
This code assumes that each column in the table contains a unique value (key) and a corresponding value (e.g., a numerical value). The resulting dictionary will contain these keys as keys and lists of corresponding values as values.

**Step 6: Store and Print the Data**

Finally, we'll print and store our extracted data.
```python
print(table_data)
```
This will output a dictionary containing our extracted data.

Here's the complete code:
```python
import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = 'https://caredge.com/ranks/maintenance/'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table')

table_data = {}
tbody = table.tbody
table_data = {}

rows = tbody.find_all('tr')
for row in rows:  # we are looping through the rows of the table
    cols = row.find_all('td')  # we are getting a list of all the columns in each row
    # we are ignoring the first column because it contains order numbers, then we are extracting the second column and using that as a key of the dictionary
    # we are cleaning the text in the third column from `$` and `,` characters and converting it from the text to an integer value
    table_data[cols[1].text.strip()] = int(cols[2].text.strip().replace('$', '').replace(',', ''))

pprint(table_data)
```
When you run this code, it should print a dictionary containing the extracted data from the first table on the page.

If we want to store the data locally we can use the `json` library to convert our dictionary to a JSON string and store it in a file.

```python
export = json.dumps(cars_cost)

with open('cars_cost.json', 'w') as f:
    f.write(export)
```
