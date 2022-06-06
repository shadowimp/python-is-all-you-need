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


```

