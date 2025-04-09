# 🛡️ AI-Driven Cyber Threat Simulation and Detection

This project is a prototype system that simulates cyberattacks using AI and detects them using anomaly detection models trained on **normal network traffic**.

## 📌 Objective
To build an intelligent detection pipeline using:
- **Autoencoder**: Learns to reconstruct normal traffic. Anomalies (attacks) cause high reconstruction error.
- **LSTM Autoencoder**: Captures temporal network patterns for sequential anomaly detection.
- **GAN (Generative Adversarial Network)**: Synthesizes fake attack samples to stress-test the detection models.

