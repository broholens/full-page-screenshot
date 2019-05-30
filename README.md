### 将网页保存为pdf或者image
##### 因为一些文章会被作者或者平台强制删除，此项目旨在将还未删除的内容保存为image or pdf。  



保存方式
---

- **selenium+chrome/phantomjs将网页存为图片**

  需要安装chromedriver/phantomjs，chromedriver的话还需要chrome浏览器

  ```python
  from pyfunctions.functions import make_driver  # pip install pyfunctions
  from capture_screen import html2img_by_selenium
  
  driver = make_driver(driver='chrome', load_img=True)
  url = 'https://www.baidu.com/'
  output_file = 'baidu.png'
  
  html2img_by_selenium(url, driver, output_file)
  ```

- **imgkit+wkhtmltoimage将网页存为图片**

  需要wkhtmltoimage

  ```python
  from capture_screen import html2img_by_imgkit
  
  url = 'https://www.baidu.com/'
  output_file = 'baidu.png'
  
  html2img_by_imgkit(url, output_file)
  ```


- **pdfkit+wkhtmltopdf**

  需要wkhtmltopdf

  ```python
  from capture_screen import html2img_by_pdfkit
  
  url = 'https://www.baidu.com/'
  output_file = 'baidu.pdf'
  
  html2img_by_imgkit(url, output_file)
  ```


- **html2pdf-server**

  基于WeasyPrint
  
  ```python
  from pyfunctions.functions import make_driver
  from capture_screen import html2pdf_by_server, html2img_by_server
  
  d = make_driver(driver='chrome', load_img=True)
  
  url = 'https://www.baidu.com/'
  output_pdf = 'baidu.pdf'
  output_png = 'baidu.png'

  html2img_by_server(d, url, output_png)
  html2pdf_by_server(d, url, output_pdf)
  ```

- **Full Page Screen Capture**
  ```text
  Chrome浏览器的一个全屏截取插件，支持image/pdf保存方式
  ```

- **splash**
  
  需要安装splash

  ```python
  from capture_screen import html2img_by_splash

  url = 'https://www.baidu.com/'
  output_file = 'baidu.png'
  
  html2img_by_splash(url, output_file)
  ```


Compare
---

| star | name | description |
| :---: | :---: | :---------: |
| 😁 | pdfkit | Works perfect on all tests. [Example][pdfkit] |
| 😭 | html2pdf-pdf | What a letdown! Works only on simple sites like [Baidu][baidu] |
| 😭 | html2pdf-img | What a letdown! Works only on simple sites like [Baidu][baidu] |
| 😔 | imgkit | Disappointed. At least on GitHub [Example][imgkit] |
| 😁 | splash | Works perfect on all tests. [Example][splash] |
| 😁 | selenium | Works perfect on all tests. [Example][selenium] |


参考链接
---

* [selenium+Phantomjs保存长图](https://www.cnblogs.com/Jack-cx/p/9405737.html) 
* [selenium+chrome图片拼接保存长图](https://www.cnblogs.com/sparkling-ly/p/5466644.html)
* [selenium+chrome设置window size保存长图](http://www.cnblogs.com/MasterMonkInTemple/p/9970512.html)
* [imgkit](https://github.com/jarrekk/imgkit)
* [pdfkit](https://github.com/JazzCore/python-pdfkit)
* [html2pdf-server](https://github.com/spoqa/html2pdf-server)
* [splash](https://splash.readthedocs.io/en/stable/api.html#render-html)
* [splash+requests](https://blog.csdn.net/mouday/article/details/82843401)

[pdfkit]: https://github.com/broholens/images/blob/master/pdfkit.pdf
[imgkit]: https://github.com/broholens/images/blob/master/imgkit.png
[splash]: https://github.com/broholens/images/blob/master/splash.png
[selenium]: https://github.com/broholens/images/blob/master/selenium.png
[baidu]: https://www.baidu.com