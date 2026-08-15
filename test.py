import colorama

colorama.just_fix_windows_console()

def colorize_print(bruh):
	print(colorama.Fore.LIGHTMAGENTA_EX+bruh+colorama.Style.RESET_ALL)

list2 = ['hello', 'konnichiwa', 'hallo', 'hola']
for i in list2:
	colorize_print(i)
