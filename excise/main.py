#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cli import args
from excision import excision


def main() -> None:
    excision(args.file, args.start, args.end)


if __name__ == "__main__":
    main()
