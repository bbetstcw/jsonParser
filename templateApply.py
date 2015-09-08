SERVICE_TRANSLATION = {"activeDirectory":"Active Directory", "automation":"自动化", "backup":"备份", "cdn":"CDN", "cloudServices":"云服务", "eventHubs":"事件中心",
                       "hdinsight":"HDInsight", "mediaService":"媒体服务", "mobileService":"移动服务", "notificationHubs":"通知中心", "redisCache":"Redis 缓存",
                       "scheduler":"计划程序", "serviceBus":"服务总线", "siteRecovery":"站点恢复", "sqlDatabase":"SQL 数据库", "storage":"存储", "trafficManager":"流量管理器",
                       "virtualMachine":"虚拟机", "virtualNetwork":"虚拟网络", "websites":"网站", "applicationGateway":"应用程序网关", "batch":"批处理"}

GLOBAL_LINK = r'http(s)?:\/\/azure.microsoft.com(\/zh\-cn)?\/'

import json
import re

def replaceVideoLink(key):
    return replaceMultiple("./videoLinkJson/"+key+".json", "video_link_template.html", 3)

def replaceRecentUpdate(key):
    return replaceMultiple("./recentUpdateJson/"+key+".json", "recent_update.html")

def replaceTutorialSelector(key):
    optionsJsonStr = readFileToString("./tutorialOptionsJson/"+key+".json")
    options = json.loads(optionsJsonStr)
    if len(options)==1:
        template = readFileToString("tutorialLink.html")
        return replace(template, options)
    else:
        template = readFileToString("tutorial_options.html")
        result = replace(template, options)
        template = readFileToString("tutorialSelector.html")
    return replace(template, [{"options":result, "first_option_title":options[0]["title"], "first_option_link":options[0]["link"]}])

def replaceAll(key):
    
    options = []
    option = json.loads(readFileToString("./contentJson/"+key+".json"))
    option["navigationJsonStr"] = readFileToString("./navigationJson/"+key+".json").strip().replace("'", "\\'")
    option["service_name"] = SERVICE_TRANSLATION[key]
    option["tutorialSelector"] = replaceTutorialSelector(key)
    option["video_links"] = replaceVideoLink(key)

    option["updates"] = replaceRecentUpdate(key)
    options.append(option)
    template = readFileToString("frame.html")
    return replace(template, options)

def replaceMultiple(jsonFileName, templateName, max = 100):
    options = json.loads(readFileToString(jsonFileName))
    if len(options)>max:
        options = options[0:max]
    template = readFileToString(templateName)
    return replace(template, options)


def replace(template, options):
    result = ""
    for option in options:
        replaceResult = template;
        for k,v in option.items():
            replaceResult = replaceResult.replace("{{"+k+"}}", v)
        result += replaceResult+"\n"
    return result

def getAll():
    for k, v in SERVICE_TRANSLATION.items():
        lines = replaceAll(k)
        lines = re.sub(GLOBAL_LINK, "/", lines)
        outputFile = open("./output/"+k+".html", "w", encoding="utf8")
        outputFile.writelines(lines);
        outputFile.close()

def readFileToString(fileName):
    file = open(fileName, "r")
    lines = file.readlines()
    file.close()
    result = ""
    for line in lines:
        result += line
    return result