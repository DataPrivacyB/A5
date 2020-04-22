import paillier as p

priv, pub = p.generate_keypair(128)

x = p.encrypt(pub, 250)
y = p.encrypt(pub, 300)
z = p.e_add(pub, x, y)
b = p.e_sub(pub,x,y)
a = p.decrypt(priv, pub, z)
c = p.decrypt(priv, pub, b)
print(x)
print(y)
print(z)
print(a)
print(c)