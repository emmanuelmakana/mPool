import requests as rq
import re
# from requests_html import Session
from bs4 import BeautifulSoup as bs
import html5lib
from fake_useragent import UserAgent

ua = UserAgent()
url = "https://www.forebet.com/en/football-tips-and-predictions-for-today"
# url = "https://www.predictz.com/predictions/"
response = rq.get(url, headers={"user-agent": ua.random})
soup = bs(response.content, 'html5lib')

with open("forebet.html", "w", encoding="utf-8") as out_file:
    out_file.write(str(soup))

with open("forebet.html", "r", encoding="utf-8") as f:
    html_page = f.read()

# print(html_page)

soup = bs(html_page, 'html5lib')
# print(soup.prettify())

main_table = soup.find("table", {"class": "schema"}).tbody
main_rows = main_table.find_all("tr", {'class': re.compile(r'tr_0|tr_1')})
# print(main_table)
main_data = []
for idx, row in enumerate(main_rows):
    if idx <= len(main_rows):
        row_data = row.find_all("td")
        ind_rows = []
        for td_idx, td in enumerate(row_data):
            if td_idx == 0:
                # print(td)
                home_team = row.find("span", {"class": "homeTeam"})
                away_team = row.find("span", {"class": "awayTeam"})
                ind_rows.append(home_team.text)
                ind_rows.append(away_team.text)
                # print(f"{td_idx}:{home_team.text}, {away_team.text}")
            elif td_idx in [8, 11]:
                td_data = td.text.split("\n")[0].strip()
                ind_rows.append(td_data)
                # print(f"{td_idx}: {td_data}")
            else:
                td_data = td.text
                ind_rows.append(td_data.strip().replace("\n", "").replace("\t", ""))
                # print(f"{td_idx}: {td_data}")
        main_data.append(ind_rows)
        # print(ind_rows)
print(main_data)
