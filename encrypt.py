import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):
    if not out_filename:
        out_filename = in_filename + '.ez'

    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    filesize = os.path.getsize(in_filename)

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(iv)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk = pad(chunk, 16)  # Pad the data if necessary

                outfile.write(cipher.encrypt(chunk))

    return out_filename

# Ejemplo de uso:
key = b'\x2a\xb5\x11\xf4\x77\x97\x7d\x25\xcf\x6f\x7a\x8a\xe0\x49\xa1\x25'
in_filename = '2101000.zip'
out_filename = encrypt_file(key, in_filename)
print(f'Archivo cifrado guardado como: {out_filename}')
