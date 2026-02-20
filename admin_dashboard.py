import streamlit as st
from services import *


def admin_dashboard():
    st.header("🛡️ Admin / Receptionist Panel")

    menu = st.sidebar.radio(
        "Menu",
        ["Doctors", "Patients", "Appointments", "Prescriptions", "Add Doctor", "Delete Doctor"]
    )

    if menu == "Doctors":
        st.table(get_doctors())

    if menu == "Patients":
        st.table(get_all_patients())

    if menu == "Appointments":
        st.table(get_all_appointments())

    if menu == "Prescriptions":
        st.table(get_all_prescriptions())

    if menu == "Add Doctor":
        name = st.text_input("Doctor Name")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        spec = st.selectbox("Specialization", ["General", "Cardio", "Neuro", "Pediatric"])
        fees = st.number_input("Fees")

        if st.button("Add Doctor"):
            add_doctor(name, password, email, spec, fees)
            st.success("Doctor Added")

    if menu == "Delete Doctor":
        email = st.text_input("Doctor Email")
        if st.button("Delete"):
            delete_doctor(email)
            st.warning("Doctor Removed")
