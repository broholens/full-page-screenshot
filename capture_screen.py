from selenium import webdriver

# 初始化参数
option = webdriver.ChromeOptions()
option.add_argument('--headless')
option.add_argument('--disable-gpu')
option.add_argument("--window-size=1280,1024")
option.add_argument("--hide-scrollbars")
option.add_argument("--no-sandbox")
 
driver = webdriver.Chrome(options=option) 
driver.get('https://www.cnblogs.com/fengyiru6369/p/7234840.html')
 
# 获取高度和宽度
scroll_width = driver.execute_script('return document.body.parentNode.scrollWidth')
scroll_height = driver.execute_script('return document.body.parentNode.scrollHeight')
# 设置窗口尺寸
driver.set_window_size(scroll_width, scroll_height)
# 保存图片
driver.save_screenshot('test.png')
driver.quit()
