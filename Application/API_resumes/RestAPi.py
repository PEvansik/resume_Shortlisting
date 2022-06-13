from email import header
from urllib import response
import requests
import json
from helper import access_token,instance_url
from concurrent.futures import ThreadPoolExecutor
import os.path

def sf_api_call(action,paramaters = {},method = 'get',data={}):

    """This is the helper
     function that we are 
     using to make call in 
     the rest api of the salesforce platform
    """ 
    headers = {
        'content-type': 'application/json',
        'Accept-Encoding':'gzip',
        'Authorization':'Bearer %s' % access_token
    }
    if method=='get':
        r = requests.request(method,instance_url+action,headers=headers,params=paramaters,timeout=30)
    elif method in ['post','patch']:
        r = requests.request(method,instance_url+action,headers = headers,json = data,params=paramaters,timeout = 10)
    else:
        raise ValueError("Method should be get or post or patch")
    print('Debug: API %s call : %s' % (method,r.url))
    if r.status_code < 300:
        if method=='patch':
            return None
        else:
            return r.json()
    else:
        raise Exception('API error when calling %s : %s' % (r.url, r.content))



record_json=sf_api_call('/services/data/v39.0/query/', {
    'q': 'Select id,Title,FileType,FileExtension from ContentVersion'
}) 

donwnload_url="https://dawnrecruit-dev-ed.my.salesforce.com/services/data/v39.0/sobjects/ContentVersion"

def save_file(record):
    objectId,fileName,FileExt = record["Id"],record["Title"],record["FileExtension"]
    headers = {
        'Accept-Encoding':'gzip',
        'Authorization':'Bearer %s' % access_token
    }
    response = requests.get(donwnload_url+"/"+objectId+"/VersionData",headers=headers)
    File = open(fileName+"."+FileExt,"wb")
    File.write(response.content)
    File.close()
    


record_list=[]
for record in record_json["records"]:
    # print(record_json["ID"])
    record_list.append(record)
    # save_file(record["Id"],record["Title"],record["FileExtension"])
# 
# curl https://dawnrecruit-dev-ed.my.salesforce.com/services/data/v39.0/sobjects/ContentVersion/0685j00000AdTP2AAN/VersionData -H "Authorization: Bearer 00D5j00000AFOK9!ARQAQAeLH9rEBvs7DR5MUsfRDGKIVQ8c0Ib8U0lVS6jNrOKllJS3NoWMDX.6Sw95_jkSFiINPgfyfw.X.jsUHBAP4WlnPv2L" --output saax.pdf



with ThreadPoolExecutor() as exzecutor:
    exzecutor.map(save_file, record_list)