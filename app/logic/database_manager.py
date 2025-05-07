import sqlite3
from contextlib import contextmanager


con = sqlite3.connect("db/courses.db")
cursor = con.cursor()

# Add a course given a course code and title
def addCourse(courseCode, courseTitle, semester=None):
    if semester: # If a semester is given, put that course into that semester
        cursor.execute("INSERT INTO courses(code, title, semester) VALUES (?, ?, ?);", (courseCode, courseTitle, semester))
    else: # If no semester is given, add course with default semester (1)
        cursor.execute("INSERT INTO courses(code, title) VALUES (?, ?);",(courseCode, courseTitle))
    con.commit()

def removeCourse(courseCode):
    cursor.execute("DELETE FROM courses WHERE code = ?;", (courseCode,))
    cursor.execute("DELETE FROM assessments WHERE code = ?", (courseCode,))
    con.commit()

def renameCourse(courseCode, newCode, newTitle):
    cursor.execute("UPDATE courses SET code = ?, title = ? WHERE code = ?;", (newCode, newTitle, courseCode))
    con.commit()

def addAssessment(courseCode, name, mark, weight):
    cursor.execute("INSERT INTO assessments(code, name, mark, weight) VALUES(?, ?, ?, ?);", (courseCode, name, mark, weight))
    updateCourseAverages()
    con.commit()

def removeAssessment(courseCode, name):
    cursor.execute("DELETE FROM assessments WHERE code = ? AND name = ?;", (courseCode, name))
    updateCourseAverages()
    con.commit()

def renameAssessment(courseCode, current, new):
    cursor.execute("UPDATE assessments SET name = ? WHERE code = ? AND name = ?", (new, courseCode, current))
    con.commit()

def editAssessment(courseCode, name, newMark, newWeight):
    cursor.execute("UPDATE assessments SET mark = ?, weight = ? WHERE code = ? AND name = ?;", (newMark, newWeight, courseCode, name))
    updateCourseAverages()
    con.commit()

def updateCourseAverages():
    cursor.execute("SELECT code FROM courses;")
    numCourses = cursor.fetchall()
    for course in numCourses:
        courseCode = course[0]
        cursor.execute("SELECT SUM(mark * weight) / SUM(weight) AS weightedAverage FROM assessments WHERE code = ?;", (courseCode,))
        result = cursor.fetchone()
        if result[0] is not None:
            weightedAverage = round(result[0], 1)
            cursor.execute("UPDATE courses SET average = ? WHERE code = ?;", (weightedAverage, courseCode))
            con.commit()
    updateGPA()

def updateGPA():
    cursor.execute("SELECT code FROM courses;")
    numCourses = cursor.fetchall()
    for course in numCourses:
        courseCode = course[0]
        cursor.execute("SELECT average FROM courses WHERE code = ?;", (courseCode,))
        average = cursor.fetchone()

        if average[0] is not None:
            if 90 <= average[0] <= 100:
                letterGrade = "A+"
                gpa = 4.33
            elif 85 <= average[0] <= 90:
                letterGrade = "A"
                gpa = 4.00
            elif 80 <= average[0] <= 85:
                letterGrade = "A-"
                gpa = 3.67
            elif 77 <= average[0] <= 80:
                letterGrade = "B+"
                gpa = 3.33
            elif 73 <= average[0] <= 77:
                letterGrade = "B"
                gpa = 3.00
            elif 70 <= average[0] <= 73:
                letterGrade = "B-"
                gpa = 2.67
            elif 67 <= average[0] <= 70:
                letterGrade = "C+"
                gpa = 2.33
            elif 63 <= average[0] <= 67:
                letterGrade = "C"
                gpa = 2.00
            elif 60 <= average[0] <= 63:
                letterGrade = "C-"
                gpa = 1.67
            elif 57 <= average[0] <= 60:
                letterGrade = "D+"
                gpa = 1.33
            elif 53 <= average[0] <= 57:
                letterGrade = "D"
                gpa = 1.00
            elif 50 <= average[0] <= 53:
                letterGrade = "D-"
                gpa = 0.67
            elif 0 <= average[0] <= 50:
                letterGrade = "F"
                gpa = 0.00
            cursor.execute("UPDATE courses SET letterGrade = ? WHERE code = ?", (letterGrade, courseCode))
            cursor.execute("UPDATE courses SET gpa = ? WHERE code = ?", (gpa, courseCode))
        else:
            cursor.execute("UPDATE courses SET letterGrade = ? WHERE code = ?;", ("No Grade Available", courseCode))
            cursor.execute("UPDATE courses SET gpa = ? WHERE code = ?;", ("No GPA Available", courseCode))
    con.commit()


def editSemester(course, current, new):
    cursor.execute("UPDATE courses SET semester = ? WHERE code = ? AND semester = ?;", (new, course, current))
    con.commit()

def getSemesters():
    cursor.execute("SELECT DISTINCT semester FROM courses ORDER BY semester ASC;")
    return cursor.fetchall()

def fetchCourses(semester=None):
    if semester:
        cursor.execute("SELECT * FROM courses WHERE semester = ?;", (semester,))
    else:
        cursor.execute("SELECT * FROM courses;")
    return cursor.fetchall()

def fetchAssessments(course):
    cursor.execute("SELECT name, mark, weight FROM assessments WHERE code = ?;", (course,))
    return cursor.fetchall()

def fetchGPA(semester=None): #If semester = none, return CGPA, if semester = value, return TGPA for given semester
    if semester:
        cursor.execute("SELECT gpa FROM courses WHERE semester = ?;", (semester,))
    else:
        cursor.execute("SELECT gpa FROM courses;")
    gpaValues = cursor.fetchall()

    # NEED TO FIX CGPA
    gpaSum = 0
    if len(gpaValues) > 0:
        for i in range(0, len(gpaValues)):
            gpaSum += gpaValues[i][0]
            return round(gpaSum/len(gpaValues), 2)
    else:
        return None

def closeCon():
    con.close()