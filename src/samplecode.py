# -*- coding: utf-8 -*-
from dataapiclient import Client
from TL_download import getcode
import codecs
#import sys  
def Writecsv(path,data):
    
    datahead=data[:data.find('\n')]
    databody=data[data.find('\n') + 1:-1]

    dfile = open(path, 'a')
    dfile.write(codecs.BOM_UTF8)
    print >> dfile, databody
    dfile.close()
if __name__ == "__main__":
    try:
        
        clist=getcode()
        client = Client()
        client.init('3960d46d91b8439d2e0bad853d0aead6792bd09eae9d64329bfc86890454866d')
        for tickit_code in clist:
            url1='/api/fundamental/getFdmtBSCCXE.csv?field=&secID=&ticker='+tickit_code+'&publishDateBegin=&publishDateEnd=&beginDate=&endDate=&beginDateRep=&endDateRep='
            code, result = client.getData(url1)
            if code==200:
                Writecsv(u'D:\\data_dload\\资产负债表16-3.csv',result)
            else:
                print code
                print result
    except Exception, e:
        #traceback.print_exc()
        raise e
