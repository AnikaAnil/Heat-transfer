import streamlit as st
from PIL import Image

# Set page title
st.set_page_config(page_title="HEAT TRANSFER MADE FUN")
st.title("🔬 HEAT TRANSFER MADE FUN")

# Step progression
if "step" not in st.session_state:
    st.session_state.step = 0
step = st.session_state.step

# Step 1: Aim
if step == 0:
    st.header("🎯 Aim")
    st.write("""
    The aim of the experiment is to determine the natural convection heat transfer coefficient 
    of a vertical heated tube kept in air, experimentally and by using empirical correlation.
    """)
    if st.button("Next"):
        st.session_state.step = 1
        st.experimental_rerun()

# Step 2: Specifications
elif step == 1:
    st.header("📏 Specifications")
    st.write("""
    - Length of the tube: 0.5 m  
    - Diameter of the tube: 0.05 m  
    - Duct size: 0.2 m x 0.2 m x 0.5 m
    """)
    if st.button("Next"):
        st.session_state.step = 2
        st.experimental_rerun()

# Step 3: Theory and Animation
elif step == 2:
    st.header("📚 Basic Theory")
    st.write("""
    In natural convection, heat transfer occurs due to the movement of fluid caused by density 
    differences resulting from temperature variations. Hot fluid rises, and cold fluid sinks, 
    creating a cycle that facilitates heat transfer.
    """)
    st.subheader("🎞️ Simulation")
    st.image("/mnt/data/natural_convection_demo.jpg", caption="Natural Convection Simulation", use_column_width=True)
    if st.button("Next"):
        st.session_state.step = 3
        st.experimental_rerun()

# Step 4: Observations
elif step == 3:
    st.header("📋 Record Observations")
    time = st.text_input("Time of reading (e.g., 5 min)")
    t_values = []
    for i in range(1, 8):
        t = st.number_input(f"Enter surface temperature T{i} (in °C)", key=f"T{i}")
        t_values.append(t)
    t_ambient = st.number_input("Enter ambient temperature (in °C)", key="T_ambient")

    if st.button("Submit Observations"):
        st.session_state.step = 4
        st.session_state.observations = {
            "time": time,
            **{f"T{i+1}": t_values[i] for i in range(7)},
            "T_ambient": t_ambient
        }
        st.success("Observations saved successfully!")
        st.experimental_rerun()

# Step 5: Summary
elif step == 4:
    st.header("📊 Summary of Observations")
    for key, value in st.session_state.observations.items():
        st.write(f"{key}: {value} °C")

    if st.button("Restart Experiment"):
        st.session_state.step = 0
        st.experimental_rerun()
