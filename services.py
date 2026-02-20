import sqlite3
from database import get_connection
from datetime import datetime


# ---------------- DOCTORS ----------------

def get_doctors():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT username, spec, docFees FROM doctb")
    data = cur.fetchall()
    conn.close()
    return data


def add_doctor(name, password, email, spec, fees):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO doctb (username, password, email, spec, docFees) VALUES (?, ?, ?, ?, ?)",
        (name, password, email, spec, fees)
    )
    conn.commit()
    conn.close()


def delete_doctor(email):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM doctb WHERE email=?", (email,))
    conn.commit()
    conn.close()


# ---------------- APPOINTMENTS ----------------

def book_appointment(data):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO appointmenttb
        (pid, fname, lname, gender, email, contact, doctor, docFees, appdate, apptime, userStatus, doctorStatus)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1, 1)
    """, data)

    conn.commit()
    conn.close()


def get_patient_appointments(fname, lname):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT ID, doctor, docFees, appdate, apptime, userStatus, doctorStatus
        FROM appointmenttb
        WHERE fname=? AND lname=?
    """, (fname, lname))
    rows = cur.fetchall()
    conn.close()
    return rows


def cancel_appointment(app_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE appointmenttb SET userStatus=0 WHERE ID=?", (app_id,))
    conn.commit()
    conn.close()


# ---------------- PRESCRIPTIONS ----------------

def get_prescriptions(pid):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT doctor, ID, appdate, apptime, disease, allergy, prescription
        FROM prestb WHERE pid=?
    """, (pid,))
    rows = cur.fetchall()
    conn.close()
    return rows


# ---------------- ADMIN DATA ----------------

def get_all_appointments():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM appointmenttb")
    rows = cur.fetchall()
    conn.close()
    return rows


def get_all_patients():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM patreg")
    rows = cur.fetchall()
    conn.close()
    return rows


def get_all_prescriptions():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM prestb")
    rows = cur.fetchall()
    conn.close()
    return rows
