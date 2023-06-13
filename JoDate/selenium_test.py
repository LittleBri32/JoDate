import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests as rs
import time
import unittest
from time import sleep #每跑一下休息

class TestClass(unittest.TestCase):
    def setUp(self):
        service = Service(r'./chromedriver')
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()
        
    def test_register(self):
        # 測試註冊供能
        url = 'https://jodate.weippig.com/'
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(5)

        self.driver.find_element(By.XPATH,'/html/body/div/div/div/main/div/form/div[3]/div/a').click()
        time.sleep(5)
        self.driver.find_element(By.ID,'uid').send_keys('111753113@g.nccu.edu.tw')
        self.driver.find_element(By.ID,'password').send_keys('abcd1234')
        self.driver.find_element(By.ID,'username').send_keys('Kevin')
        self.driver.find_element(By.ID,'check_password').send_keys('abcd1234')

        select_element =  self.driver.find_element(By.ID,'gender')
        select = Select(select_element)
        select.select_by_visible_text('男')

        self.driver.find_element(By.ID,'department').send_keys('資科系')
        self.driver.find_element(By.ID,'intro').send_keys('Hello')
        time.sleep(5)
        self.driver.find_element(By.ID,'btn').click()
        time.sleep(3)

        self.driver.find_element(By.CLASS_NAME,'swal2-confirm').click()
    
    def test_login(self):
        url = 'https://jodate.weippig.com/'
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(5)
        
        self.driver.find_element(By.ID,'email').send_keys('111753113@g.nccu.edu.tw')
        self.driver.find_element(By.ID,'password').send_keys('abcd1234')
        self.driver.find_element(By.CSS_SELECTOR,'.MuiButton-containedPrimary').click() #按Signin
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME,'swal2-confirm').click()
        time.sleep(3)

    def test_myProfile(self):
        url = 'https://jodate.weippig.com/'
        self.driver.get(url)
        self.driver.find_element(By.ID,'email').send_keys('111753113@g.nccu.edu.tw')
        self.driver.find_element(By.ID,'password').send_keys('abcd1234')
        self.driver.find_element(By.CSS_SELECTOR,'.MuiButton-containedPrimary').click() #按Signin
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME,'swal2-confirm').click()
        time.sleep(2)

        '''test_myProfile'''
        self.driver.find_element(By.CSS_SELECTOR,'.MuiButtonBase-root.MuiButton-root.MuiButton-text.MuiButton-textPrimary.MuiButton-sizeMedium.MuiButton-textSizeMedium.css-12bzubq').click()
        self.driver.get('https://jodate.weippig.com/profile')
        my_profile = self.driver.find_elements(By.CLASS_NAME,'main_wrap_leve6')
        time.sleep(2)
        for element in my_profile:
            print(element.text)  # 回傳：姓名:Kevin 性別:男 系所:資科系 信用值:100  (正確)

    def test_edit(self):
        url = 'https://jodate.weippig.com/'
        self.driver.get(url)
        self.driver.find_element(By.ID,'email').send_keys('111753113@g.nccu.edu.tw')
        self.driver.find_element(By.ID,'password').send_keys('abcd1234')
        self.driver.find_element(By.CSS_SELECTOR,'.MuiButton-containedPrimary').click() #按Signin
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME,'swal2-confirm').click()
        time.sleep(2)

        '''test_edit'''
        self.driver.get('https://jodate.weippig.com/edit')
        eidt_intro = self.driver.find_element(By.CLASS_NAME,  'MuiInputBase-input')
        #修改資料中的修改自我介紹 (因為屬性為被隱藏且可讀而已 只能用javascript去模擬輸入)
        self.driver.execute_script("arguments[0].value = 'This is Kevin';", eidt_intro)  
        time.sleep(2)

        edit_name = self.driver.find_element(By.ID,'userName')
        #修改資料中的修改用戶名稱 (因為屬性為被隱藏且可讀而已 只能用javascript去模擬輸入)
        self.driver.execute_script("arguments[0].value = 'Kevin';", edit_name) 
        time.sleep(2)

        # 點選提交（因為屬性不可被點選 因此用javascript模擬點選)
        # button = self.driver.find_element(By.CLASS_NAME, 'MuiButton-containedPrimary')   
        # self.driver.execute_script("arguments[0].click();", button)
        # self.driver.find_element(By.CLASS_NAME, 'swal2-confirm').click()  # ok 按鈕
        
    def test_create_group(self):
        url = 'https://jodate.weippig.com/'
        self.driver.get(url)
        self.driver.find_element(By.ID,'email').send_keys('111753113@g.nccu.edu.tw')
        self.driver.find_element(By.ID,'password').send_keys('abcd1234')
        self.driver.find_element(By.CSS_SELECTOR,'.MuiButton-containedPrimary').click() #按Signin
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME,'swal2-confirm').click()
        time.sleep(2)

        ''' test_creategroup '''
        self.driver.get('https://jodate.weippig.com/creategroup')
        # self.driver.find_element(By.ID, ':r6:').send_keys('一起去北車')    #揪團名稱

        input_field = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[3]/div/div/div[1]/div/div/input')
        input_field.clear()
        input_field.send_keys("一起去北車")
        time.sleep(3)

        discript_element = self.driver.find_element(By.CSS_SELECTOR,'textarea[class*="MuiInputBase-input"][class*="MuiOutlinedInput-input"   [class*="MuiInputBase-inputMultiline"]')
        discript_element.send_keys('6/18一起從政大搭車到北車')  #描述

        self.driver.find_element(By.ID, ':r5:').send_keys('政大麥側')  #地點

        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[3]/div/div/div[4]/div/div/div').click()
        dropdown_option = self.driver.find_element(By.XPATH, "//li[text()='拼車']")
        dropdown_option.click()
        time.sleep(2)

        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[3]/div/div/div[5]/div/div/div').click()
        dropdown_option2 = self.driver.find_element(By.XPATH, "//li[text()='1']")
        dropdown_option2.click()
        time.sleep(2)

        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[3]/div/div/div[6]/div/div/div').click()
        dropdown_option3 = self.driver.find_element(By.XPATH, "//li[text()='3']")
        dropdown_option3.click()
        time.sleep(2)
      
             
        input_element = self.driver.find_element(By.ID, ":r6:") #時間
        input_element.click()
        input_element.send_keys(Keys.LEFT)
        for _ in range(5):
            input_element.send_keys(Keys.LEFT)
            time.sleep(0.5)  # 延遲0.5秒以模擬連續按下的間隔
        input_element.send_keys(Keys.ARROW_UP)   #改月份

        self.driver.find_element(By.CLASS_NAME, 'MuiButton-contained').click()
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME,'swal2-confirm').click()
        time.sleep(5)
    
    def test_create_group_check(self):
        url = 'https://jodate.weippig.com/'
        self.driver.get(url)
        self.driver.find_element(By.ID,'email').send_keys('111753113@g.nccu.edu.tw')
        self.driver.find_element(By.ID,'password').send_keys('abcd1234')
        self.driver.find_element(By.CSS_SELECTOR,'.MuiButton-containedPrimary').click() #按Signin
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME,'swal2-confirm').click()
        time.sleep(2)

        # 確認是否創建成功 (測試過後創建成功)
        all_groups = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'MuiBox-root') and contains(@class, 'css-15f6i1g')]")
        if all_groups:
            last_group = all_groups[-1]
            print(last_group.text)
        else:
            print("找不到符合條件的元素")   
    
    def test_join_group(self):
        url = 'https://jodate.weippig.com/'
        self.driver.get(url)
        self.driver.find_element(By.ID,'email').send_keys('111753113@g.nccu.edu.tw')
        self.driver.find_element(By.ID,'password').send_keys('abcd1234')
        self.driver.find_element(By.CSS_SELECTOR,'.MuiButton-containedPrimary').click() #按Signin
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME,'swal2-confirm').click()
        time.sleep(2)

        element = self.driver.find_element(By.XPATH, "//a[@href='/groupdetail/2']")
        href = element.get_attribute('href')
        self.driver.get(href)

        # 加入
        button = self.driver.find_element(By.XPATH, "//button[contains(@class, 'MuiButton-containedPrimary')]") #加入
        button.click()
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME,'swal2-confirm').click()

        # 留言
        message_board = self.driver.find_element(By.XPATH, "//a[@href='/message/2']")
        href_2 = message_board.get_attribute('href')
        self.driver.get(href_2)
        sleep(3)
        self.driver.find_element(By.ID, "filled-multiline-static").send_keys('+1')
        sleep(2)
    
        submit_button = self.driver.find_element(By.XPATH, "//button[contains(text(), '送出')]")
        submit_button.click()
        time.sleep(2)
        
        # 檢查是否成功留言 (測試回傳正確)
        all_mes = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'MuiBox-root') and contains(@class, 'css-1oc44s6')]")
        if all_mes:
            last_group = all_mes[-1]
            print(last_group.text)
        else:
            print("找不到符合條件的元素")   
      
    def test_log_out(self):
        url = 'https://jodate.weippig.com/'
        self.driver.get(url)
        self.driver.find_element(By.ID,'email').send_keys('111753113@g.nccu.edu.tw')
        self.driver.find_element(By.ID,'password').send_keys('abcd1234')
        self.driver.find_element(By.CSS_SELECTOR,'.MuiButton-containedPrimary').click() #按Signin
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME,'swal2-confirm').click()
        time.sleep(2)

        '''登出'''
        profile_button = self.driver.find_element(By.XPATH, "//button[contains(text(), '我的個人檔案')]")
        profile_button.click()
        time.sleep(0.5)
        logout_element = self.driver.find_element(By.XPATH, "//li[contains(text(), '登出')]")
        logout_element.click()
        sleep(3)

if __name__ == '__main__':
    unittest.main()
