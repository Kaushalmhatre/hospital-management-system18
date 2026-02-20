import sqlite3

# Database Name
DB_NAME = "hospital.db"

# ---------------- CONNECTION ----------------
def get_connection():
    return sqlite3.connect(DB_NAME, check_same_thread=False)


# ---------------- CREATE TABLES ----------------
def create_tables():
    conn = get_connection()
    cur = conn.cursor()

    # ---------------- ADMIN TABLE ----------------
    cur.execute("""
    CREATE TABLE IF NOT EXISTS admintb (
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL
    )
    """)

    # ---------------- DOCTOR TABLE ----------------
    cur.execute("""
    CREATE TABLE IF NOT EXISTS doctb (
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL,
        email TEXT NOT NULL,
        spec TEXT NOT NULL,
        docFees INTEGER NOT NULL
    )
    """)

    # ---------------- PATIENT REGISTRATION ----------------
    cur.execute("""
    CREATE TABLE IF NOT EXISTS patreg (
        pid INTEGER PRIMARY KEY AUTOINCREMENT,
        fname TEXT NOT NULL,
        lname TEXT NOT NULL,
        gender TEXT NOT NULL,
        email TEXT NOT NULL,
        contact TEXT NOT NULL,
        password TEXT NOT NULL
    )
    """)

    # ---------------- APPOINTMENTS ----------------
    cur.execute("""
    CREATE TABLE IF NOT EXISTS appointmenttb (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        pid INTEGER NOT NULL,
        fname TEXT NOT NULL,
        lname TEXT NOT NULL,
        gender TEXT NOT NULL,
        email TEXT NOT NULL,
        contact TEXT NOT NULL,
        doctor TEXT NOT NULL,
        docFees INTEGER NOT NULL,
        appdate TEXT NOT NULL,
        apptime TEXT NOT NULL,
        userStatus INTEGER NOT NULL,
        doctorStatus INTEGER NOT NULL
    )
    """)

    # ---------------- PRESCRIPTION ----------------
    cur.execute("""
    CREATE TABLE IF NOT EXISTS prestb (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        doctor TEXT NOT NULL,
        pid INTEGER NOT NULL,
        fname TEXT NOT NULL,
        lname TEXT NOT NULL,
        appdate TEXT NOT NULL,
        apptime TEXT NOT NULL,
        disease TEXT NOT NULL,
        allergy TEXT NOT NULL,
        prescription TEXT NOT NULL
    )
    """)

    # ---------------- CONTACT ----------------
    cur.execute("""
    CREATE TABLE IF NOT EXISTS contact (
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        contact TEXT NOT NULL,
        message TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


# ---------------- SEED DATA ----------------
def seed_data():
    conn = get_connection()
    cur = conn.cursor()

    # Admin
    cur.execute(
        "INSERT OR IGNORE INTO admintb VALUES (?, ?)",
        ("admin", "admin123")
    )

    # Doctors
    doctors = [
        ("ashok", "ashok123", "ashok@gmail.com", "General", 500),
        ("arun", "arun123", "arun@gmail.com", "Cardiologist", 600),
        ("Dinesh", "dinesh123", "dinesh@gmail.com", "General", 700),
        ("Ganesh", "ganesh123", "ganesh@gmail.com", "Pediatrician", 550),
        ("Kumar", "kumar123", "kumar@gmail.com", "Pediatrician", 800),
        ("Amit", "amit123", "amit@gmail.com", "Cardiologist", 1000),
        ("Abbis", "abbis123", "abbis@gmail.com", "Neurologist", 1500),
        ("Tiwary", "tiwary123", "tiwary@gmail.com", "Pediatrician", 450)
    ]

    cur.executemany("""
    INSERT OR IGNORE INTO doctb VALUES (?, ?, ?, ?, ?)
    """, doctors)

    conn.commit()
    conn.close()


# ---------------- INIT DB ----------------
def init_db():
    create_tables()
    seed_data()
