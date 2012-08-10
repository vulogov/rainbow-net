## -*- coding: utf-8 -*-
##
##
##

import unicodedata
import rsa
from rsa import bigfile, varblock, pkcs1
import zlib
from rs import RSCoder
from StringIO import StringIO

class crypto:
    def numencode(self, data):
        c = 0
        out = ""
        for i in data:
            out = out + "%03d "%ord(i)
            c = c + 1
            if c > 10:
                c = 0
                out = out + "\n"
        return out + "\n"
    def numdecode(self, data):
        nums = data.split(" ")
        out = ""
        for i in nums:
            n = i.strip()
            if not n:
                continue
            out = out + chr(int(n))
        return out
    def compress(self, data):
        return zlib.compress(data)
    def uncompress(self, data):
        return zlib.decompress(data)
    def protect(self, data):
        c = RSCoder(255, 127)
        return c.encode(data)
    def getprotected(self, data):
        c = RSCoder(255, 127)
        return c.decode(data)
    def encrypt(self, data, key):
        if type(data) == type(u""):
            infile = StringIO(data.encode('utf8'))
        else:
            infile = StringIO(data)
        outfile = StringIO()
        bigfile.encrypt_bigfile(infile, outfile, key)
        return outfile.getvalue()
    def decrypt(self, data, key):
        infile = StringIO(data)
        outfile = StringIO()
        bigfile.decrypt_bigfile(infile, outfile, key)
        return outfile.getvalue()
    def chunks(self, data, n):
        for start in range(0, len(data), n):
            yield data[start:start+n]
    def encode(self, data, key):
        buf = self.compress(self.encrypt(data, key))
        out = ""
        for chunk in self.chunks(buf, 127):
            out = out + self.numencode(self.protect(chunk))
        return out
    def decode(self, data, key):
        buf = self.numdecode(data)
        chunks = self.chunks(buf, 255)
        buf2 = ""
        for chunk in chunks:
            buf2 = buf2 + self.getprotected(chunk)
        return self.decrypt(self.uncompress(buf2), key)
            


    
    
if __name__ == '__main__':
    c = crypto()
    a1 = c.compress("abcdefgh")
    print "compress=",len(a1)
    print "decompress=",c.uncompress(a1)
    a2 = c.protect("Hello world")
    print "protect=",len(a2)
    print "getprotected=",c.getprotected(a2)
    pub_key, priv_key = rsa.newkeys(512)
    a3 = c.encrypt("This is a secret!", pub_key)
    print "encrypt=",len(a3)
    print "decrypt=",c.decrypt(a3, priv_key)
    a4 = c.chunks(open("/usr/share/dict/words").read(), 256)
    #for i in a4:
    #    print len(i)
    #a5 = c.encode(open("/etc/passwd").read(), pub_key)
    a5 = c.encode("This is a very-very-very secret message.", pub_key)
    print a5
    print c.decode(a5, priv_key)
    a6 = c.encode(u"Большая-пребольшая тайна.", pub_key)
    print a6
    print c.decode(a6, priv_key)
