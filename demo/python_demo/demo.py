### -*- encoding:utf8 -*-
import os
import sys
import json
from datetime import datetime

DIR_THIS = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "error!!!"
        print "python_demo file_name"
        print "例: python_demo test_list"
    else:
        file_name = sys.argv[1]
        if os.path.exists('./{}.py'.format(file_name)) == True:
            print "{}.py 已经存在了".format(file_name)
        else:
            cur_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            code = file("{}/main.py".format(DIR_THIS), 'rb').read()
            code = code.replace("$file_name", file_name)
            code = code.replace("$time", cur_time)
            file('./{}.py'.format(file_name), 'wb').write(code)
            print "Done"
            print "使用 python {}.py 运行".format(file_name)
