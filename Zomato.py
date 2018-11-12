from bs4 import BeautifulSoup
import requests
import pandas as pd
from openpyxl.workbook import Workbook

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
response = requests.get("https://www.zomato.com/pune/restaurants/mcdonalds", headers=headers)
content = response.content
soup = BeautifulSoup(content, "html.parser")
list_tr = soup.find_all("div", {"id": "orig-search-list"})
list_t = list_tr[0].find_all("div", {"class": "content"})

list_rest = []
for tr in list_t:
    dataframe = {}
    dataframe["Resturant_Name"] = (tr.find("a", {"data-result-type": "ResCard_Name"})).text.replace('\n', ' ')
    dataframe["Resturant_Address"] = (tr.find("div", {"class": "col-m-16 search-result-address grey-text nowrap ln22"})).text.replace('\n', ' ')
    dataframe["Rating"] = (tr.find('div', {"data-variation": "mini inverted"})).text.replace('/n', ' ').strip()
    list_rest.append(dataframe)

df = pd.DataFrame(list_rest)
# df.to_csv("zomato_res.csv", index=False)

df.to_excel('PythonExport.xlsx')
