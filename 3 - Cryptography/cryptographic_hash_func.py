import hashlib, sys

print('\tUSAGE: python3 cryptographic_hash_function.py [FILE_NAME] [CRYPTO_HASH]')
print('\t\tcrypto hashs: MD5, SHA-256, SHA-384, SHA-512, BLAKE-2')

print('\tEXAMPLE: python3 cryptographic_hash_function.py "./file_crypto.txt" "md5"\n')



def file_crypto(name_file, crypto_hash):
    try:
        file = open(name_file, 'rb')
        #print('File content: \n"', string,'"\n')
    except Exception:
        print('ERROR: could not open file')
        return False

    # MD5
    if crypto_hash.upper() == 'MD5':
        digest = hashlib.md5()

    # SHA-256
    elif crypto_hash.upper() == 'SHA-256':
        digest = hashlib.sha256()

    # SHA-384
    elif crypto_hash.upper() == 'SHA-384':
        digest = hashlib.sha384()

    # SHA-512
    elif crypto_hash.upper() == 'SHA-512':
        digest = hashlib.sha512()

    # BLAKE-2   
    elif crypto_hash.upper() == 'BLAKE-2':
        digest = hashlib.blake2b()

    # Error
    else:
        print('\nERROR: Thats not a crypto hash;\nList of crypto hashs: MD5, SHA-256, SHA-384, SHA-512, BLAKE-2')
        return False

    while True:
        data = file.read(2000)
        if not data:
            break
        digest.update(data)
    print('HASH used: ', digest.name)
    print(digest.hexdigest())

if len(sys.argv) == 3:
    file_crypto(sys.argv[1], sys.argv[2])
else:
    print('ERROR: pass all the arguments, see example above')
