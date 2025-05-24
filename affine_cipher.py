class AffineCipher:
    def __init__(self, a, b):
        if self.gcd(a, 26) != 1:
            raise ValueError("Multiplicative key 'a' must be coprime with 26.")
        self.a = a
        self.b = b
        self.a_inv = self.modinv(a, 26)

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def modinv(self, a, m):
        for i in range(1, m):
            if (a * i) % m == 1:
                return i
        raise ValueError("No modular inverse exists.")

    def encrypt(self, plaintext):
        ciphertext = ''
        for char in plaintext:
            if char.isalpha():
                x = ord(char.lower()) - ord('a')
                enc = (self.a * x + self.b) % 26
                ciphertext += chr(enc + ord('a'))
            else:
                ciphertext += char
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = ''
        for char in ciphertext:
            if char.isalpha():
                y = ord(char.lower()) - ord('a')
                dec = (self.a_inv * (y - self.b)) % 26
                plaintext += chr(dec + ord('a'))
            else:
                plaintext += char
        return plaintext
