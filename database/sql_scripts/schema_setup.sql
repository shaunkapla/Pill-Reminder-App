-- Drop tables if they exist to avoid conflicts when running the script
DROP TABLE IF EXISTS supplement_intake;
DROP TABLE IF EXISTS user_supplements;
DROP TABLE IF EXISTS supplements;
DROP TABLE IF EXISTS users;

-- Create the users table
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone_number VARCHAR(20) NULL,
    pw TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create the supplements table
CREATE TABLE supplements (
    supp_id INTEGER PRIMARY KEY AUTOINCREMENT,
    supp_name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create the user_supplements table
CREATE TABLE user_supplements (
    us_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    user_id INTEGER NOT NULL,           
    supp_id INTEGER NOT NULL,                
    frequency VARCHAR(50) NOT NULL,        
    dosage VARCHAR(50) NOT NULL,             
    time_of_day TIME NULL,        
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (supp_id) REFERENCES supplements(supp_id) ON DELETE CASCADE
);

-- Create the supplement_intake table
CREATE TABLE supplement_intake (
    intake_id INTEGER PRIMARY KEY AUTOINCREMENT,
    us_id INTEGER NOT NULL,
    intake_date DATE NOT NULL,
    taken BOOLEAN DEFAULT FALSE,
    taken_at TIMESTAMP NULL,
    FOREIGN KEY (us_id) REFERENCES user_supplements(us_id) ON DELETE CASCADE,
    UNIQUE (us_id, intake_date)
);