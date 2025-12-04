Project 0ktapus: Phishing Incident Analysis & Simulation
!(https://img.shields.io/badge/Status-Research_Complete-green)

📖 Project Overview
This project provides a comprehensive analysis of the 0ktapus (Scattered Spider) phishing campaign that targeted Twilio, Cloudflare, and 130+ other organizations in 2022. It includes a forensic breakdown of the attack vectors, a strategic impact assessment, and a functional design for a SMS Phishing (Smishing) Simulation to test organizational resilience against similar threats.

📂 Repository Contents
docs/Research_Report.md: The full executive report analyzing the breach mechanics, legal implications, and FIDO2 defense strategies.

simulation/: Python middleware tools designed to integrate GoPhish with the Twilio API for controlled SMS simulation testing.

🛠️ Simulation Architecture
The simulation emulates the 0ktapus tactics by bypassing standard email vectors and delivering payloads via SMS.

Framework: GoPhish (Campaign Management)

Delivery: Twilio Programmable Messaging API

Middleware: Custom Python SMTP-to-SMS bridge

⚠️ Disclaimer
This project is for EDUCATIONAL AND DEFENSIVE PURPOSES ONLY. The simulation tools provided are intended for use by authorized security personnel to test systems they own or have explicit permission to test. Misuse of these tools is illegal. See(DISCLAIMER.md) for full details.
