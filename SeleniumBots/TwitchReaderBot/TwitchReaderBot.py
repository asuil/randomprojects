"""
*
*   a selenium based bot for reading twitch chat :)
*
*   author :        github.com/asuil
*   version :       0.0
*   date :          12-05-2020
*
"""

# import dependencies
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep


# main app manager class
class TwitchReaderBot:
    # static configurable variables
    streamer_id = "elrichmc"

    # initialize web driver
    def __init__(self):
        # create a webdriver
        self.driver = webdriver.Chrome()

    def read(self, xpath):
        return self.driver.find_element_by_xpath(xpath).text

    # code to run
    def run(self):

        # prepare variables
        xpath_to_parse = "/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div/" \
                         "section/div/div[3]/div/div[2]/div[3]/div/div/div[{}]/span[4]"
        message_id = 2

        # enter twitch
        self.driver.get(f"https://www.twitch.tv/{TwitchReaderBot.streamer_id}")
        # wait for it to load
        sleep(3)

        # try to get new messages until you can't
        while True:
            try:
                new_message = self.read(xpath_to_parse.format(message_id))
                print(new_message)
                message_id += 1
            except NoSuchElementException:
                pass


# execution
if __name__ == '__main__':
    TwitchReaderBot().run()
