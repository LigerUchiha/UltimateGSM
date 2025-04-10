# UltimateGSM & OSINT Engine

A powerful suite of tools for GSM cracking and advanced OSINT collection. This repository contains several modules that work together for **SIM exploitation**, **A5/1 cracking**, **GPS spoofing**, and **advanced OSINT** operations.

## Features

1. **SIM Exploit Module**:
   - Brute-forces PIN on a smartcard.
   - Extracts basic information like ICCID and IMSI.

2. **A5/1 Cracking Module**:
   - Utilizes Kraken to recover A5/1 encryption keys.
   - Decrypts intercepted GSM traffic.

3. **Geo Spoofing Module**:
   - Simulates fake GPS coordinates.
   - Allows for custom GPS coordinate input.
   - Looks up real IP-based geolocation.

4. **OSINT Engine**:
   - Reverse email lookup using Hunter.io.
   - Reverse phone lookup using TrueCaller.
   - Reverse IP lookup using IPinfo.io.

## Installation

### Requirements

- Python 3.x
- Dependencies: Install via `requirements.txt`

```bash
pip install -r requirements.txt
Setup
Clone the repository:

bash
Copy code
git clone https://github.com/LigerUchiha/UltimateGSM.git
cd UltimateGSM
Download or generate the Kraken rainbow tables and place them in the data/rainbow_tables/ directory.

Install the necessary Python libraries:

bash
pip install -r requirements.txt
Run the script:

bash
Copy code
python run.py
Usage
SIM Exploit
bash
python run.py --sim-exploit
This will attempt to brute-force the SIM PIN and extract basic information.

A5/1 Cracking
bash
python run.py --a5-crack
This will run the Kraken tool against a captured GSM stream to recover the encryption key and decrypt the traffic.

Geo Spoofing
bash

python run.py --geo-spoof
Generate fake GPS coordinates or spoof a specific location.

OSINT Engine
bash
python run.py --osint-engine <email|phone|ip>
Run OSINT lookups on an email, phone number, or IP address.

Example
For phone number lookup:


Author:Liger Uchiha
Copy code
python run.py --osint-engine +1234567890
Authors
Your Name 
