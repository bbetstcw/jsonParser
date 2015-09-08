FIRST_LEVEL_REG = r'^\<div class="wa-navigationLeft" data-control="toggle"\> \<a [^\>|^\<]*\>(?P<service>[^\>|^\<]+)\<\/a\>(?P<navigation>.+)\<\/div\>$'

SERVICE_NAME_PATTERN = '.*data-service-name="(?P<serviceID>[^\>|^\<|^"]*)".*'

FIRST_LEVEL_SPLIT_PATTERN = '(\<li [^\>|^\<]*\> \<a [^\>|^\<]*\>[^\>|^\<]+\<\/a\> \<ul [^\>|^\<]*\> (\<li\> \<a [^\>|^\<]*\>[^\>|^\<]+\<\/a\> \<\/li\> )+\<\/ul\> \<\/li\>)+'

SECOND_LEVEL_REG = r'^\<li [^\>|^\<]*\> \<a [^\>|^\<]*ms\.top="(?P<groupID>[^\>|^\<|^"]*)"[^\>|^\<]*\>(?P<groupName>[^\>|^\<]+)\<\/a\>.+'

SECOND_LEVEL_SPLIT_PATTERN = '(\<li\> \<a [^\>|^\<]*\>[^\>|^\<]+\<\/a\> \<\/li\>)+'

THIRD_LEVEL_REG = r'^\<li\> \<a [^\>|^\<]*href="(?P<link>[^\>|^\<|^"]*)"[^\>|^\<]*ms\.top="(?P<articleID>[^\>|^\<|^"]*)"[^\>|^\<]*\>(?P<articleTitle>[^\>|^\<]+)\<\/a\> \<\/li\>$'

SERVICE_TRANSLATION = {"activeDirectory":"Active Directory", "automation":"自动化", "backup":"备份", "cdn":"CDN", "cloudServices":"云服务", "eventHubs":"事件中心",
                       "hdinsight":"HDInsight", "mediaService":"媒体服务", "mobileService":"移动服务", "notificationHubs":"通知中心", "redisCache":"Redis 缓存",
                       "scheduler":"计划程序", "serviceBus":"服务总线", "siteRecovery":"站点恢复", "sqlDatabase":"SQL 数据库", "storage":"存储", "trafficManager":"流量管理器",
                       "virtualMachine":"虚拟机", "virtualNetwork":"虚拟网络", "websites":"网站", "applicationGateway":"应用程序网关", "batch":"批处理"}

VIDEO_SERVICE_PATTERN = r'课程系列: (?P<CourseSeries>.+)服务: (?P<Services>.+)'
VIDEO_SERVICE_PATTERN2 = r'视频长度: (?P<Duration>.+)发布时间: (?P<PublishTime>.+)'
OPTION_PATTERN = r'\<option value="(?P<link>[^\>|^\<|^"]*)">(?P<title>[^\>|^\<]*)\<\/option\>'

import re
import json

def navigationParse(file):
    line = file.readline()
    m = re.match(FIRST_LEVEL_REG, line)
    dict = m.groupdict()
    navigationJson = {}
    navigationJson["service"]= dict["service"];

    firstLevelList = re.findall(FIRST_LEVEL_SPLIT_PATTERN, dict["navigation"])

    m = re.match(SERVICE_NAME_PATTERN, dict["navigation"])
    dict = m.groupdict()
    navigationJson["id"]= dict["serviceID"]

    navigation = []
    for l in firstLevelList:
        m = re.match(SECOND_LEVEL_REG, l[0].strip())
        dict = m.groupdict()
        group = {}
        group["group"] = dict["groupName"]
        group["id"] = dict["groupID"]

        secondLevelList = re.findall(SECOND_LEVEL_SPLIT_PATTERN, l[0].strip())
        articles = []
        for articleL in secondLevelList:
            m = re.match(THIRD_LEVEL_REG, articleL)
            dict = m.groupdict()
            article = {}
            article["link"] = dict["link"]
            article["id"] = dict["articleID"]
            article["title"] = dict["articleTitle"]
            articles.append(article)
        
        group["articles"] = articles
        navigation.append(group)

    navigationJson["navigation"] = navigation
    return json.dumps(navigationJson)

def videoParse(key, value):
    try:
        file = open("./video-link/"+key+".txt", "r", encoding= "utf8")
    except FileNotFoundError:
        return "[]";
    line = file.readline()
    videoJson = []
    while line!="":
        if line[0:4]=="link":
            link = {}
            line = file.readline()
            link["VideoUrl"] = line.strip()
            while line[0:3]!="bg:":
                line = file.readline()
            line = file.readline()
            link["ImageUrl"] = line.strip()
            while line[0:12]!="description:":
                line = file.readline()
            line = file.readline()
            link["Title"] = line.strip()
            line = file.readline()
            m = re.match(VIDEO_SERVICE_PATTERN, line)
            dict = m.groupdict();
            link["CourseSeries"] = dict["CourseSeries"]
            link["Services"] = dict["Services"]
            line = file.readline()
            m = re.match(VIDEO_SERVICE_PATTERN2, line)
            dict = m.groupdict();
            link["Duration"] = dict["Duration"]
            link["PublishTime"] = dict["PublishTime"]
            line = file.readline()
            link["Description"] = line.strip()
            videoJson.append(link);
        line = file.readline()
    file.close()
    return json.dumps(videoJson)

def tutorialOptionParser(file):
    line = file.readline()
    options = []
    if line[0:7] == '<select':
        line = file.readline().strip()
        while line[0:8] != '</select':
            m = re.match(OPTION_PATTERN, line)
            option = {}
            dict = m.groupdict();
            option["title"] = dict["title"]
            option["link"] = dict["link"]
            options.append(option)
            line = file.readline().strip()
    else:
        option = {}
        option["title"] = line.strip()
        line = file.readline()
        option["link"] = line.strip()
        options.append(option)

    return json.dumps(options)

def recentUpdateParser(file):
    line = file.readline()
    recentUpdates = []
    while line!= "":
        if line[0:3] == '201':
            update = {}
            update["update_date"] = line.strip()
            line = file.readline()
            update["update_title"] = line.strip()
            line = file.readline()
            update["update_description"] = line.strip()
            line = file.readline()
            update["update_detail"] = line.strip()
            line = file.readline()
            update["update_link"] = line.strip()
            recentUpdates.append(update)
        line = file.readline()
    return json.dumps(recentUpdates)

def parse():
    for k,v in SERVICE_TRANSLATION.items():
        print(k)
        file = open("./navigations/"+k+".txt", "r")
        navigationJson = navigationParse(file)
        file.close()
        file = open("./navigationJson/"+k+".json", "w", encoding= "utf8")
        file.writelines(navigationJson)
        file.close()
        videoJson = videoParse(k, v)
        file = open("./videoLinkJson/"+k+".json", "w", encoding= "utf8")
        file.writelines(videoJson)
        file.close()

    
        file = open("./tutorialOptions/"+k+".txt", "r")
        tutorialOptionJson = tutorialOptionParser(file)
        file.close()
        file = open("./tutorialOptionsJson/"+k+".json", "w", encoding= "utf8")
        file.writelines(tutorialOptionJson)
        file.close()
        
        file = open("./recentUpdate/"+k+".txt", "r")
        recentUpdateJson = recentUpdateParser(file)
        file.close()
        file = open("./recentUpdateJson/"+k+".json", "w", encoding= "utf8")
        file.writelines(recentUpdateJson)
        file.close()
