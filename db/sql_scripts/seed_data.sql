INSERT INTO users (first_name, last_name, email, phone_number, pw) 
VALUES 
('John', 'Doe', 'john.doe@example.com', '1234567890', 'password123'),
('Jane', 'Smith', 'jane.smith@example.com', '0987654321', 'securepass456'),
('Emily', 'Johnson', 'emily.johnson@example.com', NULL, 'mypassword789');

INSERT INTO supplements (supp_name) 
VALUES 
('Vitamin C'),
('Omega-3 Fish Oil'),
('Multivitamin'),
('Calcium'),
('Vitamin D3');

INSERT INTO user_supplements (user_id, supp_id, frequency, dosage, time_of_day) 
VALUES 
(1, 1, 'Daily', '500mg', '08:00'),
(1, 2, 'Weekly', '1000mg', NULL),
(2, 1, 'Daily', '1000mg', '09:00'),
(2, 3, 'Daily', '1 tablet', '12:00'),
(3, 4, 'Daily', '600mg', '07:30'),
(3, 5, 'Weekly', '2000 IU', NULL);

INSERT INTO supplement_intake (us_id, intake_date, taken, taken_at) 
VALUES 
(1, DATE('2024-10-20'), TRUE, CURRENT_TIMESTAMP),
(1, DATE('2024-10-21'), FALSE, NULL),
(2, DATE('2024-10-20'), TRUE, CURRENT_TIMESTAMP),
(2, DATE('2024-10-21'), TRUE, CURRENT_TIMESTAMP),
(3, DATE('2024-10-20'), FALSE, NULL),
(3, DATE('2024-10-21'), FALSE, NULL);