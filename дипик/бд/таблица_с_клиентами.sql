CREATE TABLE Клиенты (
  id_клиента SERIAL PRIMARY KEY,
  ФИО VARCHAR(255) NOT NULL,
  Дата_рождения DATE NOT NULL,
  Пол CHAR(1) NOT NULL CHECK (Пол IN ('М', 'Ж')),
  Телефон VARCHAR(20),
  Email VARCHAR(255)
);
