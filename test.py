import colorama

colorama.just_fix_windows_console()

def colorize_print(bruh):
	print(colorama.Fore.RED+bruh+colorama.Style.RESET_ALL)

print("hello world!")
list2 = ['hello', 'bonjour', 'ohayo', 'hola']
for i in list2:
	colorize_print(i)
