import psycopg

# getAllStudents return the query that lists all the students in the database
def getAllStudents(cursor):
    cursor.execute("SELECT * FROM students;")
    return cursor.fetchall()

# addStudent function inserts a new student to the database
def addStudent(cursor, first_name, last_name, email, enrollment_date):
    sql = "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);"
    cursor.execute(sql, (first_name, last_name, email, enrollment_date))
    cursor.execute("COMMIT;")

# updateStudentEmail function updates the student's email given their ID
def updateStudentEmail(cursor, student_id, new_email):
    updateStatement = "UPDATE students SET email = %s WHERE student_id = %s;"
    cursor.execute(updateStatement, (new_email, student_id))
    cursor.execute("COMMIT;")

# deleteStudent function removes the student from the database
def deleteStudent(cursor, student_id):
    deleteStatement = "DELETE FROM students WHERE student_id = %s;"
    cursor.execute(deleteStatement, (student_id,))
    cursor.execute("COMMIT;")

# Main function to connect to database and execute queries with the cursor
def main():
    try:
        connection = psycopg.connect(
            "dbname=A3db user=postgres "
            "password=ab12345 host=localhost port=5432"
        )
        with connection.cursor() as cursor:
            addStudent(cursor, "Abby", "Bailey", "AbbyBailey@gmail.com", "2018-04-05")
            updateStudentEmail(cursor, "4", "AbbyBailey@email.ca")
            results = getAllStudents(cursor)
            print(results)
            deleteStudent(cursor, "4")
            results = getAllStudents(cursor)
            print(results)

    except psycopg.OperationalError as e:
        print(f"error: {e}")
        exit(1)

# Run the main function
main()