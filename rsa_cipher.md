# RSACipher Class - Full Code Explanation

This document explains the `RSACipher` class step-by-step, mapping each section of the code to its functionality, and how it can integrate into a Streamlit UI.

---

## 🔐 What is RSA?

RSA is a **public key cryptographic algorithm** based on number theory, particularly large prime numbers. It uses two keys:

* **Public Key (e, n)**: Used for encryption.
* **Private Key (d, n)**: Used for decryption.

It is secure due to the difficulty of factoring large numbers.

### RSA Key Components:

* `p`, `q`: Two large prime numbers.
* `n = p * q`: The modulus for both public and private keys.
* `phi = (p - 1) * (q - 1)`: Euler's totient function.
* `e`: Public exponent (chosen such that `gcd(e, phi) = 1`).
* `d`: Private exponent (modular inverse of `e mod phi`).

Encryption:

```
c = m^e mod n
```

Decryption:

```
m = c^d mod n
```

---

## 📦 Code Breakdown

### 1. `__init__(self, p, q, e)`

**Purpose:** Initialize RSA parameters and compute public and private keys.

```python
if not self.is_prime(p) or not self.is_prime(q):
    raise ValueError("Both p and q must be prime.")
```

* Checks validity of prime numbers `p` and `q`.

```python
self.n = p * q
self.phi = (p - 1) * (q - 1)
```

* Calculates `n` and Euler's totient `phi`.

```python
if self.gcd(e, self.phi) != 1:
    raise ValueError("e must be coprime to phi(n).")
```

* Ensures `e` is coprime with `phi`.

```python
self.d = self.modinv(e, self.phi)
```

* Computes `d`, the modular inverse of `e mod phi`.

🔁 **Streamlit Subtask Mapping:**

```python
p = st.number_input("Prime p")
q = st.number_input("Prime q")
e = st.number_input("Public exponent e")
cipher = RSACipher(p, q, e)
```

---

### 2. `is_prime(self, num)`

**Purpose:** Check if a number is prime.

```python
for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        return False
```

* Basic primality test.

---

### 3. `gcd(self, a, b)`

**Purpose:** Compute greatest common divisor using Euclidean algorithm.

```python
while b:
    a, b = b, a % b
return a
```

---

### 4. `modinv(self, a, m)`

**Purpose:** Compute modular inverse of `a mod m`.

```python
for i in range(1, m):
    if (a * i) % m == 1:
        return i
```

* Brute-force method to find `d` such that `(e * d) % phi = 1`.

---

### 5. `encrypt(self, binary_str)`

**Purpose:** Encrypt a binary string using RSA.

```python
m = int(binary_str, 2)
c = pow(m, self.e, self.n)
```

* Converts binary input to integer.
* Applies RSA encryption formula.

🔁 **Streamlit Subtask Mapping:**

```python
binary = st.text_input("Enter binary to encrypt")
encrypted = cipher.encrypt(binary)
```

---

### 6. `decrypt(self, c)`

**Purpose:** Decrypt an integer using RSA.

```python
m = pow(c, self.d, self.n)
return format(m, '08b')
```

* Applies RSA decryption formula.
* Converts result back to binary string.

🔁 **Streamlit Subtask Mapping:**

```python
decrypted = cipher.decrypt(encrypted)
```

---

## ✅ Summary

The `RSACipher` class provides a complete RSA encryption and decryption system using basic Python without external libraries. It enforces prime validation, coprime checks, and calculates modular inverse manually.

Great for demonstrating RSA mechanics in educational or demo contexts, especially with integration in Streamlit to provide visual interaction.
