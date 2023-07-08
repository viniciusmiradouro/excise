import argparse
from pydantic import FilePath, PositiveInt

parser = argparse.ArgumentParser(description="Extracts and prints an inclusive range of lines from a file.")
parser.add_argument("file", type=FilePath, help="The path to the file")
parser.add_argument("start", type=PositiveInt, help="The starting line number (1-based).")
parser.add_argument("end", type=PositiveInt, help="The ending line number (inclusive).")
args = parser.parse_args()
