from cryptography.fernet import Fernet


def do_fernet():
    b_key = Fernet.generate_key()
    print(f"key = {b_key}")

    plaintext = "This is clear text"
    fernet = Fernet(b_key)
    b_cipher = fernet.encrypt(plaintext.encode())
    s_plaintext = fernet.decrypt(b_cipher)
    print(plaintext, b_cipher, s_plaintext)


if __name__ == "__main__":
    do_fernet()
