SERVICE_TRANSLATION = {"activeDirectory":"Active Directory", "automation":"自动化", "backup":"备份", "cdn":"CDN", "cloudServices":"云服务", "eventHubs":"事件中心",
                       "hdinsight":"HDInsight", "mediaService":"媒体服务", "mobileService":"移动服务", "notificationHubs":"通知中心", "redisCache":"Redis 缓存",
                       "scheduler":"计划程序", "serviceBus":"服务总线", "siteRecovery":"站点恢复", "sqlDatabase":"SQL 数据库", "storage":"存储", "trafficManager":"流量管理器",
                       "virtualMachine":"虚拟机", "virtualNetwork":"虚拟网络", "websites":"网站", "applicationGateway":"应用程序网关", "batch":"批处理"}


GLOBAL_DOC_LINK = r"http(s)?:\/\/azure.microsoft.com(\/zh\-cn)?\/documentation\/articles\/(P?<docName>[^\/]+)\/"

def refine():
    for k,v in SERVICE_TRANSLATION.items():
        navigationJson = readFileToString("./navigationJson/"+k+".json")
        
    return

def readFileToString(fileName):
    file = open(fileName, "r")
    lines = file.readlines()
    file.close()
    result = ""
    for line in lines:
        result += line
    return result