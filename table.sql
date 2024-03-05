CREATE TABLE students(
student_id SERIAL PRIMARY KEY,
first_name varchar(255) NOT NULL,
last_name varchar(255) NOT NULL,
email varchar(255) NOT NULL UNIQUE,
enrollment_date DATE);