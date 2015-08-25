# jsonParser
This is a parser that can generate all landing pages.

### Preprocessing
1. The script is writen in python 3.4, so please intall at least python 3.0.
2. If you want to edit it with Visual Studio 2013/2015, please install the python plugin for Visual Studio.

### Format of the input
1. All the input files for htmlOrTxtToJsonParser are grebbed from the global site or from windowsazure.cn

	a. For navigations, they are one-line-html stored in txt files. Since I am using regular expression, I just keep it that way for convenience. There should be another way, but I am still not very good at regular expression, so maybe I will do some refactoring later.

    b. For tutorial options, some of them are html, not one-line, others, which has only one tutorial option, are stored in the following format:
		
		Getting Started with Delivering Video on Demand (VoD) using .NET SDK							#title
		https://azure.microsoft.com/zh-cn/documentation/articles/media-services-dotnet-get-started/ 	#link

	c. Video-links are plain txt file, which are stored in the following format

		backup

		link1:
		http://wacnvideo.streaming.mediaservices.chinacloudapi.cn/9bc8943a-4116-48c6-b818-75e6351f1efd/%E5%9C%A8Azure%E9%97%A8%E6%88%B7%E4%B8%AD%E7%AE%A1%E7%90%86%E5%A4%87%E4%BB%BD%E6%9C%8D%E5%8A%A1.ism/Manifest

		bg:
		http://wacnstorage.blob.core.chinacloudapi.cn/marketing-resource/media/VideoCenter/image/%E5%A4%87%E4%BB%BD/%E5%9C%A8Azure%E9%97%A8%E6%88%B7%E4%B8%AD%E7%AE%A1%E7%90%86%E5%A4%87%E4%BB%BD%E6%9C%8D%E5%8A%A1.png

		description:
		在Azure门户中管理备份服务
		课程系列: 快速入门服务: 备份服务
		视频长度: 4' 9"发布时间: 2015年6月18日
		备份服务介绍，使用备份服务进行备份和恢复

2. Input files for templateApply are all json.

	a. Navigation
		
		{
    		"service": " 虚拟机 ",
    		"navigation": [
        		{
            		"group": "概述",
            		"articles": [
                		{
                    		"id": "link_what_is_azure_vm",
                    		"title": " 什么是 Azure 虚拟机 ",
                    		"link": "/zh-cn/services/virtual-machines/"
                		},
                		...
            		],
            		"id": "area_about"
        		},
				...
			]
			"id": "VirtualMachines"
		}

	b. Recent Update
		
		[
    		{
        		"update_title": "General availability: G-Series and GS-Series virtual machines in multiple new regions",
        		"update_date": "2015/8/19",
        		"update_description": "The G-Series provides more memory and more local solid-state drive storage than other Azure virtual machines. In addition, the GS-Series supports Premium storage across the East US 2, West US, and West Europe regions.",
        		"update_link": "/test"
    		},
    		...
		]

	c. Tutorial options

		[
    		{
        		"title": "Get a tenant",
        		"link": "https://azure.microsoft.com/zh-cn/documentation/articles/active-directory-howto-tenant/"
    		},
    		...
		]

	d. Video links
		
		[
    		{
        		"CourseSeries": "快速入门",
        		"Services": "备份服务",
        		"VideoUrl": "http://wacnvideo.streaming.mediaservices.chinacloudapi.cn/9bc8943a-4116-48c6-b818-75e6351f1efd/%E5%9C%A8Azure%E9%97%A8%E6%88%B7%E4%B8%AD%E7%AE%A1%E7%90%86%E5%A4%87%E4%BB%BD%E6%9C%8D%E5%8A%A1.ism/Manifest",
        		"ImageUrl": "http://wacnstorage.blob.core.chinacloudapi.cn/marketing-resource/media/VideoCenter/image/%E5%A4%87%E4%BB%BD/%E5%9C%A8Azure%E9%97%A8%E6%88%B7%E4%B8%AD%E7%AE%A1%E7%90%86%E5%A4%87%E4%BB%BD%E6%9C%8D%E5%8A%A1.png",
        		"Duration": "4' 9\"",
        		"PublishTime": "2015年6月18日",
        		"Description": "备份服务介绍，使用备份服务进行备份和恢复",
        		"Title": "在Azure门户中管理备份服务"
    		},
			...
		]

	e. Content

		{
    		"subtitle": "了解如何设置、迁移和管理虚拟机",
    		"tutorial_message": "创建运行以下系统的 VM：",
    		"update_search_links": "/test"
		}


3. The parser for content and recent update are not yet implemented, because the farmat of input for those are not yet known. A simple copy from the global site would be bad, because a lot of them are not translated.