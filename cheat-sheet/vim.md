正常模式 Normal-mode   : 使用vim打开文件后默认的模式



插入模式 insert-mode ： 在正常模式中按 i 进入

命令模式 command-mode

可视模式 visual-mode



```
control + a    jump to head 
control + e    jump to tail 
control + f    cursor forward 
control + b    cursor backward 
control + p    the previous command
control + n    the next command 

control + v		 到最后一行

control + h    delete 
control + d			向右删除一个字符
control + k     delete 后面的到行末尾
control + o    另起一行

control + t			交换前两个字母

https://blog.csdn.net/weixin_43274002/article/details/126513777
```



Terminal 快捷键



```bash
control + a    jump to head 
control + e    jump to tail 
control + f    cursor forward 
control + b    cursor backward 
control + l    clear 
control + h    delete 
control + w    delete word   # 删除光标左边的一个单词
control + u    delete the front of cursor 
control + k    delete the back if cursor 
control + Y              # 粘贴前面 CTRL+u/k/w 删除过的内容
control + y    paste the delete word 
control + p    the previous command
control + n    the next command 
contril + c    结束当前命令
CTRL+_              # 撤销（undo）

CTRL+D              # 同 <Delete> ，或者没有内容时，退出会话
CTRL+R              # 历史命令反向搜索，使用 CTRL+G 退出搜索
CTRL+S              # 历史命令正向搜索，使用 CTRL+G 退出搜索

CTRL+G              # 退出当前编辑（比如正在 CTRL+R 搜索历史时）

CTRL+T              # 交换前后两个字符
CTRL+O              # 类似回车，但是会显示下一行历史


i # 进入编辑模式
x #删除一个字符
r #替换一个字符

vim -d 
# 看两个文件

yy + p #复制一行


#行号
set number 
set nonumber 

set nu  # 显示行号
set nonu # 不显示行号

:1,10, <       #  1至10行左移4个字符间距

0 # 到行首
$ # 到行尾
L 光标移动到当前屏幕的尾部
w 光标移动到下一个单词的开头
fa 移动到fd本行下一个为 a 的字符处
4G 移动到第4行的行首
G 到最后一行
gg 到第一行	

hjkl :  左下上右




set paste  #进入复制模式
set nopaste # 关闭复制模式


vim 替换快捷键  map
在vim下用crtl-c和crtl-v复制粘贴

把下面代码放到vimrc文件里，就可以了。

# 自定义快捷键
map <C-c> "+y
map <C-v> "+p


d 删除
dd 删除一行
dw 删除一个单词
d$ 删除到行尾
dH 删除从开始到本行
dG 删除从本行到最后

y 复制
yw 复制一个单词
yy 复制一行
y$ 复制到本行结尾
yfa 复制到下一个a的字符处


p：粘贴
p 从光标后开始粘贴
P 从光标前开始粘贴




```





### vim 配置

```

vim ~/.vimrc

set filetype=python

au BufNewFile,BufRead *.py,*.pyw setf python

set autoindent " same level indent

set smartindent " next level indent

set expandtab

set tabstop=4

set shiftwidth=4

set softtabstop=4



### 

#set nocompatible # "去掉vi的一致性"

set number # "显示行号"
  
set guioptions-=r  # " 隐藏滚动条"  
set guioptions-=L
set guioptions-=b
"隐藏顶部标签栏"
set showtabline=0
"设置字体"
set guifont=Monaco:h13         
syntax on   "开启语法高亮"
let g:solarized_termcolors=256   #"solarized主题设置在终端下的设置"
set background=dark     "设置背景色"
colorscheme solarized
set nowrap  "设置不折行"
set fileformat=unix "设置以unix的格式保存文件"
set cindent     "设置C样式的缩进格式"
set tabstop=4   "设置table长度"
set shiftwidth=4        "同上"
set showmatch   "显示匹配的括号"
set scrolloff=5     "距离顶部和底部5行"
set laststatus=2    "命令行为两行"
set fenc=utf-8      "文件编码"
set backspace=2
set mouse=a     "启用鼠标"
set selection=exclusive
set selectmode=mouse,key
set matchtime=5
set ignorecase      "忽略大小写"
set incsearch
set hlsearch        "高亮搜索项"
set noexpandtab     "不允许扩展table"
set whichwrap+=<,>,h,l
set autoread
set cursorline      "突出显示当前行"
set cursorcolumn        "突出显示当前列"





```

### 