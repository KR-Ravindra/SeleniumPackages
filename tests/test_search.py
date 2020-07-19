from selenium.webdriver.common.keys import Keys
import selenium.webdriver


browser = selenium.webdriver.Firefox()
browser.minimize_window()

browser.get(
    "https://www.youtube.com/watch?v=2mDCVzruYzQ&list=RDCLAK5uy_lyVnWI5JnuwKJiuE-n1x-Un0mj9WlEyZw")
browser.implicitly_wait(10)

# search = browser.find_element_by_xpath("//input[@id='search']")
# search.send_keys("LinkinPark hits")
# search.send_keys(Keys.ENTER)

# play = browser.find_element_by_xpath("//span[@id='overlay-text']")
# play.click()


t = 1
while t:
    control = input("Enter r p f q: ")
    if control == 'p':
        controls = browser.find_element_by_xpath(
            "//button[@class='ytp-play-button ytp-button ytp-play-button-playlist']")
        controls.click()
    if control == 'f':
        controls = browser.find_element_by_xpath(
            "//a[@class='ytp-next-button ytp-button']")
        controls.click()
    if control == 'r':
        controls = browser.find_element_by_xpath(
            "//a[@class='ytp-prev-button ytp-button']")
        controls.click()
    if control == 'q':
        t = 0

browser.quit()
