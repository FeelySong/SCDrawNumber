# coding=utf-8
import mysql.connector
from datetime import datetime
import logging

host='littlemonk.net'
port='3306'
user='root'
password='shl850325'
database='shijue'
charset='utf8'

logging.basicConfig(filename='/tmp/kaijiang.log',level=logging.INFO)
logging.basicConfig(filename='/tmp/errkj.log',level=logging.ERROR)

class MYSQL:
    def __init__(self):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    def __GetConnect(self):
        if not self.database:
            raise(NameError,"No DataBase Info")
        self.conn = mysql.connector.connect(host=self.host,port=self.port,user=self.user,password=self.password,database=self.database)
        cur = self.conn.cursor()
        if not cur:
            raise(NameError,"connect database failed")
        else:
            return cur

    def CallSP(self,kjCodes,lottery_type,lottery_num,kjtime):

        if(lottery_type =='8' or lottery_type=='6'): ##广东11选5 或者 11运夺金
            n1=int(kjCodes[0:2])
            n2=int(kjCodes[2:4])
            n3=int(kjCodes[4:6])
            n4=int(kjCodes[6:8])
            n5=int(kjCodes[8:10])
        elif(lottery_type=='5' or lottery_type=='9'):
            kjCodes=','.join(kjCodes)
            n1=int(kjCodes[0])
            n2=int(kjCodes[2])
            n3=int(kjCodes[4])
            n4=0
            n5=0
        else:
            kjCodes=','.join(kjCodes)
            n1=int(kjCodes[0])
            n2=int(kjCodes[2])
            n3=int(kjCodes[4])
            n4=int(kjCodes[6])
            n5=int(kjCodes[8])

        name=cidname(lottery_type)
        pra=(lottery_type,name,lottery_num,kjCodes,n1,n2,n3,n4,n5,kjtime,datetime.now())
        sql='INSERT INTO ssc_data(cid,name,issue,code,n1,n2,n3,n4,n5,opentime,addtime) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        zt='1'
        print lottery_type,name,lottery_num,kjCodes
        try:
            cur = self.__GetConnect()
            cur.execute(sql,pra)
            self.conn.commit()
            cur.callproc('PaiJiang',(n1,n2,n3,n4,n5,lottery_type,lottery_num,zt,))
            self.conn.commit()
            self.conn.close()
            return lottery_num
        except mysql.connector.Error as err:
            print err

#匹配彩种名称
def cidname(x):
    return {
        '1': '重庆时时彩',
        '2': '尚彩五分彩',
        '4': '江西时时彩',
        '9': '福彩3D',
        '6': '十一运夺金',
        '8': '广东11选5',
        '10': '排列三、五',
        '12': '尚彩分分彩',
    }[x]

# def kjdata(t2,cid,t1,t3):
#         cursor=cnx.cursor()
#         if(t2!=""):
#             if(cid =='8' or cid=='6'): ##广东11选5 或者 11运夺金
#                 n1=int(t2[0:2])
#                 n2=int(t2[2:4])
#                 n3=int(t2[4:6])
#                 n4=int(t2[6:8])
#                 n5=int(t2[8:10])
#             elif(cid=='5' or cid=='9'):
#                 t4=','.join(t2)
#                 n1=t4[0]
#                 n2=t4[2]
#                 n3=t4[4]
#                 n4=0
#                 n5=0
#                 n1=int(n1)
#                 n2=int(n2)
#                 n3=int(n3)
#             else:
#                 t4=','.join(t2)
#                 n1=t4[0]
#                 n2=t4[2]
#                 n3=t4[4]
#                 n4=t4[6]
#                 n5=t4[8]
#
#                 n1=int(n1)
#                 n2=int(n2)
#                 n3=int(n3)
#                 n4=int(n4)
#                 n5=int(n5)
#         # echo Get_lottery($cid)."第".$t1."期:".$t2."<br>";
#         sql = 'select * from ssc_data where cid=%s and issue=%s'
#         #echo $sql."<br>";
#         cursor.execute(sql,(cid,t1))
#         rowa = cursor.fetchone()
#         tts = 0
#         if(cid==1 or cid==2 or cid==3 or cid==4):
#             if (n1=="0" and n2=="0" and n3=="0" and n4=="0" and n5=="0"):
#                 tts = 1
#             if (n1>9 or n2>9 or n3>9 or n4>9 or n5>9):
#                 tts=1
#         elif(cid==5):
#             if (n1=="0" and n2=="0" and n3=="0"):
#                 tts=1
#             if (n1>9 or n2>9 or n3>9):
#                 tts=1
#         elif(cid==6 or cid==7 or cid==8 or cid==11):
#             if (n1=="0" and n2=="0" and n3=="0" and n4=="0" and n5=="0"):
#                 tts=1
#             if (n1>11 or n2>11 or n3>11 or n4>11 or n5>11):
#                 tts=1
#         elif(cid==9):
#             if(n1=="0" and n2=="0" and n3=="0"):
#                 tts=1
#             if(n1>9 or n2>9 or n3>9):
#                 tts=1
#         elif(cid==10):
#             if(n1=="0" and n2=="0" and n3=="0" and n4=="0" and n5=="0"):
#                 tts=1
#             if(n1>9 or n2>9 or n3>9 or n4>9 or n5>9):
#                 tts=1
#         name=cidname(cid)
#         print cid,name,t1,t2
#         #tmp='set cid='+cid+' name='+Get_lottery(cid), issue=t1, code='".$t2."', n1='".$n1."', n2='".$n2."', n3='".$n3."', n4='".$n4."', n5='".$n5."',opentime='".$t3."', addtime='".date("Y-m-d H:i:s")."'";
#         if(rowa is None):
#             if(tts==0):
#                 sql='INSERT INTO ssc_data(cid,name,issue,code,n1,n2,n3,n4,n5,opentime,addtime) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
#                 pra=(cid,name,t1,t2,n1,n2,n3,n4,n5,t3,datetime.now())
#                 try:
#                     cursor.execute(sql,pra)
#                     cnx.commit()
#                 except mysql.connector.Error as err:
#                     print err
#                 #t1=t1[2:]
#                 #print n1,n2,n3,n4,n5,cid,t1
#
#                 zt = '1'
#                 # php(str(n1),str(n2),str(n3),str(n4),str(n5),str(cid),str(t1),zt)
#
#                 # zt = '0'
#                 # print str(n1),str(n2),str(n3),str(n4),str(n5),str(cid),str(t1),zt
#                 # autokj.autokj(str(n1),str(n2),str(n3),str(n4),str(n5),str(cid),str(t1),zt)
#                 CallSP(str(n1),str(n2),str(n3),str(n4),str(n5),str(cid),str(t1),zt)
#
#         else:
#             if(rowa[10]!='1'):
#                 if(rowa[13]>5):
#                     pass
#                 else:
#                     sqls='update ssc_data set sign=sign+1 where id ='+str(rowa[0])
#                     cursor.execute(sqls)
#         return t1

# def CallSP(n1,n2,n3,n4,n5,lid,issue,sign):
#         cursor.callproc('PaiJiang',(n1,n2,n3,n4,n5,lid,issue,sign,))
#         # cursor.close()
#         # cnx.close()


'''
def kjdata360(t2,cid,t1,t3):
        if(t2!=""):
            t4=','.join(t2)
            print t4
            n1=t4[0]
            n2=t4[4]
            n3=t4[8]
            if(cid!=5 and cid!=9):
                n4=t4[12]
                n5=t4[16]
        n1=int(n1)
        n2=int(n2)
        n3=int(n3)
        n4=int(n4)
        n5=int(n5)
        # echo Get_lottery($cid)."第".$t1."期:".$t2."<br>";
        sql = 'select * from ssc_data where cid=%s and issue=%s'
        print sql
        #echo $sql."<br>";
        cursor.execute(sql,(cid,t1))
        rowa = cursor.fetchone()
        print rowa
        tts = 0
        if(cid==1 or cid==2 or cid==3 or cid==4):
            if (n1=="0" and n2=="0" and n3=="0" and n4=="0" and n5=="0"):
                tts = 1
            if (n1>9 or n2>9 or n3>9 or n4>9 or n5>9):
                tts=1
        elif(cid==5):
            if (n1=="0" and n2=="0" and n3=="0"):
                tts=1
            if (n1>9 or n2>9 or n3>9):
                tts=1
        elif(cid==6 or cid==7 or cid==8 or cid==11):
            if (n1=="0" and n2=="0" and n3=="0" and n4=="0" and n5=="0"):
                tts=1
            if (n1>11 or n2>11 or n3>11 or n4>11 or n5>11):
                tts=1
        elif(cid==9):
            if(n1=="0" and n2=="0" and n3=="0"):
                tts=1
            if(n1>9 or n2>9 or n3>9):
                tts=1
        elif(cid==10):
            if(n1=="0" and n2=="0" and n3=="0" and n4=="0" and n5=="0"):
                tts=1
            if(n1>9 or n2>9 or n3>9 or n4>9 or n5>9):
                tts=1
        name='重庆时时彩'
        print cid,name,t1,t2
        #tmp='set cid='+cid+' name='+Get_lottery(cid), issue=t1, code='".$t2."', n1='".$n1."', n2='".$n2."', n3='".$n3."', n4='".$n4."', n5='".$n5."',opentime='".$t3."', addtime='".date("Y-m-d H:i:s")."'";
        if(rowa is None):
            if(tts==0):
                sql='INSERT INTO ssc_data(cid,name,issue,code,n1,n2,n3,n4,n5,opentime,addtime) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                pra=(cid,name,t1,t2,n1,n2,n3,n4,n5,t3,datetime.now())
                cursor.execute(sql,pra)
                t1=t1[2:]
                print n1,n2,n3,n4,n5,cid,t1
                zt = '1'
                php(str(n1),str(n2),str(n3),str(n4),str(n5),str(cid),str(t1),zt)
        else:
            if(rowa[10]!='1'):
                if(rowa[13]>5):
                    pass
                else:
                    sqls='update ssc_data set sign=sign+1 where id ='+str(rowa[0])
                    cursor.execute(sqls)
        return t1
'''

# import subprocess
# import os
# #now_time=time.localtime()
# def php(n1,n2,n3,n4,n5,cid,t1,zt):
#     #t1=str(now_time.tm_year)+t1[2:6]+t1[7:10]
#     print t1
#     para=n1+' '+n2+' '+n3+' '+n4+' '+n5+' '+cid+' '+t1+' '+zt
#     print 'this is php',para
#     para1='php -f /Users/Feely/Documents/Develop/PHP/autokj/autokj.php '
#     # open process
#     p = subprocess.Popen([para1+para], shell=True,stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT, close_fds=True)
#
#     print p.stdout.read()
#     # read output
#     o = p.communicate()[0]
#     print 'exe php:'+o
#     logging.info('Execute PaiJiang Programe:'+o)
#     # kill process
#     try:
#         os.kill(p.pid, os.signal.SIGTERM)
#     except:
#         pass
#     # return
#     return o
#
# #autokj($n1,$n2,$n3,$n4,$n5,$cid,$t1,1);
# # p2='58199'
# # p1='140701089'
# # p3=datetime.now()
# #
# # kjdata(t2=p2,cid='1',t1=p1,t3=p3)