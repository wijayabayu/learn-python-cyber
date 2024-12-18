# Ciphertext dan key
ciphertext_hex = "51565e5156514c416340574a4740574a4740574a4740574a65"
key = 0x18  # Konversi hexadecimal ke integer

# Konversi ciphertext dari hexadecimal ke bytes
ciphertext_bytes = bytes.fromhex(ciphertext_hex)
        
# Lakukan XOR dengan key
plaintext_bytes = bytes([byte ^ key for byte in ciphertext_bytes])

# Konversi hasil ke string untuk mendapatkan plaintext
plaintext = plaintext_bytes.decode('utf-8', errors='ignore')

print("Plaintext:", plaintext)
