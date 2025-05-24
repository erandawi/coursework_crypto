import streamlit as st
from affine_cipher import AffineCipher
from rsa_cipher import RSACipher

st.title("Affine Cipher & RSA Cipher Demo")

option = st.sidebar.selectbox("Choose Cipher", ("Affine Cipher", "RSA Cipher"))

if option == "Affine Cipher":
    st.header("Affine Cipher")
    word = st.text_input("Enter a word to encrypt and decrypt")
    a = st.number_input("Multiplicative Key (a)", min_value=1, max_value=25, step=1)
    b = st.number_input("Additive Key (b)", min_value=0, max_value=25, step=1)

    if st.button("Run Affine Cipher"):
        try:
            cipher = AffineCipher(int(a), int(b))
            encrypted = cipher.encrypt(word)
            decrypted = cipher.decrypt(encrypted)
            st.success(f"Encrypted: {encrypted}")
            st.success(f"Decrypted: {decrypted}")
        except Exception as e:
            st.error(str(e))

elif option == "RSA Cipher":
    st.header("RSA Cipher")
    p = st.number_input("Enter prime number p", min_value=2, step=1)
    q = st.number_input("Enter prime number q", min_value=2, step=1)
    e = st.number_input("Enter public exponent e", min_value=1, step=1)
    binary_str = st.text_input("Enter 8-bit binary string to encrypt and decrypt")

    if st.button("Run RSA Cipher"):
        try:
            rsa = RSACipher(int(p), int(q), int(e))
            st.write(f"n = {rsa.n}, phi(n) = {rsa.phi}, d = {rsa.d}")

            if binary_str:
                encrypted = rsa.encrypt(binary_str)
                decrypted = rsa.decrypt(encrypted)
                st.success(f"Encrypted (ciphertext): {encrypted}")
                st.success(f"Decrypted binary: {decrypted}")

        except Exception as e:
            st.error(str(e))
