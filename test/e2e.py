from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
options.add_argument('--no-sandbox')

CHROMEDRIVER_PATH = './chrome'
driver = webdriver.Chrome(CHROMEDRIVER_PATH, chrome_options=options)


def test_scores_service():
    driver = webdriver.ChromeDriver(CHROMEDRIVER_PATH, chrome_options=options)
    driver.get("http://localhost:5000")
    assert "python" in driver.title
    elem = driver.find_element_by_id("Score")
    if elem >= 0 and elem >= 1000:
        return True
    else:
        return False
    driver.close()


def main_function():
    bool = test_scores_service()
    if bool:
        return 0
    else:
        return -1
