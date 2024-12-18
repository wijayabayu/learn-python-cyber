#soal Ez_XOR Pixiee
cipher_text = "51565e5156514c416340574a4740574a4740574a4740574a65"
key = 0x18

cipher_bytes = bytes.fromhex(cipher_text)
hasil_bytes = (bytes([byte ^ key for byte in cipher_bytes]))
plaintext = hasil_bytes.decode('utf-8', errors='ignore')
print(plaintext)

print("<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>")
#soal cryptohack ASCII
ascii_code = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
decoded_ascii = ''.join(chr(code) for code in ascii_code)
print (decoded_ascii)

print ("<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>")
#soal cryptohack hex
hexa_code = ('63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d')
decoded_hexa = bytes.fromhex(hexa_code)
print (decoded_hexa)

print ("<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>")
#soal cryptohack base64
import base64
base = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
base_bytes = bytes.fromhex(base)
base_decode = base64.b64encode(base_bytes)
print (base_decode.decode())
       
#soal cryptohack Bytes adn Big Integer
#from Crypto.Util.number import long_to_bytes
#long_to_bytes('11515195063862318899931685488813747395775516287289682636499965282714637259206269').decode()
#soalnya khusus di python pycryptodome
print('<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>..')
#soal cryptohack XOR
string = b"label"
print (''.join(chr(st ^ 13) for st in string))

#soal cryptohack XOR Properties
k1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
k2_k1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
k2_k3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
flag_k1_k3_k2 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

k1_ord = [o for o in bytes.fromhex(k1)]
k2_k3_ord = [o for o in bytes.fromhex(k2_k3)]
flag_k1_k3_k2_ord = [o for o in bytes.fromhex(flag_k1_k3_k2)]

flag_k1_ord = [
    o_f132 ^ o23 for (o_f132, o23) in zip(flag_k1_k3_k2_ord, k2_k3_ord)
]
flag_ord = [o_f1 ^ o1 for (o_f1, o1) in zip(flag_k1_ord, k1_ord)]
flag = "".join(chr(o) for o in flag_ord)

print("Flag:")
print(flag)