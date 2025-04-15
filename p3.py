import requests
from bs4 import BeautifulSoup

url = "https://omgtu.ru/general_information/the-structure/the-department-of-university.php"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Ищем все элементы <div class="col-md-6">
    department_blocks = soup.find_all('div', class_='main__content')

    departments = []

    for block in department_blocks:
        # Внутри блока находим ссылки на кафедры
        links = block.find_all('a')
        for link in links:
            name = link.get_text(strip=True)
            if name:
                departments.append(name)

    # Записываем в файл
    with open('departments.txt', 'w', encoding='utf-8') as file:
        for dept in departments:
            file.write(dept + '\n')

    print("Список кафедр был успешно записан в файл 'departments.txt'.")
else:
    print(f"Ошибка при подключении: {response.status_code}")
