from colorama import Fore
from html.parser import HTMLParser
import requests

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
def main():
    request = requests.get('https://fmovies.name/')
    if request.status_code == 200:       
            parser = fmovies()
            parser.feed(request.text)
            for results in parser.data:
                print(f'[{Fore.GREEN}Info{Fore.WHITE}] [{Fore.LIGHTRED_EX}Alert{Fore.WHITE}] [+] {results.capitalize()}') 
    else:    
            print(f'{Fore.LIGHTGREEN_EX}Status_Code{Fore.WHITE}: {Fore.LIGHTYELLOW_EX}{request.status_code}{Fore.WHITE} | Something Went {Fore.LIGHTRED_EX}Wrong!{Fore.WHITE}') 

if __name__ == "__main__":
	main()
