SERVICE_TRANSLATION = {"activeDirectory":"Active Directory", "automation":"�Զ���", "backup":"����", "cdn":"CDN", "cloudServices":"�Ʒ���", "eventHubs":"�¼�����",
                       "hdinsight":"HDInsight", "mediaService":"ý�����", "mobileService":"�ƶ�����", "notificationHubs":"֪ͨ����", "redisCache":"Redis ����",
                       "scheduler":"�ƻ�����", "serviceBus":"��������", "siteRecovery":"վ��ָ�", "sqlDatabase":"SQL ���ݿ�", "storage":"�洢", "trafficManager":"����������",
                       "virtualMachine":"�����", "virtualNetwork":"��������", "websites":"��վ", "applicationGateway":"Ӧ�ó�������", "batch":"������"}


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