from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AmazonScrap:

    def __init__(self, driver):
        self.driver = driver

    def product_page(self, url):
        return self.driver.get(url)
    
    def product_whole_price_objt(self):
        elmt = '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[2]'
        return WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, elmt)))

    def product_fraction_price(self):
        elmt = '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[3]'
        return self.driver.find_element(By.XPATH, elmt)




# '//*[@id="corePrice_feature_div"]/div/span[1]/span[2]/span[2]'
# '/html/body/div[1]/div[2]/div[9]/div[5]/div[1]/div[6]/div/div[1]/div/div/div/form/div/div/div/div/div[2]/div[1]/div/span[1]/span[2]/span[3]'