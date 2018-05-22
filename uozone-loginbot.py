from selenium import webdriver


def bot (username, password):
    
    #System.setProperty("webdriver.chrome.driver", "/Library/seleniumdrivers/chromedriver")
    #WebDriver driver = new ChromeDriver()              
    #driver.get("https://uozone2.uottawa.ca/?language=en")

    driver= webdriver.Chrome("/Library/seleniumdrivers/chromedriver")
    driver.get("https://uozone2.uottawa.ca/?language=en")


    user= driver.find_element_by_css_selector("#userid")
    user.clear()
    user.send_keys(username)

    pas= driver.find_element_by_css_selector("#password")
    pas.clear()
    pas.send_keys(password)

    btn= driver.find_element_by_css_selector("#silverb")
    btn.click()

    if __name__ == "__main__":
        file= open("uozone.rtf", 'r')
        uozone= file.readlines()
        file.close()
        bot(uozone[0], uozone[1])

