'''
Filename: /home/tomas/Desktop/SIO/4 - Validation of X.509 Certificates/Certificate_Validity_Interval.py
Path: /home/tomas/Desktop/SIO/4 - Validation of X.509 Certificates
Created Date: Monday, October 28th 2019, 5:08:38 pm
Author: tomas

Copyright (c) 2019 Tomas Batista
'''

from cryptography import x509
from cryptography.hazmat.backends import default_backend
from datetime import datetime

certs = {}

# openssl s_client -connect www.ua.pt:443 -showcerts 
def load_file_certs(file):
    d = datetime.today()
    with open(file) as file:
        cert = x509.load_pem_x509_certificate(file.read().encode(), default_backend())    
    print(cert.subject)
    certs[cert.subject] = cert
    print(f'  Creation time:\t{cert.not_valid_before}')
    print(f'  Expiration time:\t{cert.not_valid_after}')
    print(f'EXPIRED!') if d > cert.not_valid_after else 0
    return False if d > cert.not_valid_after else True

print('--- CA Server ---')
load_file_certs('ua_certs_servidor.pem')
print('\n--- CA Intermediario ---')
load_file_certs('ua_certs_intermediario.pem')