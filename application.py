import psycopg

def getAllStudents(cursor):
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()

# def addStudent(cursor, first_name, last_name, email, enrollment_date):

# def updateStudentEmail(student_id, new_email):

# def deleteStudent(student_id):

def main():
    try:
        connection = psycopg.connect(
            "dbname=Assignment3 user=postgres "
            "password=ab12345 host=localhost port=5432"
        )
        with connection.cursor() as cursor:
            results = getAllStudents(cursor)
            print(results)

    except psycopg.OperationalError as e:
        print(f"error: {e}")
        exit(1)

main()