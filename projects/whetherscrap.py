import pandas as pd
import requests
from bs4 import BeautifulSoup
page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.067&lon=-118.2907#.YU7duLgzZZU')
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.find_all('a'))
week = soup.find(id='seven-day-forecast')
# print(week)
iteams = week.find_all(class_='tombstone-container')
# print(iteams[0])
# print(iteams[0].find(class_='period-name').get_text())
# print(iteams[0].find(class_='short-desc').get_text())
# print(iteams[0].find(class_='temp').get_text())
# for item in iteams:
#     print(item.find(class_='period-name').get_text())
#     print(item.find(class_='short-desc').get_text())
#     print(item.find(class_='temp').get_text())

periodname = [item.find(class_='period-name').get_text() for item in iteams]
# print(periodname)
short_desc = [item.find(class_='short-desc').get_text() for item in iteams]
# print(short_desc)
temp = [item.find(class_='temp').get_text() for item in iteams]
# print(temp)

weather_staff = pd.DataFrame({
    "period_name" : periodname,
    "short_desc" : short_desc,
    "temp" : temp,
})
print(weather_staff)

weather_staff.to_csv('whether.csv')