import json

# Чтение данных из JSON файла
with open('input.json', 'r') as file:
    data = json.load(file)

# Сортировка списка пользователей по долгам в возрастающем порядке
sorted_users = sorted(data['users'], key=lambda x: float(x.get('badDebt', 0)))

# Обновление данных
data['users'] = sorted_users

# Запись отсортированных данных в новый JSON файл (или обновление существующего)
with open('sorted.json', 'w') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("Данные успешно отсортированы в возрастающем порядке и сохранены в 'sorted.json'")