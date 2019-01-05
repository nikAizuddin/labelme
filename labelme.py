# -*- coding: utf-8 -*-
import re
import sys
from os import path

from labelme.main import main

if __name__ == '__main__':
    sys.path.append(path.abspath(path.join("labelme")))
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(main())
