python genpem.py > private.pem
openssl rsa -in private.pem -out private.pem.unencrypted
