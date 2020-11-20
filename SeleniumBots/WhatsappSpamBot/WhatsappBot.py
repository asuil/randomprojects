"""
*
*   a selenium based bot for bothering frineds :)
*
*   author :        github.com/asuil
*   version :       0.0
*   date :          10-05-2020
*
"""


# import dependencies
from selenium import webdriver
from time import sleep


# main app manager class
class WhatsappBot:

    # static variables
    contact_name = "Tamal"
    message = "hola po dormilona uwu"

    # initialize web driver
    def __init__(self):
        # create a webdriver
        self.driver = webdriver.Chrome()

    def click(self, xpath):
        self.driver.find_element_by_xpath(xpath).click()
        sleep(1)

    def write(self, xpath, text):
        self.driver.find_element_by_xpath(xpath).send_keys(text)
        sleep(1)

    # code to run
    def run(self):

        # enter whatsapp web
        self.driver.get("https://web.whatsapp.com/")
        # connect with your phone now
        sleep(10)
        # find your chat of interest
        user_xpath = f"//span[contains(text(), '{WhatsappBot.contact_name}')]"
        self.click(user_xpath)
        # write to your chatbox
        chat_xpath = "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]"
        self.write(chat_xpath, WhatsappBot.message)
        # send!
        send_xpath = "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button"
        self.click(send_xpath)


# execution
if __name__ == '__main__':
    WhatsappBot().run()
