
##############################################################################
# 常用快捷键（默认使用 Emacs 键位）
##############################################################################

CTRL+A              # 移动到行首，同 <Home>
CTRL+B              # 向后移动，同 <Left>
CTRL+C              # 结束当前命令
CTRL+D              # 删除光标前的字符，同 <Delete> ，或者没有内容时，退出会话
CTRL+E              # 移动到行末，同 <End>
CTRL+F              # 向前移动，同 <Right>
CTRL+G              # 退出当前编辑（比如正在 CTRL+R 搜索历史时）
CTRL+H              # 删除光标左边的字符，同 <Backspace>
CTRL+K              # 删除光标位置到行末的内容
CTRL+L              # 清屏并重新显示
CTRL+N              # 移动到命令历史的下一行，同 <Down>
CTRL+O              # 类似回车，但是会显示下一行历史
CTRL+P              # 移动到命令历史的上一行，同 <Up>
CTRL+R              # 历史命令反向搜索，使用 CTRL+G 退出搜索
CTRL+S              # 历史命令正向搜索，使用 CTRL+G 退出搜索
CTRL+T              # 交换前后两个字符
CTRL+U              # 删除字符到行首
CTRL+V              # 输入字符字面量，先按 CTRL+V 再按任意键
CTRL+W              # 删除光标左边的一个单词
CTRL+X              # 列出可能的补全
CTRL+Y              # 粘贴前面 CTRL+u/k/w 删除过的内容
CTRL+Z              # 暂停前台进程返回 bash，需要时可用 fg 将其切换回前台
CTRL+_              # 撤销（undo），有的终端将 CTRL+_ 映射为 CTRL+/ 或 CTRL+7

ALT+b               # 向后（左边）移动一个单词
ALT+d               # 删除光标后（右边）一个单词
ALT+f               # 向前（右边）移动一个单词
ALT+t               # 交换字符
ALT+BACKSPACE       # 删除光标前面一个单词，类似 CTRL+W，但不影响剪贴板

CTRL+X CTRL+X       # 连续按两次 CTRL+X，光标在当前位置和行首来回跳转 
CTRL+X CTRL+E       # 用你指定的编辑器，编辑当前命令


##############################################################################
# BASH 基本操作
##############################################################################

exit                # 退出当前登陆
env                 # 显示环境变量
echo $SHELL         # 显示你在使用什么 SHELL

bash                # 使用 bash，用 exit 返回
which bash          # 搜索 $PATH，查找哪个程序对应命令 bash
whereis bash        # 搜索可执行，头文件和帮助信息的位置，使用系统内建数据库
whatis bash         # 查看某个命令的解释，一句话告诉你这是干什么的

clear               # 清初屏幕内容
reset               # 重置终端（当你不小心 cat 了一个二进制，终端状态乱掉时使用）


##############################################################################
# 目录操作
##############################################################################

cd                  # 返回自己 $HOME 目录
cd {dirname}        # 进入目录
pwd                 # 显示当前所在目录
mkdir {dirname}     # 创建目录
mkdir -p {dirname}  # 递归创建目录
pushd {dirname}     # 目录压栈并进入新目录
popd                # 弹出并进入栈顶的目录
dirs -v             # 列出当前目录栈
cd -                # 回到之前的目录
cd -{N}             # 切换到目录栈中的第 N个目录，比如 cd -2 将切换到第二个


##############################################################################
# 文件操作
##############################################################################

ls                  # 显示当前目录内容，后面可接目录名：ls {dir} 显示指定目录
ls -l               # 列表方式显示目录内容，包括文件日期，大小，权限等信息
ls -a               # 显示所有文件和目录，包括隐藏文件（.开头的文件/目录名）
ln -s {fn} {link}   # 给指定文件创建一个软链接
cp {src} {dest}     # 拷贝文件，cp -r dir1 dir2 可以递归拷贝（目录）
rm {fn}             # 删除文件，rm -r 递归删除目录，rm -f 强制删除
mv {src} {dest}     # 移动文件，如果 dest 是目录，则移动，是文件名则覆盖
touch {fn}          # 创建或者更新一下制定文件
cat {fn}            # 输出文件原始内容
any_cmd > {fn}      # 执行任意命令并将标准输出重定向到指定文件
more {fn}           # 逐屏显示某文件内容，空格翻页，q 退出
less {fn}           # 更高级点的 more，更多操作，q 退出
head {fn}           # 显示文件头部数行，可用 head -3 abc.txt 显示头三行
tail {fn}           # 显示文件尾部数行，可用 tail -3 abc.txt 显示尾部三行
tail -f {fn}        # 持续显示文件尾部数据，可用于监控日志
nano {fn}           # 使用 nano 编辑器编辑文件
vim {fn}            # 使用 vim 编辑文件
diff {f1} {f2}      # 比较两个文件的内容
wc {fn}             # 统计文件有多少行，多少个单词
chmod 644 {fn}      # 修改文件权限为 644，可以接 -R 对目录循环改权限
chgrp group {fn}    # 修改文件所属的用户组
chown user1 {fn}    # 修改文件所有人为 user1, chown user1:group1 fn 可以修改组
file {fn}           # 检测文件的类型和编码
basename {fn}       # 查看文件的名字（不包括路径）
dirname {fn}        # 查看文件的路径（不包括名字）
grep {pat} {fn}     # 在文件中查找出现过 pat 的内容
grep -r {pat} .     # 在当前目录下递归查找所有出现过 pat 的文件内容
stat {fn}           # 显示文件的详细信息

