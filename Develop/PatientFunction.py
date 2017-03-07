import sqlite3


def connect():
    conn = sqlite3.connect("patient.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS patient (id INTEGER PRIMARY KEY, patientID TEXT, patientName TEXT, patientPhone TEXT, patientAge INTEGER, patientBirthYear INTEGER, patientHistory TEXT, patientFamilyHistory TEXT, patientDescription TEXT, patientDiagnostic TEXT)")
    conn.commit()
    conn.close()


def insert(patientID, patientName, patientPhone, patientAge, patientBirthYear, patientHistory, patientFamilyHistory, patientDescription, patientDiagnostic):
    conn = sqlite3.connect("patient.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO patient VALUES (null,?,?,?,?,?,?,?,?,?)", (patientID, patientName, patientPhone, patientAge, patientBirthYear, patientHistory, patientFamilyHistory, patientDescription, patientDiagnostic))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("patient.db")
    cur = conn.cursor()
    cur.execute("SELECT * from patient")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(patientID="", patientName="", patientPhone="", patientAge="", patientBirthYear=""):
    conn = sqlite3.connect("patient.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM patient WHERE patientID=? OR patientName=? OR patientPhone=? or patientAge=? OR patientBirthYear=?", (patientID, patientName, patientPhone, patientAge, patientBirthYear))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("patient.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM patient WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update(id, patientID, patientName, patientPhone, patientAge, patientBirthYear, patientHistory, patientFamilyHistory, patientDescription, patientDiagnostic):
    conn = sqlite3.connect("patient.db")
    cur = conn.cursor()
    cur.execute("UPDATE patient SET patientID=?, patientName=?, patientPhone=?, patientAge=?, patientBirthYear=?, patientHistory=?, patientFamilyHistory=?, patientDescription=?, patientDiagnostic=?   WHERE id=?", (patientID, patientName, patientPhone, patientAge, patientBirthYear, patientHistory, patientFamilyHistory, patientDescription, patientDiagnostic, id))
    conn.commit()
    conn.close()

# connect()
# insert(982,"Hải",98,32,1985,"ko","ko","đẹp trai","giảm bớt đẹp trai")
# print(view())
# update(2,982,"aaa",99,32,1985,"cc","dd","ee ee","ff bớt đẹp trai")
print(view())
