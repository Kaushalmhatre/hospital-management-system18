import sqlite3
from database import get_connection


# ---------------- PATIENT LOGIN ----------------
def patient_login(email, password):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM patreg WHERE email=? AND password=?",
        (email, password)
    )
    user = cur.fetchone()
    conn.close()
    return user


# ---------------- PATIENT REGISTER ----------------
def patient_register(fname, lname, gender, email, contact, password):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("""
            INSERT INTO patreg (fname, lname, gender, email, contact, password)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (fname, lname, gender, email, contact, password))
        conn.commit()
        conn.close()
        return True   # Registration successful
    except sqlite3.IntegrityError:
        conn.close()
        return False  # Email already exists


# ---------------- DOCTOR LOGIN ----------------
def doctor_login(username, password):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM doctb WHERE username=? AND password=?",
        (username, password)
    )
    user = cur.fetchone()
    conn.close()
    return user


# ---------------- DOCTOR REGISTER ----------------
def doctor_register(username, specialization, password):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("""
            INSERT INTO doctb (username, specialization, password)
            VALUES (?, ?, ?)
        """, (username, specialization, password))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        conn.close()
        return False


# ---------------- ADMIN LOGIN ----------------
def admin_login(username, password):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM admintb WHERE username=? AND password=?",
        (username, password)
    )
    user = cur.fetchone()
    conn.close()
    return user


# ---------------- ADMIN REGISTER ----------------
def admin_register(username, password):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("""
            INSERT INTO admintb (username, password)
            VALUES (?, ?)
        """, (username, password))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        conn.close()
        return False
