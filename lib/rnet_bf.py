from blowfish import Blowfish
import hashlib

def encrypt(key, data):
    h = hashlib.sha1()
    h.update(key)
    cipher = Blowfish(h.hexdigest())
    cipher.initCTR()
    return cipher.encryptCTR(data)
def decrypt(key, edata):
    h = hashlib.sha1()
    h.update(key)
    cipher = Blowfish(h.hexdigest())
    cipher.initCTR()
    return cipher.decryptCTR(edata)

if __name__ == '__main__':
    e = encrypt('password', 'Secret message')
    print repr(e)
    print repr(decrypt('password', e))
    
    
    