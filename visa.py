import time

from selenium.common.exceptions import NoSuchWindowException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# URL = 'https://algeria.blsspainvisa.com/english/book_appointment.php'
from selenium.webdriver.support.wait import WebDriverWait

URL = 'http://www.exteriores.gob.es/Embajadas/NUEVADELHI/en/Noticias/Pages/Articulos/20200723_NOT8.aspx'
IS_MONITORING = False


def get_times(driver):
    times = []
    try:
        print('2')
        driver.get(URL)
        print('3')
        driver.find_element_by_xpath("//div[@class='content contenidoLayout']//p[2]/a").click()
        print('4')
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[-1])
        print('5')
        print('6')
        WebDriverWait(driver, 60).until(
            EC.invisibility_of_element_located((By.XPATH, '//img[@class="clsBktWidgetDefaultLoading"]')))
        print('7')
        WebDriverWait(driver, 60).until(
            EC.invisibility_of_element_located((By.XPATH, '//div[@class="clsDivBktWidgetDefaultLoading"]')))
        print('8')
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'bktContinue'))).click()
        time.sleep(1)
        print('9')
        driver.find_element_by_xpath("//a[contains(@href, 'bkt550308')]").click()
        print('10')
        time.sleep(2)
        print('11')
        try:
            WebDriverWait(driver, 200).until(
                EC.invisibility_of_element_located((By.XPATH, '//div[@class="clsDivBktWidgetDefaultLoading"]')))
            print('12')
            time.sleep(1)
            if not len(driver.find_elements_by_id('idDivNotAvailableSlotsTextTop')):
                times_elements = driver.find_elements_by_id("clsDivDatetimeSlot")
                print(14)
                if times_elements:
                    for time_slot in times_elements:
                        times.append(time_slot.text.strip())
        except:
            pass
    except Exception as e:
        errors = driver.find_elements_by_id('idDivBktDefaultErrorDatetimeLoadingData')
        if not len(errors):
            times = str(e)
    screen = driver.get_screenshot_as_png()
    print(times)
    return times, screen


def create_user(driver, passport, passport_expired, name, surname, email, cellphone, nationality, create_pass):
    driver.find_element_by_id('idIptBktdocument').send_keys(passport)
    driver.find_element_by_id('idIptBktcustom2').send_keys(passport_expired)
    driver.find_element_by_id('idIptBktname').send_keys(name)
    driver.find_element_by_id('idIptBktcustom1').send_keys(surname)
    driver.find_element_by_id('idIptBktemail').send_keys(email)
    driver.find_element_by_id('idIptBktcellphone').send_keys(cellphone)
    driver.find_element_by_id('idIptBktcustom3').send_keys(nationality)
    driver.find_element_by_id('idIptBktpassword').send_keys(create_pass)
    driver.find_element_by_xpath('//label[@for="idIptBktAcceptCondtions"]').click()
    time.sleep(1)
    driver.find_element_by_id('idBktDefaultSignUpConfirmButton').click()
    WebDriverWait(driver, 60).until(
        EC.invisibility_of_element_located((By.XPATH, '//div[@class="clsDivBktWidgetDefaultLoading"]')))


def add_existing_user(driver, passport, password):
    driver.find_element_by_id('idDivBktSignUpSubHeaderAccount').click()
    WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((By.ID, 'idIptBktSignInlogin')))
    driver.find_element_by_id('idIptBktSignInlogin').send_keys(passport)
    driver.find_element_by_id('idIptBktSignInpassword').send_keys(password)
    driver.find_element_by_id('idBktDefaultSignInConfirmButton').click()
