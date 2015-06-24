import os, shutil
from download.download import *
import urlparse
import urllib, json
import colorama
colorama.init()
from colorama import Fore, Back, Style

class update:
	def __init__(self, manager, arguments):
		# location of the package on the remote repository
		remotepuppaloc = urlparse.urljoin(manager.__puppagitlocation__, manager.__filename__)

		# get the tag branch or master
		version = 'master'

		### optional versioning based on Github - remove if not required -
		if len(arguments) > 2:
			response = urllib.urlopen(manager.__repositorytags__);
			responseJson = json.loads(response.read())
			if isinstance(responseJson,list):
				ref = None
				for tags in responseJson:
					refnamesplitted = tags['ref'].split('/')
					reftag = refnamesplitted[len(refnamesplitted)-1]
					if reftag == arguments[2]:
						ref = reftag
				if ref is None:
					print (Fore.YELLOW + 'The tag/ref specified has not been found!' + Style.RESET_ALL)
					return None
				else: 
					version = ref
			else:
				print (Fore.RED + 'Github repository/tags not found! Please check you have a repository with at least one tag!' + Style.RESET_ALL)
				return None
		### end of optional versioning

		# get the url of the package
		remotepupparepo = manager.__repositoryurl__ + '/blob/'+version+'/'
		url = urlparse.urljoin(remotepupparepo,remotepuppaloc)+'?raw=true'

		# download
		print (Fore.MAGENTA + 'UPDATING ' + manager.__filename__ + '@' + version + Style.RESET_ALL) 
		print 'Fetching '+url
		download(url,manager.__filename__+'.dist')

		# replace
		os.remove(manager.getCurrentEntryPath())
		shutil.move(manager.__filename__+'.dist',manager.getCurrentEntryPath())
		print (Fore.GREEN + 'UPDATED!' + Style.RESET_ALL)
