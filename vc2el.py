#!/usr/bin/python3.6
from Velasticsearch import Velastindex
from vCenter import Vcenter

#Determine elasticsearch the index_name and doc-type 
indexName = ""
docType = ""

#Determine the source vCenter
vcenterHost = "" 
vcenterUser = ""
vcenterPassword = ""
vcenterPort = 443

#Determine the target elasticsearch
elasticHost = ''
elasticPort = 9200

#Pushed data into the elasticsearch as per given info provided above
ve = Velastindex(vcenterHost, vcenterUser, vcenterPassword, 
                 vcenterPort, elasticHost, elasticPort, indexName, docType)

ve.populateALL()
    
