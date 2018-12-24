from vCenter import Vcenter
from elasticsearch import Elasticsearch
import datetime
import json

class Velastindex():
    def __init__(self, vcenterHost, vcenterUser, vcenterPassword,
                 vcenterPort, elasticHost, elasticPort,
                 indexName, docType):
        self.vcenterHost = vcenterHost
        self.vcenterUser = vcenterUser
        self.vcenterPassword = vcenterPassword
        self.vcenterPort = vcenterPort
        self.elasticHost = elasticHost
        self.elasticPort = elasticPort
        self.indexName = indexName
        self.docType = docType
        self.vc = Vcenter(self.vcenterHost, self.vcenterUser, 
                          self.vcenterPassword, self.vcenterPort)
        self.es = Elasticsearch([{'host': elasticHost, 'port': elasticPort}])
        
        
    def populate(self, id, body):
         self.es.index(index = self.indexName, doc_type = self.docType, 
                       id = id, body = body)
    def populateALL(self):
        for vm in self.vc.retrieveVMs():
            id = vm['name']
            body = vm
            self.populate(id, body)
    
        
        
        
        
