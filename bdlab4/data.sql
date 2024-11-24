DROP DATABASE IF EXISTS dblab;
CREATE DATABASE dblab;
USE dblab;

CREATE TABLE IF NOT EXISTS Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    phone_number VARCHAR(20),
    email VARCHAR(255),
    address TEXT
);

CREATE TABLE IF NOT EXISTS Manufacturers (
    manufacturer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS Equipment (
    equipment_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    manufacturer_id INT,
    FOREIGN KEY (manufacturer_id) REFERENCES Manufacturers(manufacturer_id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS Spare_Parts (
    part_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    manufacturer_id INT,
    quantity INT NOT NULL,
    FOREIGN KEY (manufacturer_id) REFERENCES Manufacturers(manufacturer_id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS Technicians (
    technician_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    phone_number VARCHAR(20),
    email VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS Repair_Types (
    repair_type_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS User_Equipment (
    user_equipment_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    equipment_id INT,
    serial_number VARCHAR(255),
    purchase_date DATE,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (equipment_id) REFERENCES Equipment(equipment_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Repairs (
    repair_id INT AUTO_INCREMENT PRIMARY KEY,
    user_equipment_id INT,
    repair_type_id INT,
    status ENUM('in_progress', 'completed') NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    FOREIGN KEY (user_equipment_id) REFERENCES User_Equipment(user_equipment_id) ON DELETE CASCADE,
    FOREIGN KEY (repair_type_id) REFERENCES Repair_Types(repair_type_id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS Replaced_Parts (
    replaced_part_id INT AUTO_INCREMENT PRIMARY KEY,
    repair_id INT,
    part_id INT,
    quantity INT NOT NULL,
    FOREIGN KEY (repair_id) REFERENCES Repairs(repair_id) ON DELETE CASCADE,
    FOREIGN KEY (part_id) REFERENCES Spare_Parts(part_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Technician_Schedule (
    schedule_id INT AUTO_INCREMENT PRIMARY KEY,
    technician_id INT,
    work_day ENUM('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'),
    start_time TIME,
    end_time TIME,
    FOREIGN KEY (technician_id) REFERENCES Technicians(technician_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Technician_Repairs (
    technician_repair_id INT AUTO_INCREMENT PRIMARY KEY,
    technician_id INT,
    repair_id INT,
    FOREIGN KEY (technician_id) REFERENCES Technicians(technician_id) ON DELETE CASCADE,
    FOREIGN KEY (repair_id) REFERENCES Repairs(repair_id) ON DELETE CASCADE,
    UNIQUE (technician_id, repair_id)
);

-- Додавання даних у таблицю Users
INSERT INTO Users (name, phone_number, email, address) VALUES
('Іван Іванов', '0671234567', 'ivan.ivanov@example.com', 'Київ, вул. Шевченка, 1'),
('Петро Петров', '0672345678', 'petro.petrov@example.com', 'Львів, вул. Франка, 2'),
('Олена Олененко', '0673456789', 'olena.olenko@example.com', 'Одеса, вул. Дерибасівська, 3'),
('Микола Миколенко', '0674567890', 'mykola.mykolenko@example.com', 'Харків, вул. Пушкіна, 4'),
('Анна Анненко', '0675678901', 'anna.annenko@example.com', 'Дніпро, вул. Грушевського, 5'),
('Тарас Тарасенко', '0676789012', 'taras.tarasenk@example.com', 'Запоріжжя, вул. Свердлова, 6'),
('Олександр Олександров', '0677890123', 'oleksandr.oleks@example.com', 'Кривий Ріг, вул. Леніна, 7'),
('Валентина Валентиненко', '0678901234', 'valentina.valentin@example.com', 'Чернівці, вул. Гоголя, 8'),
('Сергій Сергійович', '0679012345', 'serhii.serhiyovych@example.com', 'Ужгород, вул. Левка, 9'),
('Дмитро Дмитренко', '0670123456', 'dmytro.dmytrenko@example.com', 'Миколаїв, вул. Садова, 10');

-- Додавання даних у таблицю Manufacturers
INSERT INTO Manufacturers (name) VALUES
('ТМ АБВ'),
('ТМ ГДЕ'),
('ТМ XYZ'),
('ТМ DEF'),
('ТМ GHI'),
('ТМ JKL'),
('ТМ MNO'),
('ТМ PQR'),
('ТМ STU'),
('ТМ VWX');

-- Додавання даних у таблицю Equipment
INSERT INTO Equipment (name, manufacturer_id) VALUES
('Смартфон', 1),
('Ноутбук', 2),
('Принтер', 3),
('Сканер', 4),
('Факс', 5),
('Телевізор', 6),
('Камера', 7),
('Аудіосистема', 8),
('Модем', 9),
('Проектор', 10);

-- Додавання даних у таблицю Spare_Parts
INSERT INTO Spare_Parts (name, manufacturer_id, quantity) VALUES
('Батарея', 1, 20),
('Зарядний пристрій', 2, 15),
('Картридж', 3, 10),
('Дисплей', 4, 5),
('Клавіатура', 5, 30),
('Миша', 6, 25),
('Диск', 7, 12),
('Мікрофон', 8, 18),
('Датчик', 9, 8),
('Кабель', 10, 50);

-- Додавання даних у таблицю Technicians
INSERT INTO Technicians (name, phone_number, email) VALUES
('Технік 1', '0681234567', 'tech1@example.com'),
('Технік 2', '0682345678', 'tech2@example.com'),
('Технік 3', '0683456789', 'tech3@example.com'),
('Технік 4', '0684567890', 'tech4@example.com'),
('Технік 5', '0685678901', 'tech5@example.com'),
('Технік 6', '0686789012', 'tech6@example.com'),
('Технік 7', '0687890123', 'tech7@example.com'),
('Технік 8', '0688901234', 'tech8@example.com'),
('Технік 9', '0689012345', 'tech9@example.com'),
('Технік 10', '0680123456', 'tech10@example.com');

-- Додавання даних у таблицю Repair_Types
INSERT INTO Repair_Types (name) VALUES
('Діагностика'),
('Ремонт'),
('Обслуговування'),
('Встановлення'),
('Модернізація'),
('Виправлення помилок'),
('Оновлення'),
('Перевірка'),
('Чистка'),
('Замовлення деталей');

-- Додавання даних у таблицю User_Equipment
INSERT INTO User_Equipment (user_id, equipment_id, serial_number, purchase_date) VALUES
(1, 1, 'SN001', '2023-01-15'),
(2, 2, 'SN002', '2023-02-20'),
(3, 3, 'SN003', '2023-03-25'),
(4, 4, 'SN004', '2023-04-10'),
(5, 5, 'SN005', '2023-05-05'),
(6, 6, 'SN006', '2023-06-12'),
(7, 7, 'SN007', '2023-07-15'),
(8, 8, 'SN008', '2023-08-20'),
(9, 9, 'SN009', '2023-09-25'),
(10, 10, 'SN010', '2023-10-30');

-- Додавання даних у таблицю Repairs
INSERT INTO Repairs (user_equipment_id, repair_type_id, status, start_date, end_date) VALUES
(1, 1, 'in_progress', '2023-10-01', NULL),
(2, 2, 'completed', '2023-09-15', '2023-09-20'),
(3, 3, 'in_progress', '2023-10-05', NULL),
(4, 4, 'completed', '2023-09-10', '2023-09-15'),
(5, 5, 'in_progress', '2023-10-10', NULL),
(6, 6, 'completed', '2023-08-01', '2023-08-05'),
(7, 7, 'in_progress', '2023-07-15', NULL),
(8, 8, 'completed', '2023-06-01', '2023-06-10'),
(9, 9, 'in_progress', '2023-05-01', NULL),
(10, 10, 'completed', '2023-04-15', '2023-04-20');

-- Додавання даних у таблицю Replaced_Parts
INSERT INTO Replaced_Parts (repair_id, part_id, quantity) VALUES
(1, 1, 1),
(2, 2, 1),
(3, 3, 2),
(4, 4, 1),
(5, 5, 1),
(6, 6, 3),
(7, 7, 1),
(8, 8, 2),
(9, 9, 1),
(10, 10, 1);

-- Додавання даних у таблицю Technician_Schedule
INSERT INTO Technician_Schedule (technician_id, work_day, start_time, end_time) VALUES
(1, 'Monday', '09:00:00', '17:00:00'),
(2, 'Tuesday', '09:00:00', '17:00:00'),
(3, 'Wednesday', '09:00:00', '17:00:00'),
(4, 'Thursday', '09:00:00', '17:00:00'),
(5, 'Friday', '09:00:00', '17:00:00'),
(6, 'Saturday', '10:00:00', '16:00:00'),
(7, 'Sunday', '10:00:00', '16:00:00'),
(1, 'Tuesday', '09:00:00', '17:00:00'),
(2, 'Wednesday', '09:00:00', '17:00:00'),
(3, 'Thursday', '09:00:00', '17:00:00');

-- Додавання даних у таблицю Technician_Repairs
INSERT INTO Technician_Repairs (technician_id, repair_id) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8),
(9, 9),
(10, 10);
