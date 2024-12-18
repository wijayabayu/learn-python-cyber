chiper_text = '51565e5156514c416340574a4740574a4740574a4740574a65'
key = 0x18

chiper_byte = bytes.fromhex(chiper_text)

xor_key = bytes([byte ^ key for byte in chiper_byte])

xor = xor_key.decode('utf-8', errors='ignore')

print (xor)
