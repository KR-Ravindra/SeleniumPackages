from selenium.webdriver.common.keys import Keys
import selenium.webdriver
import org.openqa.selenium.JavascriptExecutor


browser = selenium.webdriver.Firefox()

Google = browser.get("https://slack.com/signin")
browser.implicitly_wait(10)

Workspace = browser.find_element_by_xpath("//input[@id='domain']")
Workspace.send_keys("nutanixcloudchallenge")
Workspace = browser.find_element_by_xpath("//button[@id='submit_team_domain']")
Workspace.click()

Credentials = browser.find_element_by_id("email")
Credentials.send_keys("rajaravindra919@gmail.com")
Credentials = browser.find_element_by_id("password")
Credentials.send_keys("R@V1ndraS")
Credentials = browser.find_element_by_id("signin_btn")
Credentials.click()

Challenge = browser.find_element_by_xpath(
    "//span[contains(text(),'30days_udacity')]")
Challenge.click()
browser.implicitly_wait(4)
Message = "Automate"
WebElement myElement = driver.findElement(By.cssSelector("body.p-client_desktop--ia-top-nav:nth-child(2) div.p-client_container:nth-child(2) div.p-client.p-client--ia-top-nav div.p-workspace-layout div.p-workspace__primary_view:nth-child(3) div.p-workspace__primary_view_contents div.p-file_drag_drop__container footer.workspace__primary_view_footer div.p-message_pane_input div.p-message_pane_input_inner div.p-workspace__input.p-message_input div.c-texty_input__container div.p-message_input_field.c-texty_input--multi_line.c-texty_input.ql-container.c-texty_input--sticky_composer.c-texty_input--double_decker.focus div.ql-editor.ql-blank > p:nth-child(1)"))
String js = "arguments[0].setAttribute('value','"+Message+"')"
((JavascriptExecutor) driver).executeScript(js, myElement)
