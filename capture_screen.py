"""
将网页保存为长图或pdf
1.使用selenium+chrome/phantomjs将html保存为image
2.使用wkhtmltox将网页保存为imageh或pdf
3.CS方式，上传html，返回pdf
4. splash将html保存为image
"""

import time
import requests
import imgkit  # pip install imgkit
import pdfkit  # pip install pdfkit
from pyfunctions.functions import save_response_content


def html2img_by_selenium(driver, url, output_file):
    """selenium将html存为图片"""
    driver.get(url)
    time.sleep(2)
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

def html2img_by_splash(url, output_file):
    """Use splash request url and save screenshot as png file"""
    splash_url = "http://localhost:8050/render.png"
    params = {
        'url': url,
        'render_all': 1,
        'wait': 2,
        # 'timeout': 5
    }
    response = requests.get(splash_url, params=params)
    with open(output_file, 'wb') as f:
        f.write(response._content)

def html2pdf_by_server(driver, url, output_file):
    """save html to pdf with html2pdf-server"""
    driver.get(url)
    time.sleep(2)
    html = driver.page_source
    server_url = 'http://localhost:8080'
    header = {
        'Content-Type': 'text/html; charset=utf-8',
        'Accept': 'application/pdf',
    }
    response = requests.post(server_url, data=html.encode('utf-8'), headers=header)
    save_response_content(response, output_file)

def html2img_by_server(driver, url, output_file):
    """save html to image with html2pdf-server"""
    driver.get(url)
    time.sleep(2)
    html = driver.page_source
    server_url = 'http://localhost:8080'
    header = {
        'Content-Type': 'text/html; charset=utf-8',
        'Accept': 'image/png',
    }
    response = requests.post(server_url, data=html.encode('utf-8'), headers=header)
    save_response_content(response, output_file)

def test():
    """test all methods"""
    from pyfunctions.functions import make_driver

    d = make_driver(driver='chrome', load_img=True)

    url = 'https://github.com/broholens'
    pdfkit_output_pdf = 'pdfkit.pdf'
    server_output_pdf = 'server.pdf'
    imgkit_output_img = 'imgkit.png'
    selenium_output_img = 'selenium.png'
    server_output_img = 'server.png'
    splash_output_img = 'splash.png'

    html2img_by_imgkit(url, imgkit_output_img)
    html2pdf_by_pdfkit(url, pdfkit_output_pdf)
    html2img_by_splash(url, splash_output_img)
    html2img_by_selenium(d, url, selenium_output_img)
    html2img_by_server(d, url, server_output_img)
    html2pdf_by_server(d, url, server_output_pdf)

    d.quit()


if __name__ == '__main__':
    test()