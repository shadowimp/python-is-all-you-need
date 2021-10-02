### Git

git的工作流

工作区：即自己当前分支所修改的代码，git add xx 之前的！不包括 git add xx 和 git commit xxx 之后的。

暂存区：已经 git add xxx 进去，且未 git commit xxx 的。

本地分支：已经git commit -m xxx 提交到本地分支的。

```bash
git status #  查看当前 git状态
git add . # 添加当前所有新增的文件
* 'git add --ignore-removal <pathspec>', which is the current default,
  ignores paths you removed from your working tree.

* 'git add --all <pathspec>' will let you also record the removals.
git commit -m "注释"
git push # 推送到github


git config --list #  显示当前的Git配置

git log # 查看所有提交历史
git log –p my_file # 查看某文件的提交历史

git push origin master  #push 代码



# 撤销，代码回滚
# 代码还未add
git checkout -- a.txt   # 丢弃某个文件， 撤销修改
git checkout -- .   #丢弃全部文件，新增的文件会被删除、删除的文件会恢复回来、修改的文件会回去。

# 文件git add到缓存区，并未commit提交
git reset HEAD a.txt	# 取消暂存 
git reset HEAD .   # 这个命令仅改变暂存区，并不改变工作区，

# git commit到本地分支、但没有git push到远程
git reset --hard	# 重置暂存区与工作区，与上一次 commit 保持一致
git reset --hard commit_id 	# 将代码回滚到当前commit_id的版本
git reset --hard HEAD^  # 回到最新的一次提交

# 已经用 git push把修改提交到远程仓库
git reset --hard <commit_id>
git push origin HEAD --force # 强制提交一次，之前错误的提交就从远程仓库删除


git stash	# 将目前改动的代码暂存起来
git pull origin master	# 从master拉代码
git stash pop	# 将之前的暂存改动与master上的代码合并， 并删除暂存的stash内容
git stash apply # 恢复，恢复后，stash内容并不删除，你要使用命令git stash drop来删除


git revert # 放弃指定提交的修改，但是会生成一次新的提交，需要填写提交注释，以前的历史记录都在；
```



##### Create a new repository

```bash
git clone http://git.intra.weibo.com/yuanbo6/ziding_handover.git
cd ziding_handover
touch README.md
git add README.md
git commit -m "add README"
git push -u origin master
```

##### Push an existing folder

```bash
cd existing_folder
git init
git remote add origin http://git.intra.weibo.com/yuanbo6/ziding_handover.git
git add .
git commit -m "Initial commit"
git push -u origin master


# 如果远程仓库已经有readme.md 首先运行
git pull origin master --allow-unrelated-histories
```

##### Push an existing Git repository

```bash
cd existing_repo
git remote rename origin old-origin
git remote add origin http://git.intra.weibo.com/yuanbo6/ziding_handover.git
git push -u origin --all
git push -u origin --tags
```



### 免密码push

```bash
git config  --global credential.helper store

#查看配置:
git config --list
#如果有下面的行，说明配置成功了:
credential.helper=store

#后面操作的时候只需要输入一次密码之后，就可以免密码操作了。
```



### git ignore 

```bash
# 创建文件 .gitignore  ,vim .gitignore或touch .gitignore命令
向其中添加不想上传到git 的文件


以斜杠/开头表示目录

*.zip 过滤所有.zip文件

# 最后一步就是把.gitignore也提交到Git
```

### branch

```bash
 git branch #查看branch
 git branch -a  # 查看所有分支，包括本地和远程分支
 
git branch yuanbo6	#创建分支yuanbo6
git checkout yuanbo6	#切换到分支yuanbo6
git push origin yuanbo6:yuanbo6 # 将分支yuanbo6的代码push到远程yuanbo6的分支上

# 删除远程分支
git push origin --delete yuanbo6

# 新建本地分支
git checkout -b localbranch


```

