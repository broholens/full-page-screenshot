"""
将网页保存为长图或pdf
1.使用selenium+chrome/phantomjs将html保存为image
2.使用wkhtmltox将网页保存为imageh或pdf
3.CS方式，上传html，返回pdf
"""

import imgkit  # pip install imgkit
import pdfkit  # pip install pdfkit
from selenium import webdriver  # pip install selenium
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def make_driver(driver='chrome'):
    """创建driver"""
    driver = driver.lower()
    if driver == 'chrome':
        # 初始化参数
        option = webdriver.ChromeOptions()
        option.add_argument('--headless')
        option.add_argument('--disable-gpu')
        option.add_argument("--hide-scrollbars")
        option.add_argument("--no-sandbox")
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        option.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"')
        d = webdriver.Chrome(options=option) 
    elif 'phantom' in driver:
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
        # phantomjs.exe位于同级目录下
        d = webdriver.PhantomJS(desired_capabilities=dcap)
    else:
        raise ValueError('Unknown argument %s. Support chrome and phantomjs only.' % driver)
    return d

def html2img_by_selenium(url, driver, output_file):
    """selenium将html存为图片"""
    driver.get(url)
    # 获取高度和宽度
    scroll_width = driver.execute_script('return document.body.parentNode.scrollWidth')
    scroll_height = driver.execute_script('return document.body.parentNode.scrollHeight')
    # 设置窗口尺寸
    driver.set_window_size(scroll_width, scroll_height)
    # 保存图片
    driver.save_screenshot(output_file)

def html2img_by_imgkit(url, output_file):
    """imgkit将html存为图片"""
    imgkit.from_url(url, output_file)

def html2pdf_by_pdfkit(url, output_file):
    """pdfkit将html存为pdf"""
    pdfkit.from_url(url, output_file)