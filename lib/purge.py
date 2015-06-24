import os, shutil
import colorama
colorama.init()
from colorama import Fore, Back, Style

class purge:
	def __init__(self, manager):
		print (Fore.MAGENTA + 'PURGING...' + Style.RESET_ALL)
		os.remove(manager.getCurrentEntryPath())
		print (Fore.GREEN + 'PURGED!' + Style.RESET_ALL)