import string
import secrets
import hashlib
import math
import random
import requests


# -------------------------------
# Calculate how random a password is
# -------------------------------
def get_entropy(pwd):
    """Return password entropy in bits."""
    possible_chars = 0
    if any(ch.islower() for ch in pwd):
        possible_chars += 26
    if any(ch.isupper() for ch in pwd):
        possible_chars += 26
    if any(ch.isdigit() for ch in pwd):
        possible_chars += 10
    if any(ch in string.punctuation for ch in pwd):
        possible_chars += len(string.punctuation)

    if possible_chars == 0:
        return 0

    return round(len(pwd) * math.log2(possible_chars), 2)


# -------------------------------
# Check password against breach database
# -------------------------------
def is_pwned(pwd):
    """Use HaveIBeenPwned's k-anonymity API to see if password appears in breaches."""
    sha1_hash = hashlib.sha1(pwd.encode("utf-8")).hexdigest().upper()
    first5, tail = sha1_hash[:5], sha1_hash[5:]

    try:
        res = requests.get(f"https://api.pwnedpasswords.com/range/{first5}", timeout=5)
        if res.status_code != 200:
            return False, None

        for entry in res.text.splitlines():
            h_suffix, count = entry.split(":")
            if h_suffix == tail:
                return True, int(count)
    except requests.RequestException:
        return False, None

    return False, None


# -------------------------------
# Create strong passwords
# -------------------------------
def random_password(length=16):
    """Make a random password using letters, digits, and symbols."""
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(chars) for _ in range(length))


def passphrase(num_words=4):
    """Make a passphrase from a mini wordlist."""
    words = [
        "alpha", "bravo", "charlie", "delta", "echo", "foxtrot",
        "golf", "hotel", "india", "juliet", "kilo", "lima",
        "mike", "november", "oscar", "papa", "quebec", "romeo",
        "sierra", "tango", "uniform", "victor", "whiskey", "xray", "yankee", "zulu"
    ]
    return "-".join(random.sample(words, num_words))


# -------------------------------
# Main password check
# -------------------------------
def evaluate_password(pwd):
    """Return strength label, feedback list, and entropy score."""
    tips = []

    # Length
    if len(pwd) < 12:
        tips.append(f"Use at least 12 characters (yours is {len(pwd)}).")

    # Variety
    if not any(ch.isupper() for ch in pwd):
        tips.append("Add uppercase letters.")
    if not any(ch.islower() for ch in pwd):
        tips.append("Add lowercase letters.")
    if not any(ch.isdigit() for ch in pwd):
        tips.append("Add numbers.")
    if not any(ch in string.punctuation for ch in pwd):
        tips.append("Add special symbols.")

    # Obvious passwords
    if pwd.lower() in {"password", "123456", "qwerty", "abc123"}:
        tips.append("Avoid common passwords.")

    # Breach check
    breached, count = is_pwned(pwd)
    if breached:
        tips.append(f"Found in {count} breaches — pick something else.")

    # Entropy
    entropy_bits = get_entropy(pwd)

    # Strength
    if tips:
        if breached or entropy_bits < 36:
            label = "Weak"
        else:
            label = "Moderate"
    else:
        label = "Strong"

    return label, tips, entropy_bits


# -------------------------------
# Run program
# -------------------------------
def main():
    print("=== Password Security Tool ===")
    user_pwd = input("Enter password to test: ")

    label, tips, entropy_bits = evaluate_password(user_pwd)

    print(f"\nStrength: {label}")
    print(f"Entropy: {entropy_bits} bits")

    if tips:
        print("Suggestions:")
        for t in tips:
            print(f" - {t}")

    if label != "Strong":
        print("\nTry one of these:")
        print(f"Random: {random_password(16)}")
        print(f"Passphrase: {passphrase(4)}")


if __name__ == "__main__":
    main()