# coding=utf-8

import socket
from lxml import etree
from datetime import datetime
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
STDERR = sys.stderr
import mechanize
import cookielib
import log
import time

socket.setdefaulttimeout(300)

#Browser

class NoHistory(object):
  def add(self, *a, **k): pass
  def clear(self): pass

br = mechanize.Browser(history=NoHistory())
cj = cookielib.CookieJar()
br.set_cookiejar(cj)
#Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

#Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize.HTTPRefreshProcessor(),max_time=3)
#User-Agent
br.addheaders = [("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:29.0) Gecko/20100101 Firefox/29.0")]


def drawnumber(ssc_type):
    #Open website
    """
    :param self:
    :param ssc_type:
    :rtype : str,datetime,datetime
    """
    try:
        r = br.open('http://data.shishicai.cn/'+ssc_type+'/haoma/')
    except Exception,err:
        error1= str(err)
        print ssc_type,error1
        log.logging.error(br.title())
        log.logging.exception(error1)
        return '0','0','0'
    else:
        ssc_html = r.read().decode('utf-8')
        #show the html title
        print br.title()
        ## xpath analyze
        d = etree.HTML(ssc_html)
        result = d.xpath(u'//meta[2]/@content')[0].encode("utf-8")
        draw_date = result[18:26]+result[27:30]
        draw_code = result[46:51]
        draw_code1=draw_code[0]+','+draw_code[1]+','+draw_code[2]+','+draw_code[3]+','+draw_code[4]
        draw_time=result[65:81].strip()
        print draw_date, draw_code, draw_time,datetime.now()
        log.logging.info(br.title())
        log.logging.info('date:%s code:%s time:%s curtime:%s',draw_date,draw_code,draw_time,datetime.now().time())
        #print result
        return draw_date,draw_code,draw_time

def CQ360(ssc360_type):
    #Open website
    """
    :param self:
    :param ssc_type:
    :rtype : str,datetime,datetime
    """
    url='http://cp.360.cn/'+ssc360_type+'/'
    now_time=time.localtime()
    number = ''
    r = br.open(url,timeout=300)
    ssc_html = r.read().decode('gb2312')
    #ssc_html = r.read()
    #show the html title
    print '360时时彩',url
    #print br.title()
    ## xpath analyze
    d = etree.HTML(ssc_html)
    #Draw DateNO
    draw_date_tmp = ''.join(d.xpath(u'/html/body/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]/div[1]/h3/em/text()'))
    draw_date=str(now_time.tm_year)+draw_date_tmp
    #drow Number
    number=number+''.join(d.xpath(u'/html/body/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]/div[1]/div/ul/li[1]/text()'))+','
    number=number+''.join(d.xpath(u'/html/body/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]/div[1]/div/ul/li[2]/text()'))+','
    number=number+''.join(d.xpath(u'/html/body/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]/div[1]/div/ul/li[3]/text()'))+','
    number=number+''.join(d.xpath(u'/html/body/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]/div[1]/div/ul/li[4]/text()'))+','
    number=number+''.join(d.xpath(u'/html/body/div[1]/div[3]/div[3]/div[2]/div[2]/div[1]/div[1]/div/ul/li[5]/text()'))
    draw_code=number
    #Draw Time
    draw_time=datetime.now().strftime("%Y-%m-%d %H:%M")
    print draw_date,draw_code,datetime.now()
    if (number=='?,?,?,?,?'):
        number='0'
    log.logging.info('360时时彩'+'   '+url)
    log.logging.info('date:%s code:%s curtime:%s',draw_date,draw_code,datetime.now())
    return draw_date,number,draw_time

def tjssc():
    try:
        r = br.open("http://kaijiang.cjcp.com.cn/tjssc")
        html = r.read()
        soup = BeautifulSoup(html)
        table_hot = soup.find('td',attrs={"class":"qihao"})
        time_hot = soup.find ('td',attrs={"class":"time"})
        draw_time=time_hot.get_text()
        date_tmp=table_hot.get_text()
        draw_date=date_tmp[0:8]+'-0'+date_tmp[9:11]
        number1 = {}
        codes=''
        t1=0
        # print soup.find('td', text=table_hot.get_text()).parent.find_all('input')['value']
        while t1<5:
            number1[t1]=soup.find("td", text=table_hot.get_text()).parent.find_all('input')[t1]['value']
            codes=codes+number1[t1].strip()+','
            t1+=1
        draw_code=codes[:-1]
        print "tjssc number:"
        print draw_code,draw_date,draw_time
        return draw_code,draw_date,draw_time[:-3]
    except AttributeError as err:
        error=str(err)
        print error
        log.logging.error(br.title())
        log.logging.error(error)
        return '0','0','0'

def gd11x5(ssc_type):
    try:
        r = br.open('http://data.shishicai.cn/'+ssc_type+'/haoma/')
    except Exception,err:
        error=str(err)
        print error
        log.logging.error(br.title())
        log.logging.error(error)
        return '0','0','0'
    else:
        ssc_html = r.read().decode('utf-8')
        #show the html title
        print br.title()
        #Show the response headers
        #print r.info()
        ## xpath analyze
        d = etree.HTML(ssc_html)
        result = d.xpath(u'//meta[2]/@content')[0].encode("utf-8")
        draw_date = result[15:27]
        draw_code = result[43:57]
        #draw_code1=draw_code[0]+','+draw_code[1]+','+draw_code[2]+','+draw_code[3]+','+draw_code[4]
        draw_time=result[71:87].strip()
        print draw_date, draw_code, draw_time,datetime.now()
        log.logging.info(br.title())
        log.logging.info('date:%s code:%s time:%s',draw_date,draw_code,draw_time)
        #print result
        return draw_date,draw_code,draw_time

def PL5(ssc360_type):
    #Open website
    """
    :param self:
    :param ssc_type:
    :rtype : str,datetime,datetime
    """
    url='http://cp.360.cn/'+ssc360_type+'/'
    now_time=time.localtime()
    number = ''
    r = br.open(url,timeout=300)
    ssc_html = r.read().decode('gb2312')
    #ssc_html = r.read()
    #show the html title
    print '360时时彩',url
    #print br.title()
    ## xpath analyze
    d = etree.HTML(ssc_html)
    #Draw DateNO
    draw_date_tmp = ''.join(d.xpath(u'/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/h3/span/b/text()'))
    draw_date=draw_date_tmp[2:]
    #drow Number
    number=number+''.join(d.xpath(u'/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div/ul/li[1]/text()'))+','
    number=number+''.join(d.xpath(u'/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div/ul/li[2]/text()'))+','
    number=number+''.join(d.xpath(u'/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div/ul/li[3]/text()'))+','
    number=number+''.join(d.xpath(u'/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div/ul/li[4]/text()'))+','
    number=number+''.join(d.xpath(u'/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div/ul/li[5]/text()'))
    draw_code=number
    #Draw Time
    draw_time=datetime.now().strftime("%Y-%m-%d %H:%M")
    print draw_date,draw_code,datetime.now()
    if (number=='?,?,?,?,?'):
        number='0'
    log.logging.info('360时时彩'+'   '+url)
    log.logging.info('date:%s code:%s curtime:%s',draw_date,draw_code,datetime.now())
    return draw_date,number,draw_time


def fc3d(ssc360_type):
    #Open website
    """
    :param self:
    :param ssc_type:
    :rtype : str,datetime,datetime
    """
    url='http://cp.360.cn/'+ssc360_type+'/'
    print url
    now_time=time.localtime()
    number = ''
    r = br.open(url,timeout=300)
    ssc_html = r.read().decode('gb2312')
    #ssc_html = r.read()
    #show the html title
    print '360时时彩',url
    #print br.title()
    ## xpath analyze
    d = etree.HTML(ssc_html)
    #Draw DateNO
    draw_date_tmp = ''.join(d.xpath(u'/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/h3/span/b/text()'))
    draw_date=draw_date_tmp[2:]
    #drow Number
    number=number+''.join(d.xpath(u'/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/div/ul/li[1]/text()'))+','
    number=number+''.join(d.xpath(u'/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/div/ul/li[2]/text()'))+','
    number=number+''.join(d.xpath(u'/html/body/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/div/ul/li[3]/text()'))
    draw_code=number
    #Draw Time
    draw_time=datetime.now().strftime("%Y-%m-%d %H:%M")
    print draw_date,draw_code,datetime.now()
    if (number=='--,--,--'):
        number='0'
    log.logging.info('360时时彩'+'   '+url)
    log.logging.info('date:%s code:%s curtime:%s',draw_date,draw_code,datetime.now())
    return draw_date,number,draw_time