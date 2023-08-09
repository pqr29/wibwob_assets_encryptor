import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# Definir la clave
key = bytes([0x80, 0xF0, 0x08, 0x39, 0x4E, 0xB0, 0x2F, 0x4F, 0xC7, 0xF5, 0xA5, 0xC2, 0x35, 0xC4, 0x29, 0x18])

# Función para encriptar un archivo OGG a OG
def encrypt_ogg_to_og(input_file, output_file):
    cipher = AES.new(key, AES.MODE_CBC)
    
    with open(input_file, 'rb') as infile:
        ogg_data = infile.read()
        encrypted_data = cipher.encrypt(pad(ogg_data, 16))
        
        with open(output_file, 'wb') as outfile:
            outfile.write(cipher.iv + encrypted_data)

# Ejemplo de uso
input_ogg_file = 'ywp_bgm_map_019.ogg'
output_encrypted_og_file = 'archivo_encrypted.og'
encrypt_ogg_to_og(input_ogg_file, output_encrypted_og_file)
print('Archivo OGG encriptado a OG exitosamente.')

