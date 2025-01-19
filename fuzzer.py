import requests


def main():
    file_name = input('Файл с ссылками (адрес относительный):\t')
    url = input('URL для поиска:\t')
    extensions_input = input('Введите расширения или фильтры через запятую (например, .php,.html):\t')
    extensions = [ext.strip() for ext in extensions_input.split(',')]

    links = []

    with open(file_name, 'rt') as f:
        links = f.readlines()
    if len(links) == 0:
        print('Нет ссылок для проверки')
        return
    filtered_links = []

    for link in links:
        link = link.strip()

        for ext in extensions:
            full_link = f"{url}{link}{ext}"

            try:
                response = requests.get(full_link)
                if response.status_code != 404:
                    print(f'{full_link} - существует')
                    filtered_links.append(full_link)
            except requests.exceptions.RequestException as e:
                print(f'Ошибка при запросе к {full_link}: {e}')

    with open('file.txt', 'w') as f:
        for link in filtered_links:
            f.write(link + '\n')
        f.close()

    print(f'Отфильтрованные ссылки сохранены в file.txt. Найдено {len(filtered_links)} ссылок.')


if __name__ == "__main__":
    main()
