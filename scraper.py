from bs4 import BeautifulSoup
import re
import requests

rates_url = 'https://www.generali.hu/Ugyfelszolgalat/Informaciok/Befektetesek/Eszkozalapjaink.aspx'

def scraper(url):
    print "Getting page contents for:", url
    r = requests.get(url)
    if r.status_code == 200:
        return r.text

def db_connector(db):
    print("Connect to DB here...")

def parse_table_bs(html):
    values_table = []
    soup = BeautifulSoup(html, 'html.parser')
    for table in soup.findAll("table", { "class" : "generali-table" }):
        # Drop first row of table header
        first = True
        for row in table.findAll("tr"):
            if first:
                first = False
                continue
            cells = row.findAll("td")
            if len(cells) != 3:
                raise Exception('Column number mismatch')
            values_table_row = [elem.text.strip() for elem in cells]
            values_table.append(values_table_row)
    return values_table

def main():
    db_connector("mysql")
    raw_data = scraper(rates_url)
    vt = parse_table_bs(raw_data)
    print vt

if __name__ == "__main__":
    main()
