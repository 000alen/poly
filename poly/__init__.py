import base64
from io import StringIO
import json
import os
import string
import uuid
import hashlib


TEMPLATE_FILE = "template.template"


def hash(string: str) -> str:
    return hashlib.md5(string.encode()).hexdigest()


def encode(k: str, s: str) -> str: return str(base64.urlsafe_b64encode(
    "".join([chr(ord(s[i]) + ord(k[i % len(k)]) % 256)
             for i in range(len(s))]).encode("utf-8")), "utf-8")


def decode(k: str, s: str) -> str: return "".join([chr(ord(s_i) - ord(k[i % len(k)]) % 256)
                                                   for i, s_i in enumerate(base64.urlsafe_b64decode(s).decode("utf-8"))])


def get_template() -> string.Template:
    template_path = os.path.join(os.path.dirname(__file__), TEMPLATE_FILE)
    with open(template_path) as template_object:
        template = string.Template(template_object.read())
    return template


def poly(package: str, outfile: StringIO):
    template = get_template()

    with open(package) as content_object:
        content = content_object.read()

    random_key = str(uuid.uuid4()).replace("-", "")

    output = template.substitute(
        content=json.dumps(encode(random_key, content)),
    )

    random_key = int(random_key, 16)
    output_hash = int(hash(output), 16)
    key = random_key ^ output_hash

    outfile.write(f"K = \"{hex(key)[2:]}\"\n{output}")
    outfile.close()
