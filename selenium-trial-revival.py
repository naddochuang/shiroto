from selenium import webdriver

geckodriver_path = r"C:\Users\Admin\AppData\Local\Programs\Python\Python39\Scripts\geckodriver.exe"
driver = webdriver.Firefox(executable_path=geckodriver_path)

driver.get('http://www.example.com')
print(driver.title)
driver.quit()
