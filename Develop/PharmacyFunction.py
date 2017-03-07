import sqlite3


def connect():
    conn = sqlite3.connect("pharmacy.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS pharmacy (id INTEGER PRIMARY KEY, medicineCode TEXT, medicineName TEXT, medicineActiveElement TEXT, medicineUnit TEXT, medicineInventory INTEGER)")
    conn.commit()
    conn.close()


def insert(medicineCode, medicineName, medicineActiveElement, medicineUnit, medicineInventory):
    conn = sqlite3.connect("pharmacy.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO pharmacy VALUES (null,?,?,?,?,?)", (medicineCode, medicineName, medicineActiveElement, medicineUnit, medicineInventory))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("pharmacy.db")
    cur = conn.cursor()
    cur.execute("SELECT * from pharmacy")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(medicineCode="", medicineName="", medicineActiveElement="", medicineUnit="", medicineInventory=""):
    conn = sqlite3.connect("pharmacy.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM pharmacy WHERE medicineCode=? OR medicineName=? OR medicineActiveElement=? or medicineUnit=? OR medicineInventory=?", (medicineCode, medicineName, medicineActiveElement, medicineUnit, medicineInventory))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("pharmacy.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM pharmacy WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update(id, medicineCode, medicineName, medicineActiveElement, medicineUnit, medicineInventory):
    conn = sqlite3.connect("pharmacy.db")
    cur = conn.cursor()
    cur.execute("UPDATE pharmacy SET medicineCode=?, medicineName=?, medicineActiveElement=?, medicineUnit=?, medicineInventory=? WHERE id=?", (medicineCode, medicineName, medicineActiveElement, medicineUnit, medicineInventory, id))
    conn.commit()
    conn.close()

# connect()
# insert("BB", "234", "Tiêu 234234", "2234", 200)
# print(view())
# update(2,"bb","cc","dd","ee",999)
print(view())
