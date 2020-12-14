import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# URL = 'https://algeria.blsspainvisa.com/english/book_appointment.php'
from selenium.webdriver.support.wait import WebDriverWait

URL = 'http://www.exteriores.gob.es/Embajadas/NUEVADELHI/en/Noticias/Pages/Articulos/20200723_NOT8.aspx'
IS_MONITORING = False


def get_times(driver):
    try:
        print('2')
        driver.get(URL)
        print('3')
        driver.find_element_by_xpath("//div[@class='content contenidoLayout']//p[2]/a").click()
        print('4')
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[-1])
        print('5')
        time.sleep(1)
        print('6')
        WebDriverWait(driver, 60).until(
            EC.invisibility_of_element_located((By.XPATH, '//img[@class="clsBktWidgetDefaultLoading"]')))
        print('7')
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'bktContinue'))).click()
        print('8')
        time.sleep(3)
        print('9')
        driver.find_element_by_xpath("//a[contains(@href, 'bkt550308')]").click()
        print('10')
        time.sleep(5)
        print('11')
        WebDriverWait(driver, 60).until(
            EC.invisibility_of_element_located((By.XPATH, '//div[@class="clsDivBktWidgetDefaultLoading"]')))
        time.sleep(3)
        if driver.find_element_by_id('idDivNotAvailableSlotsTextTop').is_displayed():
            times = []
        else:
            times_elements = driver.find_elements_by_id("clsDivDatetimeSlot")
            times = ["12:10",'11:00']
            print(14)
            if times_elements:
                for time_slot in times_elements:
                    times.append(time_slot.text.strip())
        print(times)
    except Exception as e:
        times = str(e)
    screen = driver.get_screenshot_as_png()
    return times, screen
