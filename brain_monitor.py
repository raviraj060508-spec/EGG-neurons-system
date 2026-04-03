import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
import random

st.set_page_config(page_title="EEG Monitoring System", layout="wide")

# Title
st.title("🧠 EEG Monitoring & Neurological Disorder Detection")
st.write("Prototype system for real-time brain signal monitoring and analysis")

# -----------------------------
# Sidebar Controls
# -----------------------------
st.sidebar.header("Controls")

signal_type = st.sidebar.selectbox(
    "Select Brain Wave Type",
    ["Alpha (Relaxed)", "Beta (Active)", "Theta (Drowsy)", "Delta (Deep Sleep)"]
)

duration = st.sidebar.slider("Signal Duration (seconds)", 5, 20, 10)

# -----------------------------
# Generate EEG Signal
# -----------------------------
def generate_signal(signal_type, duration):
    t = np.linspace(0, duration, 500)

    if "Alpha" in signal_type:
        signal = np.sin(2 * np.pi * 10 * t)
    elif "Beta" in signal_type:
        signal = np.sin(2 * np.pi * 20 * t)
    elif "Theta" in signal_type:
        signal = np.sin(2 * np.pi * 6 * t)
    else:
        signal = np.sin(2 * np.pi * 2 * t)

    noise = np.random.normal(0, 0.5, len(t))
    return t, signal + noise

# -----------------------------
# Display Graph
# -----------------------------
st.subheader("📊 Real-Time EEG Signal")

t, signal = generate_signal(signal_type, duration)

fig, ax = plt.subplots()
ax.plot(t, signal)
ax.set_xlabel("Time")
ax.set_ylabel("Amplitude")
ax.set_title("EEG Signal Simulation")

st.pyplot(fig)

# -----------------------------
# AI-Based Detection (Basic Logic)
# -----------------------------
st.subheader("🤖 AI Analysis")

avg_signal = np.mean(np.abs(signal))

if avg_signal > 1.2:
    result = "⚠️ High Risk of Seizure"
elif avg_signal > 0.8:
    result = "😟 Moderate Stress Level"
else:
    result = "😊 Normal Brain Activity"

st.write("### Result:", result)

# -----------------------------
# Patient Stimuli Simulation
# -----------------------------
st.subheader("⚡ Stimuli Response Test")

if st.button("Apply Stimulus (Light/Sound)"):
    st.write("Stimulus Applied... Analyzing Response...")
    time.sleep(2)

    response = random.choice([
        "Normal Response",
        "Delayed Response",
        "Abnormal Response ⚠️"
    ])

    st.success(f"Response: {response}")

# -----------------------------
# Patient Info Section
# -----------------------------
st.subheader("👤 Patient Info")

name = st.text_input("Enter Patient Name")
age = st.number_input("Enter Age", 1, 100)

if st.button("Save Report"):
    st.success(f"Report saved for {name}")

       
        
