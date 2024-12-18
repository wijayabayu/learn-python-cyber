# String Unicode yang diberikan
unicode_string = r"\u{43}\u{54}\u{46}\u{52}\u{53}\u{54}\u{7b}\u{55}\u{54}\u{46} \u{31}\u{36}\u{5f}\u{69}\u{35}\u{5f}\u{61}\u{77}\u{33}\u{73} \u{30}\u{6d}\u{65}\u{7d}"

# Fungsi untuk mengubah Unicode ke karakter biasa
def decode_unicode(unicode_string):
    # Bersihkan string untuk mengambil hanya angka hex di antara \u{ }
    unicode_values = unicode_string.split(r"\u{")[1:]
    unicode_values = [value.split("}")[0] for value in unicode_values]
    
    # Konversi setiap angka hex ke karakter
    decoded_characters = [chr(int(value, 16)) for value in unicode_values]
    return ''.join(decoded_characters)

# Dekode string Unicode
decoded_string = decode_unicode(unicode_string)

# Print hasilnya
print("Decoded string:", decoded_string)
