# coding=utf-8
__author__ = 'Feely'

import time
import multiprocessing
import sys

import DrawNO
import db
import log

import datetime
import random

# #import GDSFC


reload(sys)
sys.setdefaultencoding('utf-8')
sys.excepthook = lambda *args: None
STDERR = sys.stderr

#全局期号
CQreturndate = ''  #重庆全局期号
JXreturndate = ''  #江西全局期号
gd11_returndate = ''  #11选5全局期号
YUNreturndate = ''  #11运夺金全局期号
PLSreturnDate = ''  #排列三全局期号
fc3dreturndate = ''  #福彩3d
SC1FCreturndate = ''  #尚彩1FC
SC5FCreturndate = ''  #尚彩5FC

#360重庆时时彩
def ssc360_drawnumber(ssc360_type, db_ssc_type):
    mysql_cqssc= db.MYSQL()
    global CQreturndate
    while True:
        try:
            #调用爬虫，获取开奖信息
            assert isinstance(ssc360_type, str)
            draw_date, draw_code_tmp, draw_time_str = DrawNO.CQ360(ssc360_type)
            draw_code = draw_code_tmp.replace(",", "")
            if draw_code == '0' or draw_date <= CQreturndate:
                pass
            else:
                CQreturndate = mysql_cqssc.CallSP(kjCodes=draw_code, lottery_type=db_ssc_type, lottery_num=draw_date, kjtime=draw_time_str)
                time.sleep(180)
            time.sleep(30)
        except Exception as e:
            print e
            log.logging.error(e)
            time.sleep(5)
            continue

#360江西时时彩
def jxssc360_drawnumber(ssc360_type, db_ssc_type):
    mysql_jxssc= db.MYSQL()
    global JXreturndate
    while True:
        try:
            #调用爬虫，获取开奖信息
            assert isinstance(ssc360_type, str)
            draw_date, draw_code_tmp, draw_time_str = DrawNO.CQ360(ssc360_type)
            draw_code = draw_code_tmp.replace(",", "")
            if draw_code == '0' or draw_date <= JXreturndate:
                pass
            else:
                JXreturndate = mysql_jxssc.CallSP(kjCodes=draw_code, lottery_type=db_ssc_type, lottery_num=draw_date, kjtime=draw_time_str)
                time.sleep(180)
            time.sleep(30)
        except Exception as e:
            print e
            log.logging.error(e)
            time.sleep(5)

#360 广东11选5
def gd11_360_drawnumber(ssc360_type, db_ssc_type):
    mysql_gd11x5ssc= db.MYSQL()
    global gd11_returndate
    while True:
        try:
            #调用爬虫，获取开奖信息
            assert isinstance(ssc360_type, str)
            draw_date, draw_code_tmp, draw_time_str = DrawNO.CQ360(ssc360_type)
            draw_code = draw_code_tmp.replace(",", "")
            if draw_code == '0' or draw_date <= CQreturndate:
                pass
            else:
                gd11_returndate = mysql_gd11x5ssc.CallSP(kjCodes=draw_code, lottery_type=db_ssc_type, lottery_num=draw_date, kjtime=draw_time_str)
                time.sleep(180)
            # draw_time = datetime.strptime(draw_time_str, "%Y-%m-%d %H:%M")
            # ms.IsInfoExists(SPname='ibc.dbo.IsInfoExists',lottery_type=db_ssc_type,lottery_num=draw_date,kjCodes=draw_code,kjtime=draw_time,addtime=datetime.now())
            # time.sleep(1)
            # ms.SYSPaiJiang(SPname='ibc.dbo.SYSPaiJiang',kjExpect=draw_date,kjTime=draw_time_str,kjCode=draw_code,ltType=db_ssc_type)
            time.sleep(30)
        except Exception as e:
            print e
            log.logging.error(e)
            time.sleep(5)
            continue

#360 11运夺金（山东11选5）
def yun360_drawnumber(ssc360_type, db_ssc_type):
    mysql_sd11x5ssc= db.MYSQL()
    global YUNreturndate
    while True:
        try:
            #调用爬虫，获取开奖信息
            assert isinstance(ssc360_type, str)
            draw_date, draw_code_tmp, draw_time_str = DrawNO.CQ360(ssc360_type)
            draw_code = draw_code_tmp.replace(",", "")
            print draw_code
            if draw_code == '0' or draw_date <= YUNreturndate:
                pass
            else:
                YUNreturndate = mysql_sd11x5ssc.CallSP(kjCodes=draw_code, lottery_type=db_ssc_type, lottery_num=draw_date, kjtime=draw_time_str)
                time.sleep(180)
            # draw_time = datetime.strptime(draw_time_str, "%Y-%m-%d %H:%M")
            # ms.IsInfoExists(SPname='ibc.dbo.IsInfoExists',lottery_type=db_ssc_type,lottery_num=draw_date,kjCodes=draw_code,kjtime=draw_time,addtime=datetime.now())
            # time.sleep(1)
            # ms.SYSPaiJiang(SPname='ibc.dbo.SYSPaiJiang',kjExpect=draw_date,kjTime=draw_time_str,kjCode=draw_code,ltType=db_ssc_type)
            time.sleep(30)
        except Exception as e:
            print e
            log.logging.error(e)
            time.sleep(5)
            continue

#重庆时时彩
def ssc_drawnumber(ssc_type, db_ssc_type):
    mysql_ssccq= db.MYSQL()
    global CQreturndate
    while True:
        try:
            #调用爬虫，获取开奖信息
            assert isinstance(ssc_type, str)
            draw_date, draw_code, draw_time_str = DrawNO.drawnumber(ssc_type)
            if draw_code == '0' or draw_date <= CQreturndate:
                pass
            else:
                CQreturndate = mysql_ssccq.CallSP(kjCodes=draw_code, lottery_type=db_ssc_type, lottery_num=draw_date, kjtime=draw_time_str)
                time.sleep(180)
            # draw_time = datetime.strptime(draw_time_str, "%Y-%m-%d %H:%M")
            # ms.IsInfoExists(SPname='ibc.dbo.IsInfoExists',lottery_type=db_ssc_type,lottery_num=draw_date,kjCodes=draw_code,kjtime=draw_time,addtime=datetime.now())
            # time.sleep(1)
            # ms.SYSPaiJiang(SPname='ibc.dbo.SYSPaiJiang',kjExpect=draw_date,kjTime=draw_time_str,kjCode=draw_code,ltType=db_ssc_type)
            time.sleep(30)
        except Exception as e:
            print e
            log.logging.error(e)
            time.sleep(5)
            continue

#3D
def fc3d_drawnumber(ssc_type, db_ssc_type):
    mysql_3dccq=db.MYSQL()
    global fc3dreturndate
    while True:
        try:
            #调用爬虫，获取开奖信息
            assert isinstance(ssc_type, str)
            draw_date, draw_code, draw_time_str = DrawNO.fc3d(ssc_type)
            draw_code = draw_code.replace(",", "")
            if draw_code == '0' or draw_date <= fc3dreturndate:
                pass
            else:
                fc3dreturndate = mysql_3dccq.CallSP(kjCodes=draw_code, lottery_type=db_ssc_type, lottery_num=draw_date, kjtime=draw_time_str)
                time.sleep(180)
            # draw_time = datetime.strptime(draw_time_str, "%Y-%m-%d %H:%M")
            # ms.IsInfoExists(SPname='ibc.dbo.IsInfoExists',lottery_type=db_ssc_type,lottery_num=draw_date,kjCodes=draw_code,kjtime=draw_time,addtime=datetime.now())
            # time.sleep(1)
            # ms.SYSPaiJiang(SPname='ibc.dbo.SYSPaiJiang',kjExpect=draw_date,kjTime=draw_time_str,kjCode=draw_code,ltType=db_ssc_type)
            time.sleep(30)
        except Exception as e:
            print e
            log.logging.error(e)
            time.sleep(5)
            continue

#排列三、五
def pl5_drawnumber(ssc_type, db_ssc_type):
    mysql_plsccq=db.MYSQL()
    global PLSreturnDate
    while True:
        try:
            #调用爬虫，获取开奖信息
            assert isinstance(db_ssc_type, str)
            draw_date, draw_code, draw_time_str = DrawNO.PL5(ssc_type)
            draw_code = draw_code.replace(",", "")
            #print draw_code,draw_date,draw_time_str
            if draw_code == '0' or draw_date <= PLSreturnDate:
                pass
            else:
                print draw_date
                PLSreturnDate = mysql_plsccq.CallSP(kjCodes=draw_code, lottery_type=db_ssc_type, lottery_num=draw_date, kjtime=draw_time_str)
                time.sleep(180)
            time.sleep(30)
        except Exception as e:
            print e
            log.logging.error(e)
            time.sleep(5)
            continue

def sc5fc_drawnumber(db_ssc_type):
    mysql_sc5fc= db.MYSQL()
    global SC5FCreturndate
    while True:
        try:
            #调用爬虫，获取开奖信息
            assert isinstance(db_ssc_type,str)
            zeroyear=datetime.datetime.today().year
            zeromonth=datetime.datetime.today().month
            zeroday=datetime.datetime.today().day
            zerotime = datetime.datetime(year=zeroyear, month=zeromonth, day=zeroday, hour=0, minute=0, second=0)
            zerotime1 = datetime.datetime.now()
            datetoday= time.strftime("%y%m%d")
            dateissue = str(int((zerotime1 - zerotime).seconds / 300)).zfill(3)
            draw_date=datetoday+dateissue
            draw_code = str(random.randint(100000,999999))[1:6]
            print draw_date,draw_code,time.strftime("%Y-%m-%d %H:%M:%S")
            if draw_code == '0' or draw_date <= SC5FCreturndate:
                pass
            else:
                print "exe",draw_date,SC5FCreturndate
                log.logging.info("五分彩:")
                log.logging.info('date:%s code:%s time:%s curtime:%s',draw_date,draw_code,datetime.datetime.now().time(),datetime.datetime.now().time())
                SC5FCreturndate = mysql_sc5fc.CallSP(kjCodes=draw_code, lottery_type=db_ssc_type, lottery_num=draw_date, kjtime=time.strftime("%Y-%m-%d %H:%M:%S"))
                print "SC5FCreturndate",SC5FCreturndate
                time.sleep(180)
            # draw_time = datetime.strptime(draw_time_str, "%Y-%m-%d %H:%M")
            # ms.IsInfoExists(SPname='ibc.dbo.IsInfoExists',lottery_type=db_ssc_type,lottery_num=draw_date,kjCodes=draw_code,kjtime=draw_time,addtime=datetime.now())
            # time.sleep(1)
            # ms.SYSPaiJiang(SPname='ibc.dbo.SYSPaiJiang',kjExpect=draw_date,kjTime=draw_time_str,kjCode=draw_code,ltType=db_ssc_type)
            time.sleep(10)
        except Exception as e:
            print e
            log.logging.error(e)
            time.sleep(5)
            continue

def sc1fc_drawnumber(db_ssc_type):
    mysql_sc1fc=db.MYSQL()
    global SC1FCreturndate
    while True:
        try:
            #调用爬虫，获取开奖信息
            assert isinstance(db_ssc_type,str)
            zeroyear=datetime.datetime.today().year
            zeromonth=datetime.datetime.today().month
            zeroday=datetime.datetime.today().day
            zerotime = datetime.datetime(year=zeroyear, month=zeromonth, day=zeroday, hour=0, minute=0, second=0)
            zerotime1 = datetime.datetime.now()
            datetoday= time.strftime("%y%m%d")
            dateissue = str(int((zerotime1 - zerotime).seconds / 60)).zfill(4)
            draw_date=datetoday+dateissue
            draw_code = str(random.randint(100000,999999))[1:6]
            print draw_code
            # draw_code=draw_code_tmp[0]+','+draw_code_tmp[1]+','+draw_code_tmp[2]+','+draw_code_tmp[3]+','+draw_code_tmp[4]
            print draw_date,draw_code,time.strftime("%Y-%m-%d %H:%M:%S")
            if draw_code == '0' or draw_date <= SC1FCreturndate:
                pass
            else:
                log.logging.info("一分彩:")
                log.logging.info('date:%s code:%s time:%s curtime:%s',draw_date,draw_code,datetime.datetime.now().time(),datetime.datetime.now().time())

                SC1FCreturndate = mysql_sc1fc.CallSP(kjCodes=draw_code, lottery_type=db_ssc_type, lottery_num=draw_date, kjtime=time.strftime("%Y-%m-%d %H:%M:%S"))
                time.sleep(50)
            # draw_time = datetime.strptime(draw_time_str, "%Y-%m-%d %H:%M")
            # ms.IsInfoExists(SPname='ibc.dbo.IsInfoExists',lottery_type=db_ssc_type,lottery_num=draw_date,kjCodes=draw_code,kjtime=draw_time,addtime=datetime.now())
            # time.sleep(1)
            # ms.SYSPaiJiang(SPname='ibc.dbo.SYSPaiJiang',kjExpect=draw_date,kjTime=draw_time_str,kjCode=draw_code,ltType=db_ssc_type)
            time.sleep(5)
        except Exception as e:
            print e
            log.logging.error(e)
            time.sleep(5)
            continue


def main():
    """
    :rtype : Null
    """

    #360重庆时时彩
    ssc360_type = 'ssccq'
    db_ssc_type = '1'
    jobs = []
    for i in range(1):
        p_360cq = multiprocessing.Process(name='360CQSSC', target=ssc360_drawnumber, args=(ssc360_type, db_ssc_type,))
        jobs.append(p_360cq)
        p_360cq.start()
        p_360cq.join(timeout=10)

    # #360江西时时彩
    # ssc360_type = 'sscjx'
    # db_ssc_type = '4'
    # jobs = []
    # for i in range(1):
    #     p_360jx = multiprocessing.Process(name='360JXSSC', target=ssc360_drawnumber, args=(ssc360_type, db_ssc_type,))
    #     jobs.append(p_360jx)
    #     p_360jx.start()
    #     p_360jx.join(timeout=10)

    # #360 十一选五时时彩
    # gd11_360_type = 'gd11'
    # db_ssc_type = '8'
    # jobs = []
    # for i in range(1):
    #     p_360gd11 = multiprocessing.Process(name='360SYXW', target=gd11_360_drawnumber,
    #                                         args=(gd11_360_type, db_ssc_type,))
    #     jobs.append(p_360gd11)
    #     p_360gd11.start()
    #     p_360gd11.join(timeout=10)

    # #360 十一运夺金（山东11选5）
    # yun11_360_type = 'yun11'
    # db_ssc_type = '6'
    # jobs = []
    # for i in range(1):
    #     p_360yun11 = multiprocessing.Process(name='360YUN11', target=yun360_drawnumber,
    #                                          args=(yun11_360_type, db_ssc_type,))
    #     jobs.append(p_360yun11)
    #     p_360yun11.start()
    #     p_360yun11.join(timeout=10)

    #重庆时时彩
    # ssc_type='cqssc'
    # db_ssc_type='1'
    # jobs=[]
    # for i in range(1):
    #     p_cq=multiprocessing.Process(name='CQSSC',target=ssc_drawnumber,args=(ssc_type,db_ssc_type,))
    #     jobs.append(p_cq)
    #     p_cq.start()
    #     p_cq.join(timeout=10)

    # #PLS
    # ssc_type = 'p5'
    # db_ssc_type = '10'
    # jobs = []
    # for i in range(1):
    #     p_cq = multiprocessing.Process(name='PLS', target=pl5_drawnumber, args=(ssc_type, db_ssc_type,))
    #     jobs.append(p_cq)
    #     p_cq.start()
    #     p_cq.join(timeout=10)
    #
    #3D
    # ssc_type = 'sd'
    # db_ssc_type = '9'
    # jobs = []
    # for i in range(1):
    #     p_3d = multiprocessing.Process(name='3d', target=fc3d_drawnumber, args=(ssc_type, db_ssc_type,))
    #     jobs.append(p_3d)
    #     p_3d.start()
    #     p_3d.join(timeout=10)

    # #SC5FC
    # db_ssc_type = '2'
    # jobs = []
    # for i in range(1):
    #     p_sc5fc = multiprocessing.Process(name='SC5FC', target=sc5fc_drawnumber, args=(db_ssc_type,))
    #     jobs.append(p_sc5fc)
    #     p_sc5fc.start()
    #     p_sc5fc.join(timeout=10)
    #
    # #SC1FC
    # db_ssc_type = '12'
    # jobs = []
    # for i in range(1):
    #     p_sc1fc = multiprocessing.Process(name='SC1FC', target=sc1fc_drawnumber, args=(db_ssc_type,))
    #     jobs.append(p_sc1fc)
    #     p_sc1fc.start()
    #     p_sc1fc.join(timeout=10)

if __name__ == "__main__":
    main()