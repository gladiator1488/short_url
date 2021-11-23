# import sqlite3 as sq
# import hashlib
 
# mystring = input('Enter String to hash: ')
 
# # Предположительно по умолчанию UTF-8
# hash_object = hashlib.md5(mystring.encode())
# print(hash_object.hexdigest())


# # def check(l):
# #     conn = sq.connect("short_url.db")
# #     cur = conn.cursor()   
# #     cur.execute(f"SELECT * FROM links WHERE long_url={l}")
# #     a = cur.fetchall()
# #     # query = f'IF {link} NOT IN '
# #     cur.close()
# #     conn.close()
# #     return a

# # print(check(1))

# from hashids import Hashids
# hashids = Hashids(salt='this is my salt 1')

# hashid = hashids.encode("rgegregrege") 
# print(hashid)

import hashlib
password = 'Pa$$w0rD'.encode()
salt = 'Ваша соль'.encode()
dk = hashlib.scrypt(password, dklen=3)
print(dk.hex())
print(dk)