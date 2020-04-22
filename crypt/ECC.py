from tinyec import registry
from Crypto.Cipher import AES
import hashlib, secrets, binascii

def encrypt_AES_GCM(msg, secretKey):
    aesCipher = AES.new(secretKey, AES.MODE_GCM)
    ciphertext, authTag = aesCipher.encrypt_and_digest(msg)
    return (ciphertext, aesCipher.nonce, authTag)

def decrypt_AES_GCM(ciphertext, nonce, authTag, secretKey):
    aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
    plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
    return plaintext

def ecc_point_to_256_bit_key(point):
    sha = hashlib.sha256(int.to_bytes(point.x, 32, 'big'))
    sha.update(int.to_bytes(point.y, 32, 'big'))
    return sha.digest()

curve = registry.get_curve('brainpoolP256r1')

def encrypt_ECC(msg, pubKey):
    ciphertextPrivKey = secrets.randbelow(curve.field.n)
    sharedECCKey = ciphertextPrivKey * pubKey
    secretKey = ecc_point_to_256_bit_key(sharedECCKey)
    ciphertext, nonce, authTag = encrypt_AES_GCM(msg, secretKey)
    ciphertextPubKey = ciphertextPrivKey * curve.g
    return (ciphertext, nonce, authTag, ciphertextPubKey)

def decrypt_ECC(encryptedMsg, privKey):
    (ciphertext, nonce, authTag, ciphertextPubKey) = encryptedMsg
    sharedECCKey = privKey * ciphertextPubKey
    secretKey = ecc_point_to_256_bit_key(sharedECCKey)
    plaintext = decrypt_AES_GCM(ciphertext, nonce, authTag, secretKey)
    return plaintext

msg = b'1'
msg1 = b'2'
print("original msg:", msg)
print("original msg1:", msg1)

privKey = secrets.randbelow(curve.field.n)
pubKey = privKey * curve.g

encryptedMsg = encrypt_ECC(msg, pubKey)
encryptedMsg1 = encrypt_ECC(msg1, pubKey)
encryptedMsgObj = {
    'ciphertext': binascii.hexlify(encryptedMsg[0]),
    'nonce': binascii.hexlify(encryptedMsg[1]),
    'authTag': binascii.hexlify(encryptedMsg[2]),
    'ciphertextPubKey': hex(encryptedMsg[3].x) + hex(encryptedMsg[3].y % 2)[2:]
}
encryptedMsgObj1 = {
    'ciphertext': binascii.hexlify(encryptedMsg1[0]),
    'nonce': binascii.hexlify(encryptedMsg1[1]),
    'authTag': binascii.hexlify(encryptedMsg1[2]),
    'ciphertextPubKey': hex(encryptedMsg1[3].x) + hex(encryptedMsg1[3].y % 2)[2:]
}
print("encrypted msg:", encryptedMsgObj)
print("encrypted msg:", encryptedMsgObj1)
x = binascii.hexlify(encryptedMsg1[0]) + binascii.hexlify(encryptedMsg[0])
print("encrypted msg added:",(x))
xlist = encryptedMsg
xlist = list(xlist)
xlist[0] = x
decryptedMsg = decrypt_ECC(encryptedMsg, privKey)
print("decrypted msg:", decryptedMsg)
decryptedMsg1 = decrypt_ECC(encryptedMsg1, privKey)
print("decrypted msg:", decryptedMsg1)
decryptedMsg3 = decrypt_ECC(xlist, privKey)
print("decrypted msg:", decryptedMsg3)