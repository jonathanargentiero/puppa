import sys
import colorama
colorama.init()
from update import *
from purge import *

class manager:
	def __init__(self, arguments):
		## manager config
		self.__author__ = 'Jonathan Argentiero <jonathan.argentiero@gmail.com>'
		# github
		self.__githubuser__ = 'jonathanargentiero'
		self.__githubrepo__ = 'puppa'
		self.__repositoryurl__ = 'https://github.com/'+self.__githubuser__+'/'+self.__githubrepo__
		self.__repositorytags__ = 'https://api.github.com/repos/'+self.__githubuser__+'/'+self.__githubrepo__+'/git/refs/tags'
		self.__puppagitlocation__ = 'dist/'
		# filename
		self.__filename__ = arguments[0]
		# version : python puppa --version
		self.__version__ = '0.3'
		# doc : python puppa
		self.__doc__ = (Fore.MAGENTA + 'PUPPA!' + Style.RESET_ALL)+'\n'
		self.__doc__ += (Fore.BLUE + 'your updatable application package' + Style.RESET_ALL)+'\n'
		self.__doc__ += 'Run "python puppa --help" for a list of commands.'
		# help : python puppa --help
		self.__help__ = (Fore.RED + 'All the commands are listed below!' + Style.RESET_ALL)+'\n'
		self.__help__ += 'Usage:\n'
		self.__help__ += 'python puppa [options] [arguments]\n\n'
		self.__help__ += 'Options:\n'
		self.__help__ += '   -h, --help    	print this commands list\n'
		self.__help__ += '   -v, --version    	print version\n'
		self.__help__ += '   -p, --path    	print path location of the puppa\n'
		self.__help__ += '   -a, --author    	print author info\n'
		self.__help__ += '   update [version]    	updates the puppa from git repository\n'
		self.__help__ += '   purge		purges the puppa\n'	
		self.__help__ += '\n'+(Fore.YELLOW + 'WARNING: purging the puppa is permanent!' + Style.RESET_ALL)+'\n'

		## manager logic
		# python puppa
		if len(arguments) < 2:
			print self.__doc__
			return None

		command = arguments[1]
		# python puppa [options] [arguments]
		if command == 'update':
			# python puppa update
			update(self,arguments)

		elif command == 'purge':
			# python puppa purge
			print (Fore.YELLOW + 'WARNING!' + Style.RESET_ALL)+' This will delete permanently the puppa! Continue? [y/N]'
			choice = raw_input().lower()
			if choice in ['yes','y', 'ye']:
			   purge(self)
			elif choice in ['no','n', '']:
			   return None
			else:
			   sys.stdout.write((Fore.RED + 'UNVALID!' + Style.RESET_ALL)+" please respond with 'yes' or 'no'\n")
			   return None

		elif command == '-h' or command == '--help':
			# python puppa --help
			print self.__help__
			return None

		elif command == '-v' or command == '--version':
			# python puppa --version
			print 'v'+self.__version__
			return None

		elif command == '-p' or command == '--path':
			# python puppa --help
			print self.getCurrentEntryPath()
			return None

		elif command == '-a' or command == '--author':
			# python puppa --version
			print (Fore.GREEN + self.__author__ + Style.RESET_ALL)

		else:
			# python puppa something
			print (Fore.RED + 'COMMAND NOT VALID!' + Style.RESET_ALL)
			print self.__help__
			return None

	def getCurrentEntryPath(self):
		return os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)),'..'))