# 🔐 Password Security Tool

A Python-based command-line utility for **checking password strength**, **detecting compromised passwords** via HaveIBeenPwned, and **generating strong passwords** or passphrases.

---

## 📜 Features
- **Password Strength Analysis**
  - Checks length, character variety, and common patterns.
  - Calculates **entropy** (measure of randomness) in bits.
- **Breach Database Lookup**
  - Uses the [HaveIBeenPwned](https://haveibeenpwned.com/Passwords) API with **k-anonymity** to protect your password.
- **Password Generation**
  - Secure random passwords with letters, digits, and symbols.
  - Easy-to-remember passphrases using a NATO phonetic-style word list.
- **Actionable Feedback**
  - Suggests improvements for weak or moderate passwords.

---

## 🛠 Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/yourusername/password-security-tool.git
   cd password-security-tool


2. **Install dependncies**
   ```bash
   pip install requests

3. **Run the Tool**
   ```bash
   python password_tool.py
---
   ## 🚀 Usage
1. **When you run the script, you'll be prompted to enter a password to check:**
 
   ```bash
$ python password_tool.py
=== Password Security Tool ===
Enter password to test: MyP@ssw0rd123!
Strength: Strong
Entropy: 78.58 bits
---
2. **Weak or moderate passwords will get:**                                       

















