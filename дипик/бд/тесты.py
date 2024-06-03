import unittest
import sqlite3
from your_file import check_is_number

class TestDatabaseOperations(unittest.TestCase):

    def setUp(self):
        self.connection = sqlite3.connect('my_database.db')
        self.cursor = self.connection.cursor()

    def tearDown(self):
        self.connection.close()

    # Тест на успешное подключение к базе данных
    def test_successful_connection(self):
        try:
            self.connection = sqlite3.connect('my_database.db')
        except Exception as e:
            self.fail(f"Failed to connect to database: {e}")

    # Тест на обработку ошибки подключения
    def test_connection_error(self):
        with self.assertRaises(Exception):
            sqlite3.connect('non_existent_database.db')

    # Тест на корректное выполнение запроса
    def test_successful_query(self):
        # Создайте тестовые данные
        self.cursor.execute("""INSERT INTO Diseases (patient_id, disease, status) VALUES ('P123', 'Грипп', 'Активный')""")
        self.connection.commit()

        # Выполните запрос и проверьте результаты
        self.cursor.execute("""SELECT * FROM Diseases WHERE Status = 'Активный' """)
        results = self.cursor.fetchall()
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0][0], 'P123')
        self.assertEqual(results[0][2], 'Активный')

    # Тест на обработку ошибки запроса
    def test_query_error(self):
        with self.assertRaises(sqlite3.OperationalError):
            self.cursor.execute("""SELECT * FROM NonExistentTable""")

    # Тест на проверку типа ID пациента
    def test_invalid_patient_id_type(self):
        # Создайте тестовые данные
        self.cursor.execute("""INSERT INTO Diseases (patient_id, disease, status) VALUES (123, 'Грипп', 'Активный')""")
        self.connection.commit()

        # Выполните запрос и проверьте ошибку
        with self.assertRaises(ValueError):
            self.cursor.execute("""SELECT * FROM Diseases WHERE Status = 'Активный' """)
            self.cursor.fetchall()

    # Тест на обработку корректных записей
    def test_valid_patient_records(self):
        # Создайте тестовые данные
        self.cursor.execute("""INSERT INTO Diseases (patient_id, disease, status) VALUES ('P123', 'Грипп', 'Активный')""")
        self.cursor.execute("""INSERT INTO Diseases (patient_id, disease, status) VALUES ('P456', 'Простуда', 'Активный')""")
        self.connection.commit()

        # Выполните запрос и проверьте результаты
        self.cursor.execute("""SELECT * FROM Diseases WHERE Status = 'Активный' """)
        results = self.cursor.fetchall()
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0][0], 'P123')
        self.assertEqual(results[0][2], 'Активный')
        self.assertEqual(results[1][0], 'P456')
        self.assertEqual(results[1][2], 'Активный')

    # Тест на обработку общих исключений
    def test_general_exception(self):
        with self.assertRaises(Exception):
            raise Exception('Искусственная ошибка')

    # Тест на закрытие соединения
    def test_connection_closed(self):
        self.connection = sqlite3.connect('my_database.db')
        self.cursor = self.connection.cursor()

        # Выполните код и проверьте, закрыто ли соединение
        self.cursor.execute("""SELECT * FROM Diseases WHERE Status = 'Активный' """)
        self.connection.commit()
        self.connection.close()

        self.assertTrue(self.connection.closed)

if __name__ == '__main__':
    unittest.main()