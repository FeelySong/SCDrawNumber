# coding=utf-8

import conn
import mysql.connector
from datetime import datetime

cnx=mysql.connector.connect(user='root',password='shl850325',host='littlemonk.net',database='shijue',charset='utf8')
cursor=cnx.cursor(dictionary=True)

query='select * from ssc_set where lid=1'
cursor.execute(query)
result=cursor.fetchone()

na=[]
nb=[]
def  autokj(n1,n2,n3,n4,n5,lid,issue,sign):
    if(sign==1):
        signa=1
        signb=2
    else:
        signa=0
        signb=0
    if(lid==1 or lid==2 or lid==3 or lid==4 or lid==10):
        kjcode=n1+n2+n3+n4+n5
    elif (lid==5 or lid==9):
        kjcode=n1+n2+n3
    elif (lid==6 or lid==7 or lid==8 or lid==11):
        kjcode=n1+" "+n2+" "+n3+" "+n4+" "+n5

    na.append(n1)
    na.append(n2)
    na.append(n3)
    na.append(n4)
    na.append(n5)

    nb.append(n1)
    nb.append(n2)
    nb.append(n3)
    nb.append(n4)
    nb.append(n5)

    i=0
    j=0
    for i in range(0,5):
        for j in range (4,j>i,-1):
            if (nb[j]<nb[j-1]):
                temp0=nb[j]
                nb[j]=nb[j-1]
                nb[j-1] =temp0
    sql='select * from ssc_bills where lotteryid='+lid+' and issue='+issue+' and zt=0 order by id asc'
    conn.cursor.execute (sql)
    #此处注意是赋值，还是比较
    row = conn.cursor.fetchall()
    print row
    while (row):
        uid_fx=row['uid']
        regup_fx=row['regup']
        mid=row['mid']
        if (row['mode']=='1'):
            modes=1
        elif (row['mode']=='2'):
            modes=0.1
        elif (row['mode']=="3"):
            modes=0.01
        #五星
        if(mid=="400" or mid=="420" or mid=="440" or mid=="460"):
            stra=row['codes'].split('|')
            nums=0
            for i in range(0,len(stra)):
                strb=stra[i].split('&')
                for ii in range(0,len(strb)):
                    if(strb[ii]==na[i]):
                        nums=nums+1
            if(nums==5):
                conn.cursor.execute("update ssc_bills set zt="+signa+",prize=rates*times where id="+row['id'])
                print '1'
            else:
                conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
        #前四
        elif (mid=="401" or mid=="421" or mid=="441" or mid=="461"):
            stra=row['codes'].split('|')
            nums=0
            for i in range(0,len(stra)):
                strb=stra[i].split('&')
                for ii in range(0,len(strb)):
                    if(strb[ii]==na[i]):
                        nums=nums+1
            if(nums==4):
                conn.cursor.execute("update ssc_bills set zt="+signa+",prize=rates*times where id="+row['id'])
                print '1'
            else:
                conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
        #后四
        elif (mid=="402" or mid=="422" or mid=="442" or mid=="462"):
            stra=row['codes'].split('|')
            nums=0
            for i in range(0,len(stra)):
                strb=stra[i].split('&')
                for ii in range(0,len(strb)):
                    if(strb[ii]==na[i+1]):
                        nums=nums+1
            if(nums==4):
                conn.cursor.execute("update ssc_bills set zt="+signa+",prize=rates*times where id="+row['id'])
                print '1'
            else:
                conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
        #中三
        elif(mid=="403" or mid=="423" or mid=="443" or mid=="463"):
            #中三单式
            if(row['type']=="input"):
                cs=n2+n3+n4
                if(cs.find(row['codes'])==-1):
                    conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
                else:
                    conn.cursor.execute("update ssc_bills set zt="+signa+",prize=rates*times where id="+row['id'])
            #中三复式
            elif (row['type']=="digital"):
                stra=row['codes'].split('|')
            nums=0
            for i in range(0,len(stra)):
                strb=stra[i].split('&')
                for ii in range(0,len(strb)):
                    if(strb[ii]==na[i]):
                        nums=nums+1
            if(nums==3):
                conn.cursor.execute("update ssc_bills set zt="+signa+",prize=rates*times where id="+row['id'])
                print '1'
            else:
                conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
        #中三和值
        elif (mid=="404" or mid=="424" or mid=="444" or mid=="464"):
            zt=2
            cs=n2+n3+n4
            stra=row['codes'].split('&')
            for i in range(0,len(stra)):
                if(stra[i]==cs):
                    zt=1
                    break
            if(zt=="1"):
                conn.cursor.execute("update ssc_bills set zt="+signa+",prize=rates*times where id="+row['id'])
            else:
                conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
        #中组三
        elif (mid=="405" or mid=="425" or mid=="445" or mid=="465"):
            nums=0
            if(n2==n3 or n2==n4 or n3==n4):
                stra=row['codes'].split('&')
                for i in range(0,len(stra)):
                    if(stra[i]==n2 or stra[i]==n3 or stra[i]==n4):
                        nums=nums+1
            if(nums>=2):
                conn.cursor.execute("update ssc_bills set zt="+signa+",prize=rates*times where id="+row['id'])
            else:
                conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
        #中组六
        elif(mid=="406" or mid=="426" or mid=="446" or mid=="466"):
            nums=0
            stra=row['codes'].split('&')
            for i in range(0,len(stra)):
                if(stra[i]==n2 or stra[i]==n3 or stra[i]==n4):
                    nums=nums+1
            if(nums>=3):
                conn.cursor.execute("update ssc_bills set zt="+signa+",prize=rates*times where id="+row['id'])
            else:
                conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
        #中三组选，混合 inputok 168时时乐混合组选 298 3d 326p3
        elif (mid=="407" or mid=="427" or mid=="447" or mid=="467"):
            zt=2
            if (row['codes'].find(n2+n3+n4)==-1 and row['codes'].find(n2+n4+n3)==-1 and row['codes'].find(n3+n2+n4)==-1 and row['codes'].find(n3+n4+n2)==-1 and row['codes'].find(n4+n2+n3)==-1 and row['codes'].find(n4+n3+n2)==-1):
                conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
            else:
                rates=Get_rate(mid).split('')
                #组三
                if(n2==n3 or n2==n4 or n3==n4):
                    conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+str((rates[0]*modes))+"*times where id="+row['id'])
                else:
                    conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+str(rates[1]*modes)+"*times where id="+row['id'])
        #中三组合值
        elif(mid=="408" or mid=="428" or mid=="448" or mid=="468"):
            zt=2
            cs=n2+n3+n4
            stra=row['codes'].split('&')
            for i in range(0,len(stra)):
                if(stra[i]==cs):
                    zt=1
                    break
            if(zt=="1"):
                rates=Get_rate(mid).split('&')
                #组3
                if(n2==n3 or n2==n4 or n3==n4):
                    conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+str((rates[0]*modes))+"*times where id="+row['id'])
                else:
                    conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+str(rates[1]*modes)+"*times where id="+row['id'])
            else:
                conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
        #百家乐
        elif (mid=="409" or mid=="429" or mid=="449" or mid=="469"):
            na1a="zzz"
            na2a="zzz"
            na3a="zzz"
            na4a="zzz"
            na1b="zzz"
            na2b="zzz"
            na3b="zzz"
            na4b="zzz"

            if(n1+n2>n4+n5):
                na1a="庄闲"
            if(n1+n2<n4+n5):
                na1b="庄闲"

            if(n1==n2):
                na2a="对子"
            if(n4==n5):
                na2b="对子"

            if(n1==n2 and n1==n3):
                na3a="豹子"
            if(n3==n4 and n4==n5):
                na3b="豹子"

            if(n1+n2==8 or n1+n2==9):
                na4a="天王"
            if(n4+n5==8 or n4+n5==9):
                na4b="天王"

            stra=row['codes'].split('|')
            numa=0
            strb=stra[0].split('&')
            rates=Get_rate(mid).split("")

            for ii in range(0,len(strb)):
                if(strb[ii]==na1a):
                    numa=numa+rates[0]
                elif (strb[ii]==na2a):
                    numa=numa+rates[1]
                elif(strb[ii]==na3a):
                    numa=numa+rates[2]
                elif(strb[ii]==na4a):
                    numa=numa+rates[3]

            strb=stra[1].split("&")
            for ii in range(0,len((strb))):
                if(strb[ii]==na1b):
                    numa=numa+rates[0]
                elif(strb[ii]==na2b):
                    numa=numa+rates[1]
                elif(strb[ii]==na3b):
                    numa=numa+rates[2]
                elif(strb[ii]==na4b):
                    numa=numa+rates[3]

            if(numa>0):
                conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+numa*modes+"*times where id="+row['id'])
            else:
                conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
        #任三
        elif(mid=="410" or mid=="430" or mid=="450" or mid=="470"):
            stra=row['codes'].split("|")
            nums=0
            for i in range(0,len(stra)):
                strb=stra[i].split("&")
                for ii in range(0,len(strb)):
                    if(strb[ii]==na[i]):
                        nums=nums+1
            if(nums==3):
                conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+rates+"*times where id="+row['id'])
            else:
                conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
        #任二
        elif(mid=="411" or mid=="431" or mid=="451" or mid=="471"):
            stra=row['codes'].split("|")
            nums=0
            for i in range(0,len(stra)):
                strb=stra[i].split("&")
                for ii in range(0,len(strb)):
                    if(strb[ii]==na[i]):
                        nums=nums+1

            if(nums==2):
                conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+rates+"*times where id="+row['id'])
            else:
                conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])

        #前三直选ok164时时乐2943d 322p3
        elif(mid=="14" or mid=="52" or mid=="90" or mid=="128" or mid=="164" or mid=="294" or mid=="322"):
            #单式
            if(row['type']=="input"):
                cs=n1.n2.n3
                if(cs.find(row['codes'])==-1):
                    conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
                else:
                    conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+rates+"*times where id="+row['id'])
             #复式
            elif(row['type']=="digital"):
                stra=row['codes'].split("|")
                nums=0

                for i in range(0,len(stra)):
                    strb=stra[i].split("&")
                    for ii in range(0,len(strb)):
                        if(strb[ii]==na[i]):
                            nums=nums+1

                if(nums==3):
                    conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+rates+"*times where id="+row['id'])
                else:
                    conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])

        #前三和值ok165时时乐直选合值 295 3d 323p3
        elif(mid=="15" or mid=="53" or mid=="91" or mid=="129" or mid=="165" or mid=="295" or mid=="323"):
            zt=2
            cs=n1+n2+n3
            stra=row['codes'].split("&")
            for i in range(0,len(stra)):
                if(stra[i]==cs):
                    zt=1
                    break


            if(zt=="1"):
                conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+rates+"*times where id="+row['id'])
            else:
                conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
        #后三直选
        elif(mid=="16" or mid=="54" or mid=="92" or mid=="130"):
            #单式
            if(row['type']=="input"):
                cs=n3.n4.n5
                if(cs.find(row['codes'])==-1):
                    conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
                else:
                    conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+rates+"*times where id="+row['id'])
            #复式
            elif(row['type']=="digital"):
                stra=row['codes'].split("|")
                nums=0
                for i in range(0,len(stra)):
                    strb=stra[i].split("&")
                    for ii in range(0,len(strb)):
                        if(strb[ii]==na[i+2]):
                            nums=nums+1

                if(nums==3):
                    conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+rates+"*times where id="+row['id'])
                else:
                    conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
        #后三和
        elif(mid=="17" or mid=="55" or mid=="93" or mid=="131"):
            zt=2
            cs=n3+n4+n5
            stra=stra=row['codes'].split('&')
            for i in range(0,len(stra)):
                if(stra[i]==cs):
                    zt=1
                    break

            if(zt=="1"):
                conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+rates+"*times where id="+row['id'])
            else:
                conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
        #前组三ok 166时时乐组3 296 3d 324 p3
        elif(mid=="18" or mid=="56" or mid=="94" or mid=="132" or mid=="166" or mid=="296" or mid=="324"):
            nums=0
            if(n1==n2 or n1==n3 or n2==n3):
                stra=row['codes'].split('&')
                for i in range(0,len(stra)):
                    if(stra[i]==n1 or stra[i]==n2 or stra[i]==n3):
                        nums=nums+1

            if(nums>=2):
                conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+rates+"*times where id="+row['id'])
            else:
                conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
        #前组六ok 167时时乐组6 297 3d 325 p3
        elif(mid=="19" or mid=="57" or mid=="95" or mid=="133" or mid=="167" or mid=="297" or mid=="325"):
            nums=0
            if(n1!=n2 and n1!=n3 and n2!=n3):
                stra=row['codes'].split('&')
                for i in range(0,len(stra)):
                    if(stra[i]==n1 or stra[i]==n2 or stra[i]==n3):
                        nums=nums+1

            if(nums>=3):
                conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+rates+"*times where id="+row['id'])
            else:
                conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
         #前三组选，混合 inputok 168时时乐混合组选 298 3d
        elif(mid=="20" or mid=="58" or mid=="96" or mid=="134" or mid=="168" or mid=="298" or mid=="326"):
            zt=2
            if((n1+n2+n3).find(row['codes'])==-1 and (n1+n3+n2).find(row['codes'])==-1 and (n2+n1+n3).find(row['codes'])==-1 and (n2+n3+n1).find(row['codes'])==-1 and (n3+n1+n2).find(row['codes'])==-1 and (n3+n2+n1).find(row['codes'])==-1):
                conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
            else:
                rates=Get_rate(mid).split("")
                #组三
                if(n1==n2 or n1==n3 or n2==n3):
                    conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+(rates[0]*modes)+"*times where id="+row['id'])
                else:
                    conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+(rates[1]*modes)+"*times where id="+row['id'])

        #前三组合值ok 169时时乐组合值 299 3d 327 p3
        elif(mid=="21" or mid=="59" or mid=="97" or mid=="135" or mid=="169" or mid=="299" or mid=="327"):
            zt=2
            cs=n1+n2+n3
            stra=row['codes'].split("&")
            for i in range(0,len(stra)):
                if(stra[i]==cs):
                    zt=1
                    break

            if(zt=="1"):
                rates=Get_rate(mid).split("")
                #组3
                if(n1==n2 or n1==n3 or n2==n3):
                    conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+(rates[0]*modes)+"*times where id="+row['id'])
                else:
                    conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+(rates[1]*modes)+"*times where id="+row['id'])

            else:
                conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
        #后三组三
        elif(mid=="22" or mid=="60" or mid=="98" or mid=="136"):
            nums=0
            if(n3==n4 or n3==n5 or n4==n5):
                stra=row['codes'].split('&')
                for i in range(0,len(stra)):
                    if(stra[i]==n3 or stra[i]==n4 or stra[i]==n5):
                        nums=nums+1
            if(nums>=2):
                conn.cursor.execute("update ssc_bills set zt="+signa+",prize=rates*times where id="+row['id'])
            else:
                conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
        #后三组6
        elif(mid=="23" or mid=="61" or mid=="99" or mid=="137"):
            nums=0
            #if(n3!=n4 and n3!=n5 and n4!=n5):
            stra=row['codes'].split('&')
            for i in range(0,len(stra)):
                if(stra[i]==n3 or stra[i]==n4 or stra[i]==n5):
                    nums=nums+1
            if(nums>=3):
                conn.cursor.execute("update ssc_bills set zt="+signa+",prize=rates*times where id="+row['id'])
            else:
                conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
        #后三组混合
        elif(mid=="24" or mid=="62" or mid=="100" or mid=="138"):
            zt=2
            if((n3+n4+n5).find(row['codes'])==-1 and (n3+n5+n4).find(row['codes'])==-1 and (n4+n3+n5).find(row['codes'])==-1 and (n4+n5+n3).find(row['codes'])==-1 and (n5+n3+n4).find(row['codes'])==-1 and (n1+n2+n3).find(row['codes'])==-1):
                conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
            else:
                rates=Get_rate(mid).split("")
                #组三
                if(n3==n4 or n3==n5 or n4==n5):
                    conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+(rates[0]*modes)+"*times where id="+row['id'])
                else:
                    conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+(rates[1]*modes)+"*times where id="+row['id'])


        #后三组合值
        elif(mid=="25" or mid=="63" or mid=="101" or mid=="139"):
            zt=2
            cs=n3+n4+n5
            stra=row['codes'].split("&")
            for i in range(0,len(stra)):
                if(stra[i]==cs):
                    zt=1
                    break
            if(zt=="1"):
                rates=Get_rate(mid).split("")
                #组3
                if(n3==n4 or n3==n5 or n4==n5):
                    conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+(rates[0]*modes)+"*times where id="+row['id'])
                else:
                    conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+(rates[1]*modes)+"*times where id="+row['id'])

        #一码不定位ok
        elif(mid=="26" or mid=="64" or mid=="102" or mid=="140"):
            nums=0
            stra=row['codes'].split("&")
            for i in range(0,len(stra)):
                if(stra[i]==n3 or stra[i]==n4 or stra[i]==n5):
                    nums=nums+1

            if(nums>=1):
                conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+"rates*times*nums"+" where id="+row['id'])
            else:
                conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
        #二码不定位ok
        elif(mid=="27" or mid=="65" or mid=="103" or mid=="141"):
            nums=0
            stra=row['codes'].split("&")
            for i in range(0,len(stra)):
                if(stra[i]==n3 or stra[i]==n4 or stra[i]==n5):
                    nums=nums+1

            if(nums==2):
                conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+"rates*times*nums"+" where id="+row['id'])
            elif(nums==3):
                conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+"rates*times*3"+" where id="+row['id'])
            else:
                conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])

        #前二直选 172时时乐前2直 302 3d 330p3
        elif(mid=="28" or mid=="66" or mid=="104" or mid=="142" or mid=="172" or mid=="302" or mid=="330"):
            #单式
            if(row['type']=="input"):
                cs=n1+n2
                #pos= strpos(row['codes'],cs)
                if(cs.find(row['codes'])==-1):
                    conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
                else:
                    conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+"rates*times"+" where id="+row['id'])
            #复式
            elif(row['type']=="digital"):
                stra=row['codes'].split('&')
                nums=0
                for i in range(0,len(stra)):
                    strb=stra[i].split('&')
                    for ii in range(0,len(strb)):
                        if(strb[ii]==na[i]):
                            nums=nums+1

                if(nums==2):
                    conn.cursor.execute("update ssc_bills set zt="+signa+",prize="+"rates*times"+" where id="+row['id'])
                else:
                    conn.cursor.execute("update ssc_bills set zt="+signb+",prize=0 where id="+row['id'])
                
        if(sign==1):
            sqls="update ssc_bills set kjcode="+"'"+kjcode+"'"+" where id ="+row['id']
            rss=conn.cursor.execute(sqls)
            
            sqls="select * from ssc_bills where id ="+row['id']
            rss=conn.cursor.execute(sqls)
            rows = conn.cursor.fetchone(rss)
            if(rows['zt']==1):
                sqla = "select * from ssc_record order by id desc limit 1"
                rsa = conn.cursor.execute(sqla)
                rowa = conn.cursor.fetchall(rsa)
                #dan1 = sprintf("%07s",(base_convert(rowa['id']+1,10,36)).upper())
                dan1=base_convert(rowa['id']+1,10,36).upper()
                lmoney = Get_mmoney(rows['uid'])+rows['prize']
                #sqla="insert into ssc_record set lotteryid="+rows['lotteryid']+",lottery="+rows['lottery']+", dan="+dan1+", dan1="+rows['dan']+", dan2="+rows['dan1']+", uid="+rows['uid']+", username="+rows['username']+", issue="+rows['issue']+", types='12', mid="+rows['mid']+", mode="+rows['mode']+", smoney="+rows['prize']+",leftmoney="+lmoney+", cont="+rows['cont']+", regtop="+rows['regtop']+', regup='".rows['regup']."', regfrom='".rows['regfrom']."', adddate='".date("Y-m-d H:i:s")."'"
                sqla="insert into ssc_record set lotteryid="+rows['lotteryid']+",lottery="+rows['lottery']+", dan="+dan1+", dan1="+rows['dan']+", dan2="+rows['dan1']+", uid="+rows['uid']+", username="+rows['username']+", issue="+rows['issue']+", types='12', mid="+rows['mid']+", mode="+rows['mode']+", smoney="+rows['prize']+",leftmoney="+lmoney+", cont="+rows['cont']+", regtop="+rows['regtop']+", regup="+rows['regup']+", regfrom="+rows['regfrom']+", adddate="+str(datetime())
                exe=conn.cursor.execute(sqla)

                sqla="update ssc_member set leftmoney="+lmoney+" where id="+rows['uid']
                exe=conn.cursor.execute(sqla)

                if(rows['dan1']!=""):
                    sqla = "update ssc_zbills set prize=prize+"+str(rows['prize'])+", zjnums=zjnums+1 where dan="+rows['dan1']
                    rsa = conn.cursor.execute(sqla)
                    
                #多余转结
                if(rows['autostop']=="yes"):
                    sqla="select sum(money) as tmoney,count(*) as cnums from ssc_zdetail where zt=0 and dan="+rows['dan1']
                    rsa = conn.cursor.execute(sqla)
                    rowa = conn.cursor.execute(rsa)
                    ttm=rowa['tmoney']
                    if(ttm>0):
                        sqla = "update ssc_zbills set cnums=cnums+"+str(rowa['cnums'])+", cmoney=cmoney+"+str(ttm)+" where dan="+str(rows['dan1'])
                        rsa = conn.cursor.execute(sqla)
                        sqla = "select * from ssc_record order by id desc limit 1"
                        rsa = conn.cursor.execute(sqla)
                        rowa = conn.cursor.execute(rsa)
                        #追号返款
                        #dan1 = sprintf("%07s",(base_convert(rowa['id']+1,10,36)).upper())
                        dan1=base_convert(rowa['id']+1,10,36).upper()
                        #sqla="insert into ssc_record set lotteryid='".rows['lotteryid']."', lottery='".rows['lottery']."', dan='".dan1."', dan2='".rows['dan']."', uid='".rows['uid']."', username='".rows['username']."', issue='".rows['issue']."', types='10', mid='".rows['mid']."', mode='".rows['mode']."', smoney=".ttm.",leftmoney=".(lmoney+ttm).", cont='".rows['cont']."', regtop='".rows['regtop']."', regup='".rows['regup']."', regfrom='".rows['regfrom']."', adddate='".date("Y-m-d H:i:s")."'"
                        sqla="insert into ssc_record set lotteryid="+rows['lotteryid']+", lottery="+str(rows['lottery'])+", dan="+str(dan1)+", dan2="+str(rows['dan'])+", uid="+str(row['uid'])+", username="+str(rows['username'])+", issue="+str(rows['issue'])+", types=10, mid="+str(rows['mid'])+", mode="+str(rows['mode'])+", smoney=ttm, leftmoney=lmoney+ttm, cont="+str(rows['cont'])+", regtop="+rows['regtop']+", regup="+rows['regup']+", regfrom="+rows['regfrom']+", adddate="+str(datetime)
                        exe=conn.cursor.execute(sqla)
                        sqla="update ssc_member set leftmoney="+str(lmoney+ttm)+" where id="+rows['uid']
                        exe=conn.cursor.execute(sqla)
                    
                    sqla="update ssc_zdetail set zt=2 where dan="+str(rows['dan1'])+" and zt=0"
                    exe=conn.cursor.execute(sqla)

    if(sign==0):
        sqlb="select SUM(IF(types = 1, smoney, 0)) as t1,SUM(IF(types = 2, zmoney, 0)) as t2,SUM(IF(types = 3, smoney, 0)) as t3,SUM(IF(types = 7, zmoney, 0)) as t7,SUM(IF(types = 11, smoney, 0)) as t11,SUM(IF(types = 12, smoney, 0)) as t12,SUM(IF(types = 13, smoney, 0)) as t13,SUM(IF(types = 15, zmoney, 0)) as t15,SUM(IF(types = 16, zmoney, 0)) as t16,SUM(IF(types = 32, smoney, 0)) as t32,SUM(IF(types = 40, smoney, 0)) as t40 from ssc_record where lotteryid="+str(lid)+" and issue="+str(issue)
        rsb = conn.cursor.execute(sqlb)
        rowb = conn.cursor.fetchall(rsb)
        sqlc="select SUM(prize) as zj from ssc_bills where lotteryid="+str(lid)+" and issue="+str(issue)
        rsc = conn.cursor.execute(sqlc)
        rowc = conn.cursor.fetchall(rsc)
        sqld="insert into ssc_info set lotteryid="+str(lid)+", lottery="+Get_lottery(lid)+", issue="+str(issue)+", tz="+str(rowb['t7']-rowb['t13'])+", fd="+str((rowb['t11']-rowb['t15']))+", zj="+rowc['zj']+", adddate="+str(datetime.now())
        exe=conn.cursor.execute(sqld)
    #计分红 zh
    elif(sign==1):
        issueb=int(issue)+1
        sqlb="select * from ssc_zdetail where lotteryid="+str(lid)+" and issue="+str(issueb)+" and zt=0"
        rsb = conn.cursor.execute(sqlb)
        rowb = conn.cursor.fetchall(rsb)
        while (rowb):
            sqla = "update ssc_zbills set fnums=fnums+1, fmoney=fmoney+"+str(rowb['money'])+" where dan="+rowb['dan']
            rsa = conn.cursor.execute(sqla)
        
            sql = "select * from ssc_member where username="+rowb['username']
            rs = conn.cursor.execute(sql)
            row =conn.cursor.fetchall(rs)
            lmoney=row['leftmoney']
            # point处理
            if(rowb['mid']=="20" or rowb['mid']=="21" or rowb['mid']=="24" or rowb['mid']=="25" or rowb['mid']=="58" or rowb['mid']=="59" or rowb['mid']=="62" or rowb['mid']=="63" or rowb['mid']=="96" or rowb['mid']=="97" or rowb['mid']=="100" or rowb['mid']=="101" or rowb['mid']=="134" or rowb['mid']=="135" or rowb['mid']=="138" or rowb['mid']=="139" or rowb['mid']=="168" or rowb['mid']=="169" or rowb['mid']=="205" or rowb['mid']=="206" or rowb['mid']=="239" or rowb['mid']=="240" or rowb['mid']=="273" or rowb['mid']=="274" or rowb['mid']=="298" or rowb['mid']=="299" or rowb['mid']=="326" or rowb['mid']=="327" or rowb['mid']=="366" or rowb['mid']=="367"):
                sstra=row['rebate'].split("")
                sstrb=sstra[sstri-1].split(",")
                spoint=sstrb[1]/100
            else:
                spoint=rowb['point']

            sqla = "select * from ssc_record order by id desc limit 1"
            rsa = conn.cursor.execute(sqla)
            rowa =conn.cursor.fetchall(rsa)
            #追号返款
            #dan1 = sprintf("%07s",(base_convert(rowa['id']+1,10,36).upper()))
            dan1 = base_convert(rowa['id']+1,10,36).upper()
            sqla="insert into ssc_record set lotteryid="+rowb['lotteryid']+", lottery="+str(rowb['lottery'])+", dan="+str(dan1)+", dan2="+str(rowb['dan'])+"', uid="+rowb['uid']+", username="+str(rowb['username'])+", issue="+rowb['issue']+", types='10', mid="+str(rowb['mid'])+", mode="+str(rowb['mode'])+", smoney="+str(rowb['money'])+", leftmoney="+str(lmoney+rowb['money'])+", cont="+str(rowb['cont'])+", regtop="+str(rowb['regtop'])+"', regup="+str(rowb['regup'])+"', regfrom="+str(rowb['regfrom'])+", adddate='"+datetime.now()
            exe=conn.cursor.execute(sqla)

            sqla = "select * from ssc_bills order by id desc limit 1"
            rsa = conn.cursor.execute(sqla)
            rowa =conn.cursor.fetchone(rsa)
            #转注单
            #dan2 = sprintf("%06s",(base_convert(rowa['id']+1,10,36)).upper())
            dan2=base_convert(rowa['id']+1,10,36).upper()
            sqla="INSERT INTO ssc_bills set lotteryid="+str(rowb['lotteryid'])+", lottery="+str(rowb['lottery'])+", dan="+str(dan2)+", dan1="+str(rowb['dan'])+", uid="+rowb['uid']+", username="+rowb['username']+", issue="+rowb['issue']+", type="+rowb['type']+", mid="+rowb['mid']+", codes="+str(rowb['codes'])+", nums="+str(rowb['nums'])+", times="+str(rowb['times'])+", money="+str(rowb['money'])+"' mode="+str(rowb['mode'])+", rates="+str(rowb['rates'])+", point="+str(rowb['point'])+", cont="+str(rowb['cont'])+", regtop="+str(rowb['regtop'])+", regup="+rowb['regup']+", regfrom="+str(rowb['regfrom'])+", userip="+str(rowb['userip'])+", adddate="+datetime("Y-m-d H:i:s")+", canceldead="+str(rowb['canceldead'])+", autostop="+str(rowb['autostop'])
            exe=conn.cursor.execute(sqla)
            
            sqla = "update ssc_zdetail set danb="+str(dan2)+", zt=1 where id="+str(rowb['id'])
            rsa = conn.cursor.execute(sqla)
                        
            sqla = "select * from ssc_record order by id desc limit 1"
            rsa = conn.cursor.execute(sqla)
            rowa =conn.cursor.fetchall(rsa)
            #投注扣款
            #dan1 = sprintf("%07s",(base_convert(rowa['id']+1,10,36)).upper())
            dan1=base_convert(rowa['id']+1,10,36).upper()
            sqla="insert into ssc_record set lotteryid="+str(rowb['lotteryid'])+", lottery="+str(rowb['lottery'])+", dan="+str(dan1)+", dan1="+str(dan2)+", dan2="+str(rowb['dan'])+", uid="+rowb['uid']+", username="+str(rowb['username'])+", issue="+str(rowb['issue'])+"', types='7', mid="+str(rowb['mid'])+"', mode="+str(rowb['mode'])+", zmoney="+str(rowb['money'])+",leftmoney="+str(lmoney)+", cont="+str(rowb['cont'])+", regtop="+str(rowb['regtop'])+", regup="+str(rowb['regup'])+", regfrom="+str(rowb['regfrom'])+", adddate='"+datetime.now("Y-m-d H:i:s")
            exe=conn.cursor.execute(sqla)
            if(spoint!="0"):
                sstrp=spoint*100
                sqla = "select * from ssc_record order by id desc limit 1"
                rsa = conn.cursor.execute(sqla)
                rowa =conn.cursor.fetchall(rsa)
                #dan1 = sprintf("%07s",(base_convert(rowa['id']+1,10,36)).upper())
                dan1=base_convert(rowa['id']+1,10,36).upper()
                sqla="insert into ssc_record set lotteryid="+str(rowb['lotteryid'])+", lottery="+str(rowb['lottery'])+", dan="+str(dan1)+", dan1="+str(dan2)+", dan2="+str(rowb['dan'])+", uid="+rowb['uid']+", username="+rowb['username']+", issue="+str(rowb['issue'])+", types='11', mid="+str(rowb['mid'])+", mode="+str(rowb['mode'])+", smoney="+str(rowb['money']*spoint)+",leftmoney="+str(lmoney+rowb['money']*spoint)+", cont="+str(rowb['cont'])+", regtop="+str(rowb['regtop'])+", regup="+str(rowb['regup'])+", regfrom="+str(rowb['regfrom'])+", adddate="+datetime.now("Y-m-d H:i:s")
                exe=conn.cursor.execute(sqla)

                sqla="update ssc_member set leftmoney="+str((lmoney+rowb['money']*spoint))+" where username='"+str(rowb['username'])
                exe=conn.cursor.execute(sqla)

                #上级返点
                if(rowb['regfrom']!=""):
                    regfrom=rowb['regfrom'].split('&&')
                    for ia in range(0,regfrom):
                        susername=regfrom[ia].replace("&","")
                        sqla = "select * from ssc_member where username="+str(susername)
                        rsa = conn.cursor.execute(sqla)
                        rowa =conn.cursor.fetchall(rsa)
                        sstra=rowa['rebate'].split('')
                                    
                        sstrb=sstra[sstri-1].split('')
                        sstrc=rstrb[0].split('_')
                        if((sstrb[1]-sstrp)>0):
                            sstrp=sstrb[1]

                            sqla = "select * from ssc_record order by id desc limit 1"
                            rsa = conn.cursor.execute(sqla)
                            rowa =conn.cursor.fetchall(rsa)
                            #dan1 = sprintf("%07s",(base_convert(rowa['id']+1,10,36)).upper())
                            dan1=base_convert(rowa['id']+1,10,36).upper()
                            sqla="insert into ssc_record set lotteryid='"+rowb['lotteryid']+"', lottery='".rowb['lottery']+"', dan='"+str(dan1)+"', dan1='"+str(dan2)+"', dan2='"+str(rowb['dan'])+"', uid="+str(Get_memid(susername))+", username="+str(susername)+", issue="+str(rowb['issue'])+", types='11', mid="+str(rowb['mid'])+", mode="+str(rowb['mode'])+", smoney="+str((rowb['money']*(sstrb[1]-sstrp)/100))+",leftmoney="+str((Get_mmoney(susername)+rowb['money']*(sstrb[1]-sstrp)/100))+", cont="+str(rowb['cont'])+", regtop="+str(rowb['regtop'])+", regup="+str(rowb['regup'])+", regfrom="+str(rowb['regfrom'])+", adddate="+datetime.now("Y-m-d H:i:s")
                            exe=conn.cursor.execute(sqla)
            
                            sqla="update ssc_member set leftmoney=leftmoney"+str((rowb['money']*(sstrb[1]-sstrp)/100))+" where username="+str(susername)
                            exe=conn.cursor.execute(sqla)
        
        sqla="select * from ssc_zbills where lotteryid="+str(lid)+" and zt='0'"
        rsa = conn.cursor.execute(sqla)
        rowa =conn.cursor.fettchall(rsa)
        while (rowa):
            sqlb="select * from ssc_zdetail where dan="+str(rowa['dan'])+" and zt='0'"
            rsb = conn.cursor.execute(sqlb)
            total = conn.cursor.rowcount(rsb)
            if(total==0):
                sqlb="update ssc_zbills set zt='1' where dan="+str(rowa['dan'])
                exe=conn.cursor.execute(sqlb)
        
# #投注佣金返利开始
# sql_jc = "select * from ssc_huodong where id=1"
# rs_jc = conn.cursor.execute(sql_jc)
# row_jc =conn.cursor.execute(rs_jc)
# #每日领取一次
# if(row_jc['kg']==1):
#     sql_jc1 = "select * from ssc_record where uid_xj='uid_fx' and types='70' and  adddate like '%"+datetime.now("Y-m-d")+"%'"
#     rs_jc1 = conn.cursor.execute(sql_jc1)
#     row_jc1 =conn.cursor.execute(rs_jc1)
#
# sql_jc2 = "select sum(zmoney) sum_tj from ssc_record where uid='uid_fx' and types='7' and  adddate like '%"+datetime.now("Y-m-d H:i:s")+"%'"
# rs_jc2 = conn.cursor.execute(sql_jc2)
# row_jc2 =conn.cursor.fetchall(rs_jc2)

# if ((not is_set(row_jc1['id'])) and row_jc2['sum_tj']>=500):
#     sqla = "select * from ssc_member WHERE username="+str(regup_fx)
#     rsa = conn.cursor.execute(sqla)
#     rowa =conn.cursor.execute(rsa)
#     leftmoney=rowa['leftmoney']
#     #帐变
#     sqlc = "select * from ssc_record order by id desc limit 1"
#     rsc = conn.cursor.execute(sqlc)
#     rowc =conn.cursor.execute(rsc)
#     #dan1 = sprintf("%07s",base_convert(rowc['id']+1,10,36).upper())
#     dan1=base_convert(rowc['id']+1,10,36).upper()
#     lmoney=row_jc['jieguo']
#     leftmoney=rowa['leftmoney']+lmoney
#     sqla="insert into ssc_record set dan="+str(dan1)+", uid="+str(rowa['id'])+", username="+rowa['username']+", types='70', smoney="+lmoney+", leftmoney="+leftmoney+", regtop="+str(rowa['regtop']+", regup="+str(rowa['regup'])+", regfrom="+str(rowa['regfrom'])+", adddate="+str(datetime.now("Y-m-d H:i:s"))+", uid_xj=uid_fx'"
#     exe=conn.cursor.execute(sqla)
#     sqlb="insert into ssc_savelist set uid='".rowa['id']."', username='".rowa['username']."', bank='投注佣金返利', bankid='0', cardno='', money=".lmoney.", sxmoney='0', rmoney=".lmoney.", adddate='".date("Y-m-d H:i:s")."',zt='1',types='70'"
#     exe=conn.cursor.execute(sqlb)
#     sql="update ssc_member set leftmoney =(leftmoney+".lmoney."),totalmoney=(totalmoney+".lmoney.") where id ='".rowa['id']."'"
#     exe=conn.cursor.execute(sql)

'''
##投注佣金返利结束

# //分红
# //sqlb="select regtop, SUM(IF(types = 1, smoney, 0)) as t1,SUM(IF(types = 2, zmoney, 0)) as t2,SUM(IF(types = 3, smoney, 0)) as t3,SUM(IF(types = 7, zmoney, 0)) as t7,SUM(IF(types = 11, smoney, 0)) as t11,SUM(IF(types = 12, smoney, 0)) as t12,SUM(IF(types = 13, smoney, 0)) as t13,SUM(IF(types = 15, zmoney, 0)) as t15,SUM(IF(types = 16, zmoney, 0)) as t16,SUM(IF(types = 32, smoney, 0)) as t32,SUM(IF(types = 40, smoney, 0)) as t40 from ssc_record where lotteryid='".lid."' and issue='".issue."' group by regtop"
# //rsb = conn.cursor.execute(sqlb)
# //        while (rowb =conn.cursor.execute(rsb)):
# //            if(rowb['regtop']!=""):
# //                sqls="select * from ssc_member where username ='".rowb['regtop']."'"
# //                rss=conn.cursor.execute(sqls) or  die("数据库修改出错1".mysql_error())
# //                rows =conn.cursor.execute(rss)
# //                zmoney = rows['zc']*(row['t7']-row['t11']-row['t12']-row['t13']+row['t15']+row['t16'])/100
# //                lmoney = rows['leftmoney']+zmoney
# //
# //                sqla = "select * from ssc_record order by id desc limit 1"
# //                rsa = conn.cursor.execute(sqla)
# //                rowa =conn.cursor.execute(rsa)
# //                dan1 = sprintf("%07s",strtoupper(base_convert(rowa['id']+1,10,36)))
# //
# //                sqla="insert into ssc_record set lotteryid='".lid."', lottery='".Get_lottery(lid)."', dan='".dan1."', uid='".rows['uid']."', username='".rowb['regtop']."', issue='".issue."', types='40', smoney=".zmoney.",leftmoney=".lmoney.", adddate='".date("Y-m-d H:i:s")."'"
# //                exe=conn.cursor.execute(sqla) or  die("数据库修改出错!!!".mysql_error())
# //
# //                sqla="update ssc_member set leftmoney=".lmoney." where username='".rowb['regtop']."'"
# //                exe=conn.cursor.execute(sqla) or  die("数据库修改出错!!!".mysql_error())
# //
# //
'''

def Get_rate(rrr):
    result=conn.cursor.execute('Select * from ssc_class where mid='+rrr)
    raa=conn.cursor.fetchall(result)
    return raa['rates']

def Get_mmoney(rrr):
    result=conn.cursor.execute("Select * from ssc_member where id="+rrr)
    raa=conn.cursor.fetchall(result)
    return raa['leftmoney']

def Get_lottery(rrr):
    result=conn.cursor.execute("Select * from ssc_set where id="+rrr)
    raa=conn.cursor.fetchall(result)
    return raa['name']

def base_convert(number, fromBase, toBase):
    try:
        # Convert number to base 10
        base10 = int(number, fromBase)
    except ValueError:
        raise

    if toBase < 2 or toBase > 36:
        raise NotImplementedError

    output_value = ''
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    sign = ''

    if base10 == 0:
        return '0'
    elif base10 < 0:
        sign = '-'
        base10 = -base10

    # Convert to base toBase
    s = ''
    while base10 != 0:
        r = base10 % toBase
        r = int(r)
        s = digits[r] + s
        base10 //= toBase

    output_value = sign + s
    return output_value

def is_set(variable):
    """
    判读变量是否定义
    :param variable:
    :return: bool
    """
    return variable in locals() or variable in globals()

if __name__ == "__main__":
    autokj('4','7','7','5','8','1','20150410053',0)