import sqlite3

def check_is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

try:
    # Подключиться к базе данных
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()

    # Выполнить запрос SQL
    query = """ SELECT * FROM Diseases WHERE Status = 'Активный' """
    cursor.execute(query)

    # Проверить результаты запроса
    results = cursor.fetchall()

    # Если есть записи, соответствующие условию, отправить уведомление
    if results:
        for row in results:
            if check_is_number(row[0]):
                raise ValueError("ID пациента должен быть строковым значением")
            print(f"У пациента с ID {row[0]} есть активное заболевание: {row[2]}")

except Exception as e:
    # Обработать ошибку
    print(f"Ошибка при работе с базой данных: {e}")

# Закрыть соединение с базой данных
connection.close()