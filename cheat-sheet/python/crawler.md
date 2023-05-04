

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

selenium+python自动化100-linux搭建selenium环境

https://cloud.tencent.com/developer/article/1514874