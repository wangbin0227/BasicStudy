### -*- encoding:utf8 -*-
import os
import sys
import json
DIR_THIS = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "demo file_name"
        print "例: demo test_list"
    else:
        file_name = sys.argv[1]
        if os.path.exists('./{}.py'.format(file_name)) == True:
            print "{}.py 已经存在了".format(file_name)
        else:
            code = file("{}/main.py".format(DIR_THIS), 'rb').read()
            code = code.replace("$file_name", file_name)
            file('./{}'.format(file_name), 'wb').write(code)
