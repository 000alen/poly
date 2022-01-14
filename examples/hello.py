K = "704e93c7ec69922eed9a4c637707e11c"
S = "w5PCpsKZwqDCpsKMVXnCmcOPwqHCpGBQwrjDksKrw5DDh1PCh18="


import uuid
import hashlib
import base64
import functools


@functools.cache
def e(k, s): return str(base64.urlsafe_b64encode(
    "".join([chr(ord(s[i]) + ord(k[i % len(k)]) % 256)
             for i in range(len(s))]).encode("utf-8")), "utf-8")


@functools.cache
def d(k, s): return "".join([chr(ord(s_i) - ord(k[i % len(k)]) % 256)
                             for i, s_i in enumerate(base64.urlsafe_b64decode(s).decode("utf-8"))])


@functools.cache
def h(s): return hashlib.md5(s.encode()).hexdigest()


@functools.cache
def s(): return "".join(open(__file__).readlines()[1:])


@functools.cache
def x(n): return int(n, 16)


def r(): return str(uuid.uuid4()).replace("-", "")


def w(s): open(__file__, "w").write(s)


def m():
    L = s().split("\n")
    A = r()
    L[0] = f"S = \"" + e(A, d(hex(x(h(s())) ^ x(K))[2:], S)) + "\""
    _S = "\n".join(L)
    B = h(_S)
    w(f"K = \"" + hex(x(A) ^ x(B))[2:] + "\"\n" + _S)


try:
    exec(d(hex(x(h(s())) ^ x(K))[2:], S))
    m()
except:
    print("Integrity error")
