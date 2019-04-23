"""使用pdfkit+wkhtmltopdf将网页保存为pdf
"""

import pdfkit  # pip install pdfkit

# 保存网页
pdfkit.from_url('https://www.baidu.com/', 'test.pdf')
