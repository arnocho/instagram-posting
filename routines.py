from InstaBuddy import InstaBuddy
from time import sleep


def login(ib : InstaBuddy):
    #init the project
    ib.create_folder()
    #remove cookie banner
    try:
        ib.click_on_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]")
    except:
        pass
    #write username
    ib.write_text_on_name("username", ib.username)
    #write password and send form
    ib.write_text_on_name("password", ib.password, True)
    #check if account is suspected
    if ib.is_suspected():
        return False
    else:
        return True

def post_random_image(ib : InstaBuddy):
    post = True
    #click on create button
    post = ib.click_on_xpath("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[1]/div/div/div/div/div[2]/div[6]/div/div/a/div")
    #send image
    post = ib.write_text_on_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/form/input", ib.image_to_upload[0])
    #click on next
    post = ib.click_on_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/button")
    #click on next
    post = ib.click_on_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/button")
    #write description
    post = ib.write_text_on_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/textarea", ib.description)
    #click on post
    post = ib.click_on_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/button")
    sleep(ib.time_after_post)
    return post