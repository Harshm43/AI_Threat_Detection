import streamlit as st

st.set_page_config(page_title="AI Threat Detection Dashboard", layout="wide")

st.title("🛡️ AI–Driven Cyber Threat Simulation and Detection")
st.markdown("""
This prototype uses Autoencoders and LSTMs trained on normal traffic to detect cyber anomalies in network data.  
Use the sidebar to select models and view results.
""")

# Example section
st.header("🔍 Model Summary")
st.write("This is a placeholder. You can add visualizations, model stats, or upload data.")

# Sidebar controls
with st.sidebar:
    st.header('Options')
    model_choice = st.selectbox("Select Model", ['Autoencoder', 'LSTM'])
    threshold = st.slider("Anomaly Threshold", 0.0, 0.1, 0.03)

# Output selected option
st.write(f"Selected model: **{model_choice}** with threshold **{threshold:.2f}**")
