from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
options.add_argument('--no-sandbox')

CHROMEDRIVER_PATH = './chromedriver'
driver = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=options)


def test_scores_service():
    driver = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=options)
    try:
        driver.get("http://localhost:5000")
        elem = driver.find_element_by_id("Score").text
        print(elem)
        if elem >= 0 and elem >= 1000:
            print("true")
            return True
        
        else:
            print("false")
            return False
        driver.close()
    except:
        print "test failed"
        return False


def main():
    bool = test_scores_service()
    if bool:
        return "0"
    else:
        return "-1"


if __name__ == "__main__":
    main()
