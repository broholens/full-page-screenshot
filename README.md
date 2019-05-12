### 将网页保存为pdf或者image
##### 因为一些文章会被作者或者平台强制删除，此项目旨在将还未删除的内容保存为image or pdf。  



#### 保存方式
- **selenium+chrome/phantomjs将网页存为图片**

  需要安装chromedriver/phantomjs，chromedriver的话还需要chrome浏览器

  ```python
  from capture_screen import make_driver, html2img_by_selenium
  
  driver = make_driver(driver='chrome')
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

  基于[WeasyPrint](http://weasyprint.org/)，具体参照[html2pdf-server](https://github.com/spoqa/html2pdf-server)



##### 参考链接
* [selenium+Phantomjs保存长图](https://www.cnblogs.com/Jack-cx/p/9405737.html) 
* [selenium+chrome图片拼接保存长图](https://www.cnblogs.com/sparkling-ly/p/5466644.html)
* [selenium+chrome设置window size保存长图](http://www.cnblogs.com/MasterMonkInTemple/p/9970512.html)
* [imgkit](https://github.com/jarrekk/imgkit)
* [pdfkit](https://github.com/JazzCore/python-pdfkit)
* [html2pdf-server](https://github.com/spoqa/html2pdf-server)