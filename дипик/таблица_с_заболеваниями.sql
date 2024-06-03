CREATE TABLE Заболевания (
  id_заболевания SERIAL PRIMARY KEY,
  id_клиента INTEGER NOT NULL REFERENCES Клиенты(id_клиента),
  Название_заболевания VARCHAR(255) NOT NULL,
  Дата_диагностики DATE NOT NULL,
  Статус VARCHAR(20) NOT NULL CHECK (Статус IN ('Активное', 'Вылечено', 'В процессе лечения')),
  Комментарий TEXT
);