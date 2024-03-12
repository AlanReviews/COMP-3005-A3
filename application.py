import psycopg

def getAllStudents(cursor):
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()

def addStudent(cursor, first_name, last_name, email, enrollment_date):
    sql = "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);"
    cursor.execute(sql, (first_name, last_name, email, enrollment_date))

def updateStudentEmail(cursor, student_id, new_email):
    updateStatement = "UPDATE students SET email = %s WHERE student_id = %s;"
    cursor.execute(updateStatement, (new_email, student_id))

def deleteStudent(cursor, student_id):
    deleteStatement = "DELETE FROM students WHERE student_id = %s;"
    cursor.execute(deleteStatement, (student_id,))

def main():
    try:
        connection = psycopg.connect(
            "dbname=Assignment3 user=postgres "
            "password=ab12345 host=localhost port=5432"
        )
        with connection.cursor() as cursor:
            addStudent(cursor, "Alan", "Nguyen", "alannguyen@gmail.com", "2018-01-01")
            updateStudentEmail(cursor, 1, "johndoe@email.com")
            results = getAllStudents(cursor)
            print(results)
            deleteStudent(cursor, "1")
            results = getAllStudents(cursor)
            print(results)

    except psycopg.OperationalError as e:
        print(f"error: {e}")
        exit(1)

main()