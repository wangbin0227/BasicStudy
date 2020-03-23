### Mac 安装YouCompleteMe 
The ycmd server SHUT DOWN (restart with ‘:YcmRestartServer’). Unexpected exit code -11
原因：anaconda 与 YouCompleteMe冲突
解决方案是：使用内置的Python 执行 python install.py


### vim 配置python自动补全 mac
[参考文档](https://blog.csdn.net/apache0554/article/details/45752067)
```
wget https://github.com/rkulla/pydiction/archive/master.zip
unzip -q master
mv pydiction-master pydiction
mkdir -p ~/.vim/tools/pydiction
cp -r pydiction/after ~/.vim
cp pydiction/complete-dict ~/.vim/tools/pydiction
```

配置vimrc
filetype plugin on
let g:pydiction_location = '~/.vim/tools/pydiction/complete-dict'


### python命令行配置自动补全
[参考文档](https://www.cnblogs.com/ma6174/archive/2013/01/05/2845776.html)
在用户目录下新建".pythonstartup"文件，写入以下内容
```
import readline
import rlcompleter
import atexit
import os

readline.parse_and_bind('tab: complete')
#history file
historyfile = os.path.join(os.environ['HOME'],'.pythonstartup')
try:
    readline.read_history_file(historyfile)
except:
    pass
atexit.register(readline.write_history_file,historyfile)
del os,historyfile,readline,rlcompleter
```

增加环境变量
```
export PYTHONSTARTUP="/用户目录/.pythonstartup"
```

