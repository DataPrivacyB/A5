import phe
from phe import paillier
import json

pub_key,priv_key = paillier.generate_paillier_keypair()
print(pub_key.getN())
# enc1 = pub_key.encrypt(5)
# enc2 = pub_key.encrypt(20)
# enc3 = pub_key.encrypt(30,precision=1e-2)
# priv_key.decrypt(enc1), priv_key.decrypt(enc2), priv_key.decrypt(enc3)
#
# keyring = paillier.PaillierPrivateKeyring()
# pub_keys = []
# for i in range(5):
#     pub,priv = paillier.generate_paillier_keypair()
#     pub_keys.append(pub)
#     keyring.add(priv)
# enc1= pub_keys[0].encrypt(5.5)
# enc2= pub_keys[2].encrypt(13.6)
# enc3= pub_keys[3].encrypt(3.14)
# ## Notice below keyring will findout right private key for decrypting number without developer manually keeping track of it..
# keyring.decrypt(enc1), keyring.decrypt(enc2), keyring.decrypt(enc3)
#
# enc1 = pub_key.encrypt(10)
# enc2 = pub_key.encrypt(20)
# enc3 = pub_key.encrypt(30)
#
# print(enc1,enc2,enc3)
# print("1:",priv_key.decrypt(enc1))
# enc1 = enc1 + 3.3
# print("2:",priv_key.decrypt(enc1))
# enc1 = enc1 - 3.3
# print("3:",priv_key.decrypt(enc1))
# enc4 = enc2 + enc3
# print("4:",priv_key.decrypt(enc4))
# enc5 = enc3 - enc2
# print("5:",priv_key.decrypt(enc5))
# enc6 = -5 + enc5
# print("6:",priv_key.decrypt(enc6))
#
# enc1 = enc1 * 2.2
# print("wrong",priv_key.decrypt(enc1))
# enc1 = enc1 / 10
# print("wrong",priv_key.decrypt(enc1))
# enc7 = enc1 * -2
# print("wrong",priv_key.decrypt(enc7))
# enc8 = enc1 / -2
# print("wrong enc1 / -2",priv_key.decrypt(enc8))
