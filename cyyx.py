# -*- coding: utf-8 -*-
#通联数据中获取朝阳永续研报信息
from dataapi import Client
import pandas as pd
import os 
df = pd.read_csv('stock_base.csv')
df['code'] = df['code'].map(lambda x: str(x).zfill(6))
for intcode in df['code']:
    if __name__ == "__main__":
        try:
            stcode = str(intcode)
            client = Client()
            client.init('3ac6213396d593c5caae8639416051c450e60f17bdb4fdefec54ff4dc8f1c952') #通联数据凭证
            #url1='/api/report/getReportGG.csv?field=&orgName=&BeginWriteDate=20161001&EndwriteDate=20170205&secID=&ticker='+stcode+'&title=&author='
            #code, result = client.getData(url1)
            #if code==200:
                #print result
            #else:
                #print code
                #print result
            if os.path.isfile('cyyxreport\\'+stcode+'.csv') == False:
                url2='/api/report/getReportGG.csv?field=&orgName=&BeginWriteDate=20161001&EndwriteDate=20170205&secID=&ticker='+stcode+'&title=&author='
                code, result = client.getData(url2)
                if(code==200 and result != '-1:No Data Returned'):
                    file_object = open('cyyxreport\\'+stcode+'.csv', 'w')
                    file_object.write(result)
                    file_object.close( )
                else:
                    print code
                    print result
        except Exception, e:
            #traceback.print_exc()
            raise e
print 'get data ok'