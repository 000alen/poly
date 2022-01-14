import base64
import uuid
import hashlib


def hash(string: str) -> str:
    return hashlib.md5(string.encode()).hexdigest()


def encode(k: str, s: str) -> str: return str(base64.urlsafe_b64encode(
    "".join([chr(ord(s[i]) + ord(k[i % len(k)]) % 256)
             for i in range(len(s))]).encode("utf-8")), "utf-8")


def decode(k: str, s: str) -> str: return "".join([chr(ord(s_i) - ord(k[i % len(k)]) % 256)
                                                   for i, s_i in enumerate(base64.urlsafe_b64decode(s).decode("utf-8"))])


def main():
    with (
        open("template.py", "r") as template,
        open("input.py", "r") as content,
    ):
        TEMPLATE = template.read()
        CONTENT = content.read()

    A = str(uuid.uuid4()).replace("-", "")

    OUTPUT = TEMPLATE.format(
        content=encode(A, CONTENT)
    )

    B = hash(OUTPUT)

    a = int(A, 16)
    b = int(B, 16)
    c = a ^ b

    with open("output.py", "w") as output:
        output.write(f"K = \"{hex(c)[2:]}\"\n{OUTPUT}")


if __name__ == "__main__":
    main()
