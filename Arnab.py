from colorama import Fore,Style
from time import sleep

def Arnab(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='#'):
	percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration/float(total)))
	filledLength = int(length * iteration // total)
	bar = fill * filledLength + '-' * (length - filledLength)
	print(Fore.GREEN+Style.BRIGHT+f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
	if iteration == total:
		print()

items = list(range(0, 50))
l = len(items)

Arnab(0, l, prefix='System Loading:', suffix='Complete', length=l)
for i, item in enumerate(items):
	sleep(0.1)
	Arnab(i + 1, l, prefix='System Loading:', suffix='Complete', length=l)