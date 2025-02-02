import gmpy2

delta_k = gmpy2.mpz('0xfffffffffffffffffffffffffffffffebaaedce6af487e246f4eac90b714b3bd')
z1 = gmpy2.mpz('0x9233d997d01ccf4b46187b215819354f107e76d9c27968bc460e4463334ee7c3')
r1 = gmpy2.mpz('0x838db77b981db321faf527a830461cfda01aed50d85c345a7b0a8f4e5e4fd3fc')
s1 = gmpy2.mpz('0x288da41a03e78a23e2ac277921e2d19d17717a27a10f1c6cca7fd5ba351a5fca')
z2 = gmpy2.mpz('0xd39ba1c8ae6e441de9b5a2656a0c6b621fb4054986776327731753ed1d858c37')
r2 = gmpy2.mpz('0xde97092bfb7c02148a827b4f8b62db1e189a739c77815799df5e6fb35ae88a1f')
s2 = gmpy2.mpz('0x3f4fa38bcbb17615446fabc6fbebceefbb7d052eca9ce136b3a4a67b7f0d4f42')

# Modulus SECP256k1
n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

# Menghitung pembilang
numerator = (delta_k * s1 * s2) + (z2 * s1) - (z1 * s2)

# Menghitung penyebut
denominator = (r1 * s2 - r2 * s1)

# Menghitung invers perkalian modulo dari penyebut
denominator_inv = gmpy2.invert(denominator, n)

# Menghitung pk
pk = (numerator * denominator_inv) % n

print(hex(pk))
