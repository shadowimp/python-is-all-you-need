

```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(open('index.html'))
soup = BeautifulSoup(page.content.decode('utf-8', 'ignore'), "lxml")

# soup all content 
soup

# text 
app_content = soup.p.text
```



### selenium

解决动态页面的加载问题

selenium+python自动化100-linux搭建selenium环境

https://cloud.tencent.com/developer/article/1514874

**安装selenium**

```
pip3 install selenium
```

**安装最新版chrome**

```
yum install google-chrome-stable_current_x86_64.rpm
```

安装**chromedriver驱动**

```
wget http://npm.taobao.org/mirrors/chromedriver/77.0.3865.40/chromedriver_linux64.zip

unzip chromedriver_linux64.zip # 解压zip

mv chromedriver /usr/bin/

#查看chromedriver版本号
chromedriver --version
```

test

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument('--headless')  # 无界面
chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在报错问题
chrome_options.add_argument('--disable-gpu')   # 禁用GPU硬件加速。如果软件渲染器没有就位，则GPU进程将不会启动。chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--window-size=1920,1080')  # 设置当前窗口的宽度和高度
chrome_options.add_argument('--disable-extensions')
cd_path = '/usr/chromedriver'

driver = webdriver.Chrome(executable_path=cd_path, options=chrome_options)
driver.get(url)
page = driver.page_source
```



```


```

