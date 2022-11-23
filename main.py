import signal
from py_console import console
from progress.bar import IncrementalBar
from time import sleep
from bs4 import BeautifulSoup

from InstaBuddy import InstaBuddy
from routines import login, post_random_image


def handler(signum, frame):
    res = input("Ctrl-c was pressed. Do you really want to exit? y/n ")
    if res == 'y':
        exit(1)
 

if __name__ == "__main__":
    console.setShowTimeDefault(True)
    console.log("Press Ctrl+c to exit.")
    signal.signal(signal.SIGINT, handler)


    while True:
        # start posting routine 
        console.info("[*] posting image...")
        bot = InstaBuddy()
        bot.post_data_init()
        bot.go_to_page("https://instagram.com")
        sucess = login(bot)
        if not sucess:
            bot.clean_close_driver()
        else:
            bot.go_to_page(f"https://www.instagram.com/{bot.username}/")
            res = post_random_image(bot)
            if res:
                bot.clean_post_data()
                console.success("[+] Image has been posted.")
            else:
                console.error("[-] Image couldn't be posted.")
            bot.clean_close_driver()
        # end posting routine

        with IncrementalBar('Waiting before next post', max=14400) as bar:
            for i in range(14400):
                # Do some work
                sleep(1)
                bar.next()
