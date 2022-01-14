from io import StringIO
from typing import TypedDict
from poly import poly
import argparse
import sys


class Args(TypedDict):
    package: str
    outfile: StringIO


parser = argparse.ArgumentParser()
parser.add_argument(
    "package",
)
parser.add_argument(
    "-o",
    "--outfile",
    nargs="?",
    type=argparse.FileType("w"),
    default=sys.stdout
)

args: Args = parser.parse_args()

poly(args.package, args.outfile)
