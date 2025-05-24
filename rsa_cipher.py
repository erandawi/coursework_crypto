class RSACipher:
    def __init__(self, p, q, e):
        if not self.is_prime(p) or not self.is_prime(q):
            raise ValueError("Both p and q must be prime.")
        self.p = p
        self.q = q
        self.n = p * q
        self.phi = (p - 1) * (q - 1)
        if self.gcd(e, self.phi) != 1:
            raise ValueError("e must be coprime to phi(n).")
        self.e = e
        self.d = self.modinv(e, self.phi)

    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def modinv(self, a, m):
        for i in range(1, m):
            if (a * i) % m == 1:
                return i
        raise ValueError("No modular inverse exists.")

    def encrypt(self, binary_str):
        m = int(binary_str, 2)
        c = pow(m, self.e, self.n)
        return c

    def decrypt(self, c):
        m = pow(c, self.d, self.n)
        return format(m, '08b')