# -*- coding: utf8 -*-

import rsa

class RSA:
    def __init__(self):
        self.priv_key = None
        self.pub_key  = None
    def _generateRSA(self):
        self.pub_key, self.priv_key = rsa.newkeys(1536)
    def _loadRSA(self, pub, priv):
        self.priv_key = rsa.key.PrivateKey.load_pkcs1(priv)
        self.pub_key = rsa.key.PublicKey.load_pkcs1(pub)

    