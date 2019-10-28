'''
Filename: /home/tomas/Desktop/SIO/4 - Validation of X.509 Certificates/trust_anchor_certificates.py
Path: /home/tomas/Desktop/SIO/4 - Validation of X.509 Certificates
Created Date: Monday, October 28th 2019, 5:44:45 pm
Author: tomas

Copyright (c) 2019 Your Company
'''

import os
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from datetime import datetime
from Certificate_Validity_Interval import load_file_certs


for entry in os.scandir(path='/etc/ssl/certs'):
    load_file_certs(entry) if (not entry.is_dir() and load_file_certs(entry)) else 0
