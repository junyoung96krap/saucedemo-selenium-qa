# https://www.saucedemo.com/
# saucedemo 웹 페이지

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

result_pass_list = [] # PASS 된 TC LIST
result_fail_list = [] # FAIL 된 TC LIST
fail_reason_list = [] # FAIL 된 TC 사유 LIST

try:
    # TC_001 :: 웹 페이지 접속 여부 확인 TC
    try:
        tc_progress = 'TC_001'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get('https://www.saucedemo.com/')

        # 접속 후 user_name 찾기
        driver.find_element(By.ID, 'user-name')

        print(f'웹 페이지 접속 성공, PASS')
        result_pass_list.append(tc_progress)

    except Exception as e :
        fail_reason = '웹페이지 접속 실패 FAIL'
        print(f'{fail_reason}, FAIL')
        result_fail_list.append(tc_progress)
        fail_reason_list.append(f'{tc_progress} : {fail_reason}')

    # TC_002 :: 정상적인 로그인 확인 여부
    try:
        tc_progress = 'TC_002'

        id_input = driver.find_element(By.ID, 'user-name')
        id_input.send_keys('standard_user')
        pw_input = driver.find_element(By.ID, 'password')
        pw_input.send_keys('secret_sauce')

        driver.find_element(By.CLASS_NAME, 'submit-button').click()
        driver.implicitly_wait(10)
        if driver.find_element(By.CLASS_NAME, 'title').is_displayed():
            print(f'로그인 성공, PASS')
            result_pass_list.append(tc_progress)
        else:
            fail_reason = '상품 목록 미표시'
            print(f'{fail_reason}, FAIL')        
            result_fail_list.append(tc_progress)
            fail_reason_list.append(f'{tc_progress} : {fail_reason}') 

    except Exception as e :
        fail_reason = '로그인 실패'
        print(f'{fail_reason}, FAIL')
        result_fail_list.append(tc_progress)
        fail_reason_list.append(f'{tc_progress} : {fail_reason}') 

    # TC_003 :: FAIL 결과 확인을 위한 로그인 실패 테스트
    try:
        tc_progress = 'TC_003'

        driver.find_element(By.ID, 'react-burger-menu-btn').click()
        driver.find_element(By.CSS_SELECTOR, '#logout_sidebar_link').click()
    
        id_input = driver.find_element(By.ID, 'user-name')
        id_input.send_keys('standard_user')
        pw_input = driver.find_element(By.ID, 'password')
        pw_input.send_keys('asd')
    
        driver.find_element(By.CLASS_NAME, 'submit-button').click()
        driver.implicitly_wait(10)
        if driver.find_element(By.CLASS_NAME, 'title').is_displayed():
            print(f'로그인 성공, PASS')
            result_pass_list.append(tc_progress)
        else:
            fail_reason = '상품 목록 미표시'
            print(f'{fail_reason}, FAIL')
            result_fail_list.append(tc_progress)
            fail_reason_list.append(f'{tc_progress} : {fail_reason}') 
            
    
    except Exception as e :
        fail_reason = '로그인 실패'
        print(f'{fail_reason}, FAIL')
        result_fail_list.append(tc_progress)
        fail_reason_list.append(f'{tc_progress} : {fail_reason}') 

    # TC_004 :: 상품 목록 확인
    try: 
        tc_progress = 'TC_004'

        id_input = driver.find_element(By.ID, 'user-name')
        id_input.clear()
        id_input.send_keys('standard_user')
        pw_input = driver.find_element(By.ID, 'password')    
        pw_input.clear()
        pw_input.send_keys('secret_sauce')

        driver.find_element(By.CLASS_NAME, 'submit-button').click()
        driver.implicitly_wait(10)

        product_list = driver.find_elements(By.CLASS_NAME, 'inventory_item')
        if len(product_list) > 0:
            print(f'{len(product_list)} 개 : 상품 목록 출력, PASS')
            result_pass_list.append(tc_progress)
        else:
            fail_reason = '상품 목록 미출력'
            result_fail_list.append(tc_progress)
            fail_reason_list.append(f'{tc_progress} : {fail_reason}')
            print(f'{fail_reason}, FAIL')
    except Exception as e :
        fail_reason = '상품 목록 확인 중 오류 발생'
        print(f'{fail_reason}, FAIL')
        result_fail_list.append(tc_progress)
        fail_reason_list.append(f'{tc_progress} : {fail_reason}')

    time.sleep(10)
    
except Exception as e:
    print(f'에러 발생! 테스트 스크립트 종료')
