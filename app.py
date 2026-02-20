import streamlit as st

if "name" not in st.session_state:
    st.session_state.name = ""
import streamlit as st
from auth import patient_login, doctor_login, admin_login, patient_register, doctor_register, admin_register
from database import init_db

# ✅ CORRECT IMPORT (singular dashboard)
from dashboard.patient_dashboard import patient_dashboard
from dashboard.admin_dashboard import admin_dashboard

# ---------------- INIT ----------------
st.set_page_config(
    page_title="Hospital Management System",
    layout="wide"
)

init_db()

# ---------------- SESSION INIT ----------------
if "role" not in st.session_state:
    st.session_state.role = None


# ---------------- LOGIN + REGISTRATION PAGE ----------------
def login_page():
    st.title("🏥 Hospital Management System")

    tabs = st.tabs(["👤 Patient", "🩺 Doctor", "🛡️ Admin"])

    # -------- PATIENT --------
    with tabs[0]:
        st.subheader("Patient Login")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Login as Patient"):
            user = patient_login(email, password)
            if user:
                st.session_state.role = "patient"
                st.session_state.pid = user[0]
                st.session_state.fname = user[1]
                st.session_state.lname = user[2]
                st.session_state.gender = user[3]
                st.session_state.email = user[4]
                st.session_state.contact = user[5]
                st.success("Patient login successful")
                st.rerun()
            else:
                st.error("Invalid email or password")

        st.subheader("New Patient Registration")
        fname = st.text_input("First Name")
        lname = st.text_input("Last Name")
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        reg_email = st.text_input("Register Email")
        contact = st.text_input("Contact")
        reg_pass = st.text_input("Register Password", type="password")

        if st.button("Register Patient"):
            success = patient_register(fname, lname, gender, reg_email, contact, reg_pass)
            if success:
                st.success("✅ Registration successful! You can now log in.")
            else:
                st.error("⚠️ Email already exists. Try another.")

    # -------- DOCTOR --------
    with tabs[1]:
        st.subheader("Doctor Login")
        username = st.text_input("Username", key="doc_user")
        password = st.text_input("Password", type="password", key="doc_pass")

        if st.button("Login as Doctor"):
            user = doctor_login(username, password)
            if user:
                st.session_state.role = "doctor"
                st.session_state.doctor = user[0]
                st.success("Doctor login successful")
                st.rerun()
            else:
                st.error("Invalid username or password")

        st.subheader("New Doctor Registration")
        doc_user = st.text_input("New Username", key="new_doc_user")
        specialization = st.text_input("Specialization")
        doc_pass = st.text_input("New Password", type="password", key="new_doc_pass")

        if st.button("Register Doctor"):
            success = doctor_register(doc_user, specialization, doc_pass)
            if success:
                st.success("✅ Registration successful! You can now log in.")
            else:
                st.error("⚠️ Username already exists. Try another.")

    # -------- ADMIN --------
    with tabs[2]:
        st.subheader("Admin Login")
        username = st.text_input("Username", key="admin_user")
        password = st.text_input("Password", type="password", key="admin_pass")

        if st.button("Login as Admin"):
            user = admin_login(username, password)
            if user:
                st.session_state.role = "admin"
                st.success("Admin login successful")
                st.rerun()
            else:
                st.error("Invalid username or password")

        st.subheader("New Admin Registration")
        new_user = st.text_input("New Username", key="new_admin_user")
        new_pass = st.text_input("New Password", type="password", key="new_admin_pass")

        if st.button("Register Admin"):
            success = admin_register(new_user.strip(), new_pass.strip())
            if success:
                st.success("✅ Registration successful! You can now log in.")
            else:
                st.error("⚠️ Username already exists. Try another.")


# ---------------- ROUTING ----------------
def route_app():
    st.sidebar.title("Navigation")

    if st.session_state.role == "patient":
        patient_dashboard()

    elif st.session_state.role == "admin":
        admin_dashboard()

    elif st.session_state.role == "doctor":
        st.info("🩺 Doctor Dashboard – Coming in Phase 4")

    st.sidebar.divider()

    if st.sidebar.button("🚪 Logout"):
        st.session_state.clear()
        st.rerun()


# ---------------- MAIN ----------------
if st.session_state.role is None:
    login_page()
else:
    route_app()
