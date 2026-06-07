import sqlite3


def get_grade(marks):
    if marks >= 90:
        return "A"
    if marks >= 80:
        return "B"
    if marks >= 70:
        return "C"
    if marks >= 60:
        return "D"
    return "F"


def create_student_marks_table(db_path="students.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS student_marks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT NOT NULL,
            marks INTEGER NOT NULL,
            grade TEXT
        )
    """)
    conn.commit()

    cursor.execute("PRAGMA table_info(student_marks)")
    columns = {row[1] for row in cursor.fetchall()}
    if "grade" not in columns:
        cursor.execute("ALTER TABLE student_marks ADD COLUMN grade TEXT")
        conn.commit()

    cursor.execute("""
        DELETE FROM student_marks
        WHERE id NOT IN (
            SELECT MIN(id)
            FROM student_marks
            GROUP BY student_name
        )
    """)
    conn.commit()

    students = [
        ("Alice", 85),
        ("Bob", 92),
        ("Charlie", 78),
        ("Diana", 88),
    ]

    cursor.execute("SELECT student_name FROM student_marks")
    existing_students = {row[0] for row in cursor.fetchall()}

    new_rows = [
        (name, marks, get_grade(marks))
        for name, marks in students
        if name not in existing_students
    ]

    if new_rows:
        cursor.executemany("""
            INSERT INTO student_marks (student_name, marks, grade)
            VALUES (?, ?, ?)
        """, new_rows)
        conn.commit()

    cursor.execute("SELECT id, marks FROM student_marks WHERE grade IS NULL")
    rows_to_update = cursor.fetchall()
    if rows_to_update:
        cursor.executemany(
            "UPDATE student_marks SET grade = ? WHERE id = ?",
            [(get_grade(marks), row_id) for row_id, marks in rows_to_update]
        )
        conn.commit()

    cursor.execute("SELECT student_name, marks, grade FROM student_marks ORDER BY student_name")
    for student_name, marks, grade in cursor.fetchall():
        print(f"{student_name}: {marks} points, grade {grade}")

    conn.close()


if __name__ == "__main__":
    create_student_marks_table()
