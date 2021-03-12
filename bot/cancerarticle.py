import os
import random
import time
from random import randrange

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\chaiy\Downloads\chromedriver.exe")
baseURL = "https://www.copy.ai/sign-in"
driver.maximize_window()
driver.get(baseURL)

time.sleep(60)
# driver.find_element_by_xpath("/html/body/div[1]/div/div/a").click()
while True:
    try:
        driver.find_element_by_xpath("/html/body/div[10]/div/div[3]/form/div/div[2]/div[2]/div[2]/div[11]/div/div[1]/a").click()
    except:
        continue

    time.sleep(30)
    datastored = []

    for i in range(5+1):
        k = "idea-" + str(i)
        datastored.append(driver.find_element(By.ID, k).get_attribute("original_text"))

    filename = str(randrange(10)) + str(randrange(10)) + str(randrange(10)) +str(randrange(10)) +str(randrange(10)) +str(randrange(10)) + ".txt"
    wblog = open(filename , "w+")
    print("File Opened.")

    wblog.writelines(datastored)
    wblog.close()
    print("File Closed.")







"""
driver.find_element(By.ID, "txtNRIC").send_keys("T0037597C")
driver.find_element(By.ID, "txtPassword").send_keys("168816")
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/article/div/div/div/div/div[2]/div[1]/div/div/form/div/input").click()
driver.switch_to.frame("leftFrame")
time.sleep(2)
driver.find_element_by_link_text("Booking without Fixed Instructor").click()
time.sleep(2)
driver.switch_to.default_content()
time.sleep(2)
driver.switch_to.frame("mainFrame")
time.sleep(2)
driver.find_element_by_xpath("/html/body/table/tbody/tr[4]/td[1]/input").click()
driver.find_element_by_xpath("/html/body/table/tbody/tr/td[2]/form/table/tbody/tr[1]/td/table/tbody/tr[1]/td[2]/table/tbody/tr[4]/td[1]/input").click()
driver.find_element_by_xpath("/html/body/table/tbody/tr/td[2]/form/table/tbody/tr[1]/td/table/tbody/tr[3]/td[2]/input[9]").click()
driver.find_element_by_xpath("/html/body/table/tbody/tr/td[2]/form/table/tbody/tr[1]/td/table/tbody/tr[6]/td[2]/input").click()
driver.find_element_by_xpath("/html/body/table/tbody/tr/td[2]/form/table/tbody/tr[3]/td[2]/input").click()
driver.switch_to_alert().accept()
for i in driver.find_elements_by_xpath("/html/body/table/tbody/tr/td[2]/form/table[1]/tbody/tr[10]/td/table/tbody/tr[3]/td[1]"):
    print(i.getText())
"""
"""
frames=driver.find_elements_by_tag_name("iframe")
driver.switch_to.frame(frames[0]);
delay()

#click on checkbox to activate recaptcha
driver.find_element_by_class_name("recaptcha-checkbox-border").click()

#switch to recaptcha audio control frame
driver.switch_to.default_content()
frames=driver.find_element_by_xpath("/html/body/div[2]/div[4]").find_elements_by_tag_name("iframe")
driver.switch_to.frame(frames[0])
delay()

#click on audio challenge
driver.find_element_by_id("recaptcha-audio-button").click()

#switch to recaptcha audio challenge frame
driver.switch_to.default_content()
frames= driver.find_elements_by_tag_name("iframe")
driver.switch_to.frame(frames[-1])
delay()

#click on the play button
driver.find_element_by_xpath("/html/body/div/div/div[3]/div/button").click()
#get the mp3 audio file
src = driver.find_element_by_id("audio-source").get_attribute("src")
print("[INFO] Audio src: %s"%src)
#download the mp3 audio file from the source
urllib.request.urlretrieve(src, os.getcwd()+"\\sample.mp3")
sound = pydub.AudioSegment.from_mp3(os.getcwd()+"\\sample.mp3")
sound.export(os.getcwd()+"\\sample.wav", format="wav")
sample_audio = sr.AudioFile(os.getcwd()+"\\sample.wav")
r= sr.Recognizer()

with sample_audio as source:
    audio = r.record(source)

#translate audio to text with google voice recognition
key=r.recognize_google(audio)
print("[INFO] Recaptcha Passcode: %s"%key)

#key in results and submit
driver.find_element_by_id("audio-response").send_keys(key.lower())
driver.find_element_by_id("audio-response").send_keys(Keys.ENTER)
driver.switch_to.default_content()
delay()
driver.find_element_by_id("recaptcha-demo-submit").click()
delay()


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C:\\Users\chaiy\Downloads\chromedriver.exe")
baseURL = "https://info.bbdc.sg/members-login/"
driver.maximize_window()
driver.get(baseURL)
driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/article/div/div/div/div/div[2]/div[1]/div/div/form/input[2]").click()
driver.find_element(By.ID, "txtNRIC").send_keys("T0037597C")
driver.find_element(By.ID, "txtPassword").send_keys("168816")
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()
driver.switch_to.default_content()
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[title='recaptcha challenge']")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button#recaptcha-audio-button"))).click()
driver.switch_to.default_content()
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[title='recaptcha challenge']")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "rc-audiochallenge-tdownload-link"))).click()
"""
