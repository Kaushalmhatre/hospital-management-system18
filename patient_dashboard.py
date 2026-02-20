import streamlit as st
from services import *
from datetime import date


def patient_dashboard():
    st.header(f"👤 Welcome {st.session_state.name}")

    menu = st.sidebar.radio(
        "Menu",
        ["Dashboard", "Book Appointment", "My Appointments", "Prescriptions"]
    )

    # -------- DASHBOARD --------
    if menu == "Dashboard":
        st.info("Use sidebar to manage appointments")

    # -------- BOOK APPOINTMENT --------
    if menu == "Book Appointment":
        doctors = get_doctors()
        doc_map = {d[0]: d for d in doctors}

        spec = st.selectbox("Specialization", sorted(set(d[1] for d in doctors)))
        filtered = [d[0] for d in doctors if d[1] == spec]

        doctor = st.selectbox("Doctor", filtered)
        fees = doc_map[doctor][2]

        st.text_input("Fees", fees, disabled=True)
        appdate = st.date_input("Date", min_value=date.today())
        apptime = st.selectbox("Time", ["08:00", "10:00", "12:00", "14:00", "16:00"])

        if st.button("Book Appointment"):
            book_appointment((
                st.session_state.pid,
                st.session_state.fname,
                st.session_state.lname,
                st.session_state.gender,
                st.session_state.email,
                st.session_state.contact,
                doctor,
                fees,
                str(appdate),
                apptime
            ))
            st.success("Appointment Booked")

    # -------- MY APPOINTMENTS --------
    # -------- MY APPOINTMENTS --------

    if menu == "My Appointments":
        rows = get_patient_appointments(
            st.session_state.fname,
            st.session_state.lname
        )

        for r in rows:
            st.write(r)

            if r[5] == 1 and st.button(f"Cancel {r[0]}"):
                cancel_appointment(r[0])
                st.warning("Appointment Cancelled")

