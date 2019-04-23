"""imgkit+wkhtmltopdf将网页保存为图片
"""

import imgkit  # pip install imgkit

# 保存网页为图片
imgkit.from_url('https://www.baidu.com', 'test.png')
