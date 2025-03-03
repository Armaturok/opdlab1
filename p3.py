import requests
from bs4 import BeautifulSoup

url = "https://omgtu.ru/structure/departments"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    departments = soup.find_all('div', class_='department-name')

    with open('departments.txt', 'w', encoding='utf-8') as file:
        for dept in departments:
            file.write(dept.get_text(strip=True) + '\n')

print("Список кафедр был успешно записан в файл 'departments.txt'.")
