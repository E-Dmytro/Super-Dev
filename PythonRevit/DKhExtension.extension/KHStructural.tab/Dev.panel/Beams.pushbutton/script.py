# -*- coding: UTF-8 -*-
import os
location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
file = os.path.realpath(os.path.join(location + '/log.txt'))
from datetime import datetime

from rpw import revit
user = revit.username
with open(file, mode='a+') as csv_file:
    csv_file.writelines(str(user) + ' ' + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + '\n')
from module import *
# -*- coding: UTF-8 -*-
