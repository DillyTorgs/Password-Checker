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
   
## 🚀 Usage
When you run the script, you'll be prompted to enter a password to check:

  ```bash
$ python password_tool.py
=== Password Security Tool ===
Enter password to test: MyP@ssw0rd123!

Strength: Strong
Entropy: 78.58 bits

**If the password is weak or moderate, you'll receive suggestions and some secure alternatives:**

 ```bash
Strength: Weak
Entropy: 25.76 bits
Suggestions:
 - Use at least 12 characters (yours is 8).
 - Add special symbols.

Try one of these:
Random: U#e%zP2$Q8!tW3^b
Passphrase: bravo-uniform-zulu-sierra

## 📂 Project Structure
 ```bash

password_tool.py   # Main script
README.md          # Documentation

📊 Entropy Calculation
Entropy is calculated as:

```bash
Entropy = length_of_password × log2(possible_characters)

Where:

Lowercase letters: 26 possible chars

Uppercase letters: 26 possible chars

Numbers: 10 possible chars

Symbols: 32 possible chars (from string.punctuation)

Higher entropy = more randomness = harder to crack.

🌐 Breach Checking
This tool never sends your password in full.
It:

Hashes your password with SHA-1.

Sends only the first 5 characters of the hash to the HaveIBeenPwned API.

Compares the returned list of matching hashes locally.

📄 License
This project is licensed under the MIT License.
Feel free to use, modify, and distribute.

⚠️ Disclaimer
This tool is for educational and personal security purposes.
Never enter real passwords you currently use unless you trust your environment.

🤝 Contributing
Pull requests are welcome!
For major changes, open an issue first to discuss what you'd like to change.









