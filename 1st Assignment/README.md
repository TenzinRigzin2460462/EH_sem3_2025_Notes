
# 🛡️ Ethical Hacking Assignment 1 – TCP and UDP Port Discovery

**Assigned to:** SankaraNarayananS18  
**Target:** `scanme.nmap.org`  
**Tool Used:** Nmap / Zenmap  
**Submission Directory:** `EH_sem3_2025_Notes/1st Assignment`  
**Report Type:** One-page README with screenshot

---

## 🎯 Objective

To scan both **TCP and UDP ports** of the target website `scanme.nmap.org` using **Nmap**, identify open ports and running services, and explain the difference between **TCP and UDP** protocols through real-world testing.

---

## 🧭 Step-by-Step Guide

> You can use **Zenmap GUI** (Nmap’s graphical interface) on **Windows or Linux**.

### 🖥️ Step 1: Open Zenmap
- Install Nmap (includes Zenmap) from: [https://nmap.org/download.html](https://nmap.org/download.html)
- Open **Zenmap** on your system

### 🔍 Step 2: Set Scan Details
- **Target:** `scanme.nmap.org`
- **Command:**  
  ```
  nmap -sS -sU -T4 -v scanme.nmap.org
  ```

### 🚀 Step 3: Run the Scan
- Click **Scan** and wait for results to load (this may take a few minutes)

### 💾 Step 4: Save the Results
- After scan is complete:
  - Click `Profile → Save Scan`
  - Save it as `scan-results.txt` (optional for records)

### 🖼️ Step 5: Screenshot and Upload
- Take a screenshot of the Zenmap scan result screen
- Name it `screenshot.png`
- Upload `screenshot.png` along with this `README.md` in the assignment folder

---

## 🔧 Nmap Command Breakdown

```bash
nmap -sS -sU -T4 -v scanme.nmap.org
```

| Flag   | Description                        |
|--------|------------------------------------|
| `-sS`  | TCP SYN scan (fast, stealthy)      |
| `-sU`  | UDP scan                           |
| `-T4`  | Aggressive timing (faster scan)    |
| `-v`   | Verbose output                     |

---

## 🔍 Findings (Sample)

The scan revealed the following open ports and services:

| Protocol | Port | Service      |
|----------|------|--------------|
| TCP      | 22   | SSH          |
| TCP      | 80   | HTTP         |
| UDP      | 123  | NTP (likely) |
| UDP      | 161  | SNMP (likely)|

> Actual output may vary slightly based on timing and version.

---

## 🔁 TCP vs UDP – Comparison Table

| Feature          | TCP (Transmission Control Protocol) | UDP (User Datagram Protocol)      |
|------------------|--------------------------------------|-----------------------------------|
| Connection       | Yes (connection-oriented)            | No (connectionless)               |
| Speed            | Slower (handshaking involved)        | Faster (no handshaking)           |
| Reliability      | High (guarantees delivery)           | Low (no guarantee of delivery)    |
| Use Cases        | Web, Email, SSH                      | Streaming, DNS, VoIP              |
| Communication    | Two-way (acknowledged)               | One-way (fire-and-forget)         |

**TCP is like a phone call** – confirmed delivery and two-way.  
**UDP is like shouting** – fast but you don’t know if it reached.

---

## 🖼️ Screenshot of Scan

> Upload the screenshot file as `screenshot.png` to your GitHub folder.

![Scan Screenshot](./screenshot.png)

---

## ✅ Submission Checklist

- [x] Scanned both TCP and UDP ports on `scanme.nmap.org`
- [x] Saved scan output (optional)
- [x] Added screenshot as `screenshot.png`
- [x] Explained TCP vs UDP clearly
- [x] Uploaded all to GitHub under correct directory

---

## 📘 Notes

- This scan was performed on a **safe, authorized target**
- Never scan domains you don’t have permission to test
- For this assignment, you are acting as a **Security Analyst**

---
