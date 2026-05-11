# app.py

import streamlit as st
import time

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Mechanical Unit Converter & Density Checker",
    page_icon="⚙️",
    layout="wide"
)

# ---------------- CUSTOM CSS / ANIMATION ---------------- #

st.markdown("""
<style>

body {
    background-color: #0f172a;
}

.main-title {
    font-size: 45px;
    font-weight: bold;
    text-align: center;
    color: #38bdf8;
    animation: glow 2s ease-in-out infinite alternate;
}

@keyframes glow {
    from {
        text-shadow: 0 0 10px #38bdf8;
    }
    to {
        text-shadow: 0 0 25px #0ea5e9;
    }
}

.student-box {
    background: linear-gradient(135deg, #1e293b, #0f172a);
    padding: 20px;
    border-radius: 15px;
    color: white;
    border: 2px solid #38bdf8;
    margin-bottom: 20px;
    animation: float 3s ease-in-out infinite;
}

@keyframes float {
    0% {transform: translateY(0px);}
    50% {transform: translateY(-5px);}
    100% {transform: translateY(0px);}
}

.result-box {
    background-color: #1d4ed8;
    padding: 15px;
    border-radius: 12px;
    color: white;
    font-size: 24px;
    font-weight: bold;
    text-align: center;
    animation: pulse 1.5s infinite;
}

@keyframes pulse {
    0% {transform: scale(1);}
    50% {transform: scale(1.03);}
    100% {transform: scale(1);}
}

.footer {
    text-align:center;
    color:gray;
    margin-top:40px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #

st.markdown(
    "<div class='main-title'>⚙️ Mechanical Unit Converter & Material Density Checker ⚙️</div>",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- STUDENT INFO ---------------- #

st.markdown(f"""
<div class='student-box'>
<h3>👨‍🎓 Student Information</h3>
<h4>Full Name: Muhammad Abdullah</h4>
<h4>Roll Number: 25-ME-51</h4>
</div>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("⚙️ Navigation")

option = st.sidebar.radio(
    "Choose Feature",
    ["Unit Converter", "Material Density Checker"]
)

# ---------------- UNIT CONVERTER ---------------- #

if option == "Unit Converter":

    st.header("🔄 Engineering Unit Converter")

    category = st.selectbox(
        "Select Unit System",
        ["Length", "Pressure", "Temperature", "Density"]
    )

    # ---------- LENGTH ---------- #

    if category == "Length":

        value = st.number_input("Enter Length Value", value=0.0)

        from_unit = st.selectbox(
            "From Unit",
            ["Meter", "Centimeter", "Millimeter", "Foot (ft)", "Inch"]
        )

        to_unit = st.selectbox(
            "To Unit",
            ["Meter", "Centimeter", "Millimeter", "Foot (ft)", "Inch"]
        )

        conversion_to_meter = {
            "Meter": 1,
            "Centimeter": 0.01,
            "Millimeter": 0.001,
            "Foot (ft)": 0.3048,
            "Inch": 0.0254
        }

        meter_value = value * conversion_to_meter[from_unit]
        result = meter_value / conversion_to_meter[to_unit]

        progress = st.progress(0)

        for i in range(100):
            time.sleep(0.005)
            progress.progress(i + 1)

        st.markdown(
            f"<div class='result-box'>Converted Value = {result:.4f} {to_unit}</div>",
            unsafe_allow_html=True
        )

    # ---------- PRESSURE ---------- #

    elif category == "Pressure":

        value = st.number_input("Enter Pressure Value", value=0.0)

        from_unit = st.selectbox(
            "From Pressure Unit",
            ["Pascal", "kPa", "Bar", "psi"]
        )

        to_unit = st.selectbox(
            "To Pressure Unit",
            ["Pascal", "kPa", "Bar", "psi"]
        )

        conversion_to_pascal = {
            "Pascal": 1,
            "kPa": 1000,
            "Bar": 100000,
            "psi": 6894.76
        }

        pascal_value = value * conversion_to_pascal[from_unit]
        result = pascal_value / conversion_to_pascal[to_unit]

        progress = st.progress(0)

        for i in range(100):
            time.sleep(0.005)
            progress.progress(i + 1)

        st.markdown(
            f"<div class='result-box'>Converted Pressure = {result:.4f} {to_unit}</div>",
            unsafe_allow_html=True
        )

    # ---------- TEMPERATURE ---------- #

    elif category == "Temperature":

        value = st.number_input("Enter Temperature", value=0.0)

        from_unit = st.selectbox(
            "From Temperature Unit",
            ["Celsius", "Fahrenheit", "Kelvin"]
        )

        to_unit = st.selectbox(
            "To Temperature Unit",
            ["Celsius", "Fahrenheit", "Kelvin"]
        )

        # Convert to Celsius
        if from_unit == "Celsius":
            celsius = value

        elif from_unit == "Fahrenheit":
            celsius = (value - 32) * 5 / 9

        else:
            celsius = value - 273.15

        # Convert from Celsius
        if to_unit == "Celsius":
            result = celsius

        elif to_unit == "Fahrenheit":
            result = (celsius * 9 / 5) + 32

        else:
            result = celsius + 273.15

        progress = st.progress(0)

        for i in range(100):
            time.sleep(0.005)
            progress.progress(i + 1)

        st.markdown(
            f"<div class='result-box'>Converted Temperature = {result:.2f} {to_unit}</div>",
            unsafe_allow_html=True
        )

    # ---------- DENSITY ---------- #

    elif category == "Density":

        value = st.number_input("Enter Density Value", value=0.0)

        from_unit = st.selectbox(
            "From Density Unit",
            ["kg/m³", "g/cm³"]
        )

        to_unit = st.selectbox(
            "To Density Unit",
            ["kg/m³", "g/cm³"]
        )

        # Convert to kg/m³
        if from_unit == "kg/m³":
            density = value
        else:
            density = value * 1000

        # Convert to target
        if to_unit == "kg/m³":
            result = density
        else:
            result = density / 1000

        progress = st.progress(0)

        for i in range(100):
            time.sleep(0.005)
            progress.progress(i + 1)

        st.markdown(
            f"<div class='result-box'>Converted Density = {result:.4f} {to_unit}</div>",
            unsafe_allow_html=True
        )

# ---------------- MATERIAL DENSITY CHECKER ---------------- #

elif option == "Material Density Checker":

    st.header("🧱 Material Density Checker")

    materials = {
        "Steel": 7850,
        "Aluminum": 2700,
        "Copper": 8960,
        "Brass": 8500,
        "Titanium": 4500,
        "Cast Iron": 7200
    }

    material = st.selectbox(
        "Select Material",
        list(materials.keys())
    )

    density = materials[material]

    st.markdown(
        f"<div class='result-box'>{material} Density = {density} kg/m³</div>",
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # Density Classification

    if density > 8000:
        st.success("🔴 HIGH Density Material")

    elif density > 5000:
        st.warning("🟡 MEDIUM Density Material")

    else:
        st.info("🟢 LOW Density Material")

    # Animated Progress Bar

    st.subheader("Density Visualization")

    density_percentage = min(int((density / 10000) * 100), 100)

    progress = st.progress(0)

    for i in range(density_percentage):
        time.sleep(0.01)
        progress.progress(i + 1)

# ---------------- FOOTER ---------------- #

st.markdown("""
<div class='footer'>
🚀 Developed using Streamlit Cloud + GitHub <br>
⚙️ Mechanical Engineering Project
</div>
""", unsafe_allow_html=True)
