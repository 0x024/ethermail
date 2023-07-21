from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time,os,sqlite3
import urllib3

'''
You need to install the following environment on your ubuntu
pip3 install requests
pip3 install selenium
pip3 install urllib3
adduser vnc
addgroup vnc sudo
sudo apt install ubuntu-desktop -y
wget http://mirror.cs.uchicago.edu/google-chrome/pool/main/g/google-chrome-stable/google-chrome-stable_107.0.5304.68-1_amd64.deb
sudo dpkg -i google-chrome-stable_107.0.5304.68-1_amd64.deb
wget https://chromedriver.storage.googleapis.com/107.0.5304.62/chromedriver_linux64.zip
unzip chromedriver_linux64.zip 
cp chromedriver /usr/local/bin/
mkdir /home/vnc/ethermail /home/vnc/ethermail/tool
chmod 777 -R /home/vnc/ethermail/*
chmod 777 -R /home/vnc/ethermail/
'''
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def ethermail_run():
    pwd = os.getcwd()
    db_pwd = pwd + "/ethermail.db"
    conn = sqlite3.connect(db_pwd)
    c = conn.cursor()
    c.execute('SELECT * FROM ethermail;')
    rows = c.fetchall()
    count=1
    for i in rows[8000:10000]:
        secret_key = i[3].split(" ")
        address=i[1]
        print("count "+str(count))
        print("address："+str(address))
        #print("secret_key："+str(secret_key))
        EXTENSION_PATH = "/home/vnc/ethermail//tool/matemask.crx"
        WEB_DRIVER_PATH="/usr/local/bin/chromedriver"
        opt = webdriver.ChromeOptions()
        opt.add_extension(EXTENSION_PATH)
        driver = webdriver.Chrome(executable_path=WEB_DRIVER_PATH,options=opt)
        driver.set_window_size(height=1000,width=400)
        driver.set_window_position(x=800, y=0)
        driver.switch_to.window(driver.window_handles[0])
        delay = 10
        print("[ready,ready,ready]")
        print("click [metamask regeist]")
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/button')))
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/button').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[2]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button').click()
        time.sleep(1)
        secret_key_1 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-0"]')
        secret_key_1.send_keys(secret_key[0])
        secret_key_2 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-1"]')
        secret_key_2.send_keys(secret_key[1])
        secret_key_3 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-2"]')
        secret_key_3.send_keys(secret_key[2])
        secret_key_4 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-3"]')
        secret_key_4.send_keys(secret_key[3])
        secret_key_5 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-4"]')
        secret_key_5.send_keys(secret_key[4])
        secret_key_6 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-5"]')
        secret_key_6.send_keys(secret_key[5])
        secret_key_7 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-6"]')
        secret_key_7.send_keys(secret_key[6])
        secret_key_8 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-7"]')
        secret_key_8.send_keys(secret_key[7])
        secret_key_9 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-8"]')
        secret_key_9.send_keys(secret_key[8])
        secret_key_10 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-9"]')
        secret_key_10.send_keys(secret_key[9])
        secret_key_11 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-10"]')
        secret_key_11.send_keys(secret_key[10])
        secret_key_12 = driver.find_element(By.XPATH, '//*[@id="import-srp__srp-word-11"]')
        secret_key_12.send_keys(secret_key[11])
        password = driver.find_element(By.XPATH, '//*[@id="password"]')
        password.send_keys('abcd1234')
        password_confirmation = driver.find_element(By.XPATH, '//*[@id="confirm-password"]')
        password_confirmation.send_keys('abcd1234')
        driver.find_element(By.XPATH, '//*[@id="create-new-vault__terms-checkbox"]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div[2]/form/button').click()
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/button').click()
        driver.switch_to.window(driver.window_handles[1])
        print("input [web url]")
        driver.get("https://ethermail.io?afid=64b93c066741b54828e219e6")
        # change you inviteurl
        time.sleep(10)
        print("click [sign up for free]")
        driver.find_element(By.XPATH, '//*[@id="app"]/div/section[1]/div[3]/div[1]/div[3]/button').click()
        time.sleep(5)
        print("click [metamask icon]")
        driver.find_element(By.XPATH, '//*[@id="headlessui-dialog-panel-5"]/div/div/div/div/ul/li[1]/div/img').click()
        time.sleep(10)
        print("chang [windows 2]")
        driver.switch_to.window(driver.window_handles[2])
        print("click [metamask next]")
        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[3]/div[2]/button[2]').click()
        time.sleep(1)
        print("click [metamask connect]")
        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]').click()
        time.sleep(1)
        print("chang [windows 1]")
        driver.switch_to.window(driver.window_handles[1])
        print("click [sign now]")
        driver.find_element(By.XPATH, '//*[@id="headlessui-dialog-panel-5"]/div/div/button').click()
        time.sleep(5)
        try:
            print("chang [windows 2]")
            driver.switch_to.window(driver.window_handles[2])
            print("click [metamask sign]")
            driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[3]/button[2]').click()
            time.sleep(10)
            try:
                print("chang [windows 1]")
                driver.switch_to.window(driver.window_handles[1])
                print("click [NEXT]")
                driver.find_element(By.XPATH, '//*[@id="__nuxt"]/div/div[2]/div/div/div[2]/div/div/div/div[2]/button').click()
                print("input [Email]")
                email = driver.find_element(By.XPATH, '//*[@id="__nuxt"]/div/div[2]/div/div/div[2]/div/div/div/div/form/input')
                random_email="zw97073966@gmail.com"
                email.send_keys(random_email)
                print("click [NEXT]")
                driver.find_element(By.XPATH, '//*[@id="__nuxt"]/div/div[2]/div/div/div[2]/div/div/div/div/form/div[2]/button[1]').click()
                time.sleep(1)
                print("click [GREAT]")
                driver.find_element(By.XPATH, '//*[@id="__nuxt"]/div/div[2]/div/div/div[2]/div/div/div/div[2]/button').click()
                print("click [next]")
                driver.find_element(By.XPATH, '//*[@id="__nuxt"]/div/div[2]/div/div/div[2]/div/div/div/div/button').click()
                print("click [go to inbox]")
                driver.find_element(By.XPATH, '//*[@id="__nuxt"]/div/div[2]/div/div/div[2]/div/div/div/div[2]/button').click()
                time.sleep(1)
                print("click [next]")
                driver.find_element(By.XPATH, '//*[@id="__nuxt"]/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/button').click()
                time.sleep(2)
                print("click [Retrieve Encryption Keys]")
                driver.find_element(By.XPATH, '//*[@id="__nuxt"]/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/button').click()
                time.sleep(1)
                print("chang [windows 2]")
                driver.switch_to.window(driver.window_handles[2])
                print("click [metamask sign]")
                driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[3]/button[2]').click()
                print("click [finish]")
                c.execute("UPDATE ethermail SET status = '1' where address=='%s';"%(address))
                conn.commit()
                print("complate goodluck")
            except:
                print("address has benn sign up or have some problem")
                c.execute("UPDATE ethermail SET status = '2' where address=='%s';"%(address))
                conn.commit()
                print("opoos! someting wrong!")
        except:
                print("not relaod matemask sign")
                c.execute("UPDATE ethermail SET status = '3' where address=='%s';"%(address))
                conn.commit()
                print("*****************************************")
        count=count+1
        print("let`s get next one")
        driver.quit()


if __name__ == '__main__':
    ethermail_run()
