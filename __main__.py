#!/usr/bin/env python
# file app/__main__.py

import sys
from lib.manager import *

__all__ = ("main")

def main():
	try:
		manager(sys.argv)
	except (IOError):
		return 1
	return 0

if __name__ == '__main__':
	if main():
		print("Oh noes errors happenned :(")
