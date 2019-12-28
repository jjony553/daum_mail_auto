from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time

options = webdriver.ChromeOptions()

URL = 'https://www.daum.net/'
ID ='아이디입력'
PASSWORD = '비밀번호입력'

#URL열기
driver = webdriver.Chrome(r'C:\Users\whdgu\Desktop\selenium\chromedriver.exe')#크롬드라이버 주소
driver.get(URL)
#driver.maximize_window() #창 제일 크게 열기
action = ActionChains(driver) #driver 제어

#로그인인 화면으로 이동
driver.get("https://logins.daum.net/accounts/dsso.do?url=https%3A%2F%2Fwww.daum.net%2F")
time.sleep(2)

#아이디, 비밀번호 입력
driver.find_element_by_id('id').send_keys(ID)
driver.find_element_by_id('inputPwd').send_keys(PASSWORD)
driver.find_element_by_id('loginBtn').click()
time.sleep(2)

#메일 보내기 이동
driver.get('https://mail.daum.net/')
time.sleep(2)
driver.find_element_by_css_selector('.btn_comm.btn_write').click() #메일쓰기 버튼
time.sleep(2)


#메시지 보내기
(
action.send_keys('wlqndzlr94@daum.net').key_down(Keys.TAB).pause(1).key_down(Keys.TAB).key_down(Keys.TAB)#보낼 이메일주소
.send_keys('제목입니다.').key_down(Keys.TAB)#제목입력 부분
.send_keys('메크로메일').key_down(Keys.ENTER)#내용입력 부분
.key_down(Keys.SHIFT).send_keys('a') #대문자 변경시
.perform()
)

driver.find_element_by_css_selector('.btn_toolbar.btn_write').click() #보내기 버튼
driver.close()
