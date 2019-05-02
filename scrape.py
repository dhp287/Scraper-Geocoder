from bs4 import BeautifulSoup
import requests
import xlsxwriter

workbook = xlsxwriter.Workbook('arrays.xlsx')

response = requests.get("http://www.city-data.com/accidents/acc-Cincinnati-Ohio.html", timeout=20)

page_content = BeautifulSoup(response.content, "html.parser")

tables = page_content.findAll("table", attrs={"class":"table tblsort tblsticky tabBlue"})
for table in tables:
    worksheet = workbook.add_worksheet()
    col = 0
    rows = table.findAll("tr")
    headers = rows[0].findAll("th")
    for header in headers:
        worksheet.write(0, col,  header.text)
        col += 1
    for i in range(1, len(rows)):
        col = 0
        values = rows[i].findAll("td")
        for v in values:
            worksheet.write(i, col, v.text)
            col += 1
workbook.close()