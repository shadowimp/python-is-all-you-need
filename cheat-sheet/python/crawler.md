

```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(open('index.html'))
soup = BeautifulSoup(page.content.decode('utf-8', 'ignore'), "lxml")

# soup all content 
soup

# text 
app_content = soup.p.text


# tag 的 .content 属性可以将tag的子节点以列表的方式输出
print soup.head.contents 

for child in soup.body.children:
  print child
  
  
  for child in soup.descendants:
  print child
  
  
  soup.find('div').find('aside')
```



### selenium

解决动态页面的加载问题

selenium+python自动化100-linux搭建selenium环境

https://cloud.tencent.com/developer/article/1514874

**安装selenium**

```
pip3 install selenium
pip install webdriver_manager
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



```python
# 等待1s加载
driver.implicitly_wait(1) #最多10秒
 

# 退出
driver.close() - closes the browser active window.

driver.quit() - closes all browser windows and ends driver's session/process.
```









```python
def parse():
    r = session.get('http://www.qdaily.com/')
    # 获取首页新闻标签、图片、标题、发布时间
    for x in r.html.find('.packery-item'):
        yield {
            'tag': x.find('.category')[0].text,
            'image': x.find('.lazyload')[0].attrs['data-src'],
            'title': x.find('.smart-dotdotdot')[0].text if x.find('.smart-dotdotdot') else x.find('.smart-lines')[0].text,
            'addtime': x.find('.smart-date')[0].attrs['data-origindate'][:-6]
        }
```







### 安装中文字体

```
https://www.cnblogs.com/helios-fz/p/13706157.html

https://www.cnblogs.com/yanjieli/p/10119900.html#:~:text=Windows%E5%AD%97%E4%BD%93%E5%8C%85%E4%B8%8B%E8%BD%BD%E9%93%BE%E6%8E%A5%EF%BC%9A%20https%3A%2F%2Fpan.baidu.com%2Fs%2F1ks9a70snHo02CTuqTrQhhg%20%E6%8F%90%E5%8F%96%E7%A0%81%EF%BC%9A7aw5%20%EF%BC%881%EF%BC%89%E5%9C%A8%2Fusr%2Fshare%2Ffonts%2F%E4%B8%8B%E5%88%9B%E5%BB%BA%E4%B8%80%E4%B8%AA%E7%9B%AE%E5%BD%95%E5%AD%98%E6%94%BEWindows%E5%AD%97%E4%BD%93%20%23%20mkdir%20%2Fusr%2Fshare%2Ffonts%2Fwinfonts%2F%20%EF%BC%882%EF%BC%89%E5%B0%86%E5%AD%97%E4%BD%93%E4%B8%8A%E4%BC%A0%E5%88%B0%E5%88%9B%E5%BB%BA%E5%A5%BD%E7%9A%84%E7%9B%AE%E5%BD%95%E5%B9%B6%E8%A7%A3%E5%8E%8B,%23%20cd%20%2Fusr%2Fshare%2Ffonts%2Fwinfonts%2F%20%23%20tar%20xf%20Windows_fonts.%20tar.gz

https://learnku.com/articles/50665
```

```
sudo yum -y install fontconfig

cd /usr/share/fonts

sudo mkdir chinese

chmod -R 755 /usr/share/fonts/chinese

mv SanJiJinSongJianTi-2.ttf /usr/share/fonts/chinese

sudo yum -y install ttmkfdir
sudo ttmkfdir -e /usr/share/X11/fonts/encodings/encodings.dir


fc-cache

fc-list|grep chinese
```





```
# 手机 user agent 
http://fynas.com/ua
```

