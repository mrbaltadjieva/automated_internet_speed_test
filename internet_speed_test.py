from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class InternetSpeedTwitterBot:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.down = 0
        self.up = 0

    class TextNotEmpty:
        def __init__(self, locator):
            self.locator = locator

        def __call__(self, driver):
            elem = driver.find_element(*self.locator)
            txt = elem.text.strip()

            # Speedtest shows "—" before numbers appear
            if txt and txt != "—":
                return elem
            return False

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        wait = WebDriverWait(self.driver, 40)

        # 1. Accept consent
        try:
            consent_button = wait.until(
                EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
            )
            consent_button.click()
        except:
            print("No consent popup — continuing.")

        # 2. Click GO
        go_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".start-button a")))
        go_button.click()

        # Give Speedtest time to switch screens
        time.sleep(3)
        download_locator = (By.CSS_SELECTOR, ".download-speed")
        upload_locator = (By.CSS_SELECTOR, ".upload-speed")

        # 3. Wait until the numbers have REAL TEXT
        down_elem = wait.until(self.TextNotEmpty(download_locator))
        up_elem = wait.until(self.TextNotEmpty(upload_locator))

        self.down = down_elem.text
        self.up = up_elem.text

        print("Download speed:", self.down)
        print("Upload speed:", self.up)

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()`
