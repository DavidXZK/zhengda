#-*- coding=utf-8 -*-
import codecs
import re
import urllib2
import time
urlfile = file('url.txt').readlines();
if urlfile[0][:3] == codecs.BOM_UTF8:# 前面插入的几个字符
    urlfile[0] = urlfile[0][3:];
fp = open('content.txt','w+');
log = open('log.txt','a+');
log.write(time.strftime('%Y-%m-%d  %H:%M:%S',time.localtime(time.time()))+'\n');
count = 0;#计数器
cc = 0;
for url in urlfile:
    try:
        content = urllib2.urlopen(url).read();
    except Exception,e:
        print url;
        log.write(e.reason+'\n');
        log.write(str(count)+' '+url);
        log.write('\n');
        continue;
    m = re.findall('<h1 class="title">([\s\S]*?)</h1>',content);
    fp.write(m[0]+'\n');
    m = re.findall('<div class="field-item">([\s\S]*?)</div>\
',content);
    if m:
        for part in m:
            part = re.sub('\n','',part);
            part = part.lstrip();
            part = part.rstrip();
            fp.write(part+'\n');
    fp.write('*********\n');
    m = re.findall('<td class="views-field views-field-phpcode">([\s\S]*?)</td>[\s]*?<td class="views-field views-field-phpcode-1">([\s\S]*?)</td>[\s]*?<td class="views-field views-field-field-gs-science-value">([\s\S]*?)</td>[\s]*?<td class="views-field views-field-title">([\s\S]*?)</td>',content);
    if m:
        for part in m:
            for pt in part:
                pt = pt.lstrip();
                pt = pt.rstrip();
                fp.write(pt+'*');
            fp.write('\n');
    else:
        m = re.findall('<td class="views-field" colspan="4">([\s\S]*?)</td>',content);
        if m:
            fp.write(m[0]+'\n');
    fp.write('*********\n');
    m = re.findall('<td class="views-field views-field-phpcode">([^<]*?)</td>[\s]*?<td class="views-field views-field-title">([^<]*?)</td>',content);
    if m:
        for part in m:
            for pt in part:
                pt = re.sub('\n','',pt);
                pt = pt.lstrip();
                pt = pt.rstrip();
                fp.write(pt+'*');
            fp.write('\n');
    else:
        m = re.findall('<td class="views-field" colspan="2">([\s\S]*?)</td>',content);
        if m:
            fp.write(m[0]+'\n');
    fp.write('*********\n');
    m = re.findall('<td class="views-field views-field-phpcode">([^<]*?)</td>[\s]*?<td class="views-field views-field-phpcode-1">([^<]*?)</td>[\s]*?<td class="views-field views-field-title">([\s\S]*?)</td>',content);
    if m:
        for part in m:
            for pt in part:
                pt = re.sub('\n','',pt);
                pt = pt.lstrip();
                pt = pt.rstrip();
                fp.write(pt+'*');
            fp.write('\n');
    fp.write('#######################\n');
        #fp.write(m[0][1]+'...');
    count = count +1;
    print count,'\n';
fp.close();
log.write('************\n');
log.close();
print 'finish',count;
    
