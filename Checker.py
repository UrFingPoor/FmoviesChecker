from colorama import Fore
from html.parser import HTMLParser
import requests, os

class fmovies(HTMLParser):
    def __init__(self):
        super().__init__()
        self.data = []
        self.capture = False

    def handle_starttag(self, tag, attrs):
        if tag in ('li'):
            self.capture = True

    def handle_endtag(self, tag):
        if tag in ('li'):
            self.capture = False

    def handle_data(self, data):
        if self.capture:              
            self.data.append(data)

def logo():
    width = os.get_terminal_size().columns
    os.system('cls')
    os.system('title Lethal Services!')
    print(Fore.LIGHTMAGENTA_EX+'                                                           '.center(width))
    print(Fore.LIGHTMAGENTA_EX+'     ██╗     ███████╗████████╗██╗  ██╗ █████╗ ██╗          '.center(width))
    print(Fore.LIGHTMAGENTA_EX+'     ██║     ██╔════╝╚══██╔══╝██║  ██║██╔══██╗██║          '.center(width))
    print(Fore.LIGHTMAGENTA_EX+'     ██║     █████╗     ██║   ███████║███████║██║          '.center(width))
    print(Fore.LIGHTMAGENTA_EX+'     ██║     ██╔══╝     ██║   ██╔══██║██╔══██║██║          '.center(width))
    print(Fore.LIGHTMAGENTA_EX+'     ███████╗███████╗   ██║   ██║  ██║██║  ██║███████╗     '.center(width))
    print(Fore.LIGHTMAGENTA_EX+'     ╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝     '.center(width))
    print(Fore.LIGHTCYAN_EX+'        TOS: Lethal Holds No Responsibility At ALL!         '.center(width))
    print(Fore.WHITE+f'             Version: Beta 1.0.0 https://lethals.org/            \n\n'.center(width))

def main():
    logo()
    request = requests.get('https://fmovies.name/')
    if request.ok:       
            parser = fmovies()
            parser.feed(request.text)
            for results in parser.data:
                if 'live' in results:
                    print(f'[{Fore.GREEN}Info{Fore.WHITE}] {Fore.LIGHTMAGENTA_EX}Status{Fore.WHITE}: {Fore.LIGHTGREEN_EX}{results.capitalize()}{Fore.WHITE}') 
                else:
                    print(f'[{Fore.GREEN}Result{Fore.WHITE}] {Fore.LIGHTBLUE_EX}Website{Fore.WHITE}: {Fore.LIGHTYELLOW_EX}https://{results}/{Fore.WHITE}') 
    else:    
            print(f'{Fore.LIGHTGREEN_EX}Status_Code{Fore.WHITE}: {Fore.LIGHTYELLOW_EX}{request.status_code}{Fore.WHITE} | Something Went {Fore.LIGHTRED_EX}Wrong!{Fore.WHITE}') 

if __name__ == "__main__":
	main()
