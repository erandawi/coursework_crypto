# AffineCipher Class - Full Code Explanation

This document explains the `AffineCipher` class step-by-step, mapping each section of the code to its corresponding functionality and Streamlit interface integration.

---

## 🔐 What is the Affine Cipher?

The Affine Cipher is a type of monoalphabetic substitution cipher based on a simple mathematical formula:

* **Encryption:** $E(x) = (a \cdot x + b) \mod 26$
* **Decryption:** $D(y) = a_{inv} \cdot (y - b) \mod 26$

Where:

* `a` = multiplicative key (must be coprime with 26)
* `b` = additive key
* `a_inv` = modular inverse of `a` modulo 26
* `x` = position of plaintext letter
* `y` = position of ciphertext letter

---

## 📦 Code Breakdown

### 1. `__init__(self, a, b)`

**Purpose:** Initialize the cipher with keys `a` and `b`.

```python
if self.gcd(a, 26) != 1:
    raise ValueError("Multiplicative key 'a' must be coprime with 26.")
```

* Checks if `a` is valid (i.e., coprime with 26).

```python
self.a = a
self.b = b
self.a_inv = self.modinv(a, 26)
```

* Stores the keys and calculates modular inverse of `a`.

🔁 **Streamlit Subtask Mapping:**

```python
a = st.number_input("Multiplicative Key (a)", min_value=1, max_value=25)
b = st.number_input("Additive Key (b)", min_value=0, max_value=25)
```

---

### 2. `gcd(self, a, b)`

**Purpose:** Compute greatest common divisor (Euclidean algorithm).

```python
while b:
    a, b = b, a % b
return a
```

* Used to validate if `a` is coprime with 26.

---

### 3. `modinv(self, a, m)`

**Purpose:** Compute modular inverse of `a` mod `m`.

```python
for i in range(1, m):
    if (a * i) % m == 1:
        return i
```

* Brute-force method to find modular inverse.
* Raises error if none exists.

---

### 4. `encrypt(self, plaintext)`

**Purpose:** Encrypt the input text.

```python
for char in plaintext:
    if char.isalpha():
        x = ord(char.lower()) - ord('a')
        enc = (self.a * x + self.b) % 26
        ciphertext += chr(enc + ord('a'))
```

* Converts each character to a 0–25 index.
* Applies the affine encryption formula.
* Keeps non-alphabetic characters unchanged.

🔁 **Streamlit Subtask Mapping:**

```python
word = st.text_input("Enter a word to encrypt/decrypt")
cipher = AffineCipher(a, b)
encrypted = cipher.encrypt(word)
```

---

### 5. `decrypt(self, ciphertext)`

**Purpose:** Decrypt the encrypted text.

```python
for char in ciphertext:
    if char.isalpha():
        y = ord(char.lower()) - ord('a')
        dec = (self.a_inv * (y - self.b)) % 26
        plaintext += chr(dec + ord('a'))
```

* Applies the affine decryption formula.
* Uses the precomputed `a_inv`.

🔁 **Streamlit Subtask Mapping:**

```python
decrypted = cipher.decrypt(encrypted)
```

---

## ✅ Summary

The `AffineCipher` class handles both encryption and decryption of text using a classical mathematical transformation. It enforces the requirement that `a` must be coprime with 26 and provides educational insight into how classical substitution ciphers work.

Use this alongside a Streamlit app for interactive demos in classrooms, exams, or crypto tutorials.
