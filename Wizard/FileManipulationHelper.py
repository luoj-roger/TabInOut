'''
Created on 2 Jun 2016

@author: mbaxkhm4

Created at the University of Manchester, School of Computer Science
Licence GNU/GPL 3.0
'''
import os
from os import listdir
from os.path import isfile, join
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def CreateFoderIfNotExist(FolderName):
    if not os.path.exists(FolderName):
        os.makedirs(FolderName)

def CreateFolderStructure():
    CreateFoderIfNotExist("Projects")
    

def readProjects():
    projects = [os.path.join("",o) for o in os.listdir("Projects") if os.path.isdir(os.path.join("Projects",o))]
    return projects

def CreateProjectCfgFileIfNotExist(Folder):
    if not os.path.exists(Folder+"/Config.cfg"):
        f = open(Folder+"/Config.cfg",'w')
        f.write('Host:127.0.0.1\n') # python will convert \n to os.linesep
        f.write('Port:3306\n')
        f.write('User:root\n')
        f.write('Pass:\n')
        f.write('Database:table_db')
        f.close() # you can omit in most cases as the destructor will call it

def SaveToConfigFile(project_name,hostname,port,user,pasword,database):
    f = open("Projects/"+project_name+"/Config.cfg",'w')
    f.write('Host:'+hostname+'\n') # python will convert \n to os.linesep
    f.write('Port:'+port+'\n')
    f.write('User:'+user+'\n')
    f.write('Pass:'+pasword+'\n')
    f.write('Database:'+database+'\n')
    f.close()

def LoadDBConfigFile(project_name):
    f  = open("Projects/"+project_name+"/Config.cfg",'r')
    lines = f.readlines()
    dbSettings = {}
    for line in lines:
        parts = line.split(':')
        if(parts[0]=='Host'):
            dbSettings['Host']=parts[1].replace('\n','')
        if(parts[0]=='Port'):
            dbSettings['Port']=parts[1].replace('\n','')
        if(parts[0]=='User'):
            dbSettings['User']=parts[1].replace('\n','')
        if(parts[0]=='Pass'):
            dbSettings['Pass']=parts[1].replace('\n','')
        if(parts[0]=='Database'):
            dbSettings['Database']=parts[1].replace('\n','')
    return dbSettings

def SaveCueList(rule_path,rule_name, whitelist,blacklist,typeVar,wl_look_head,wl_look_stub,wl_look_super,wl_look_data,bl_look_head,bl_look_stub,bl_look_super,bl_look_data):
    f = open(rule_path+'/'+rule_name+'_WhiteList.lst','w')
    f.write('Type:'+"WhiteList"+'\n')
    f.write('Header:'+str(wl_look_head.get())+'\n')
    f.write('Stub:'+str(wl_look_stub.get())+'\n')
    f.write('Super-row:'+str(wl_look_super.get())+'\n')
    f.write('Data:'+str(wl_look_data.get())+'\n')
    f.write('WordList:\n')
    for item in whitelist:
        f.write(item+'\n')
    f.close
    f = open(rule_path+'/'+rule_name+'_BlackList.lst','w')
    f.write('Type:'+"BlackList"+'\n')
    f.write('Header:'+str(bl_look_head.get())+'\n')
    f.write('Stub:'+str(bl_look_stub.get())+'\n')
    f.write('Super-row:'+str(bl_look_super.get())+'\n')
    f.write('Data:'+str(bl_look_data.get())+'\n')
    f.write('WordList:\n')
    for item in blacklist:
        f.write(item+'\n')
    f.close
    
def SaveCueListSem(rule_path,rule_name, whitelist,blacklist,typeVar, wl_look_head,wl_look_stub,wl_look_super,wl_look_data,bl_look_head,bl_look_stub,bl_look_super,bl_look_data):
    f = open(rule_path+'/'+rule_name+'_WhiteList.lst','w')
    f.write('Type:'+"WhiteList"+'\n')
    f.write('Header:'+str(wl_look_head.get())+'\n')
    f.write('Stub:'+str(wl_look_stub.get())+'\n')
    f.write('Super-row:'+str(wl_look_super.get())+'\n')
    f.write('Data:'+str(wl_look_data.get())+'\n')
    f.write('Sem:'+str("1")+'\n')
    f.write('SemanticTypes:\n')
    for item in whitelist:
        f.write(item+'\n')
    f.close
    f = open(rule_path+'/'+rule_name+'_BlackList.lst','w')
    f.write('Type:'+"BlackList"+'\n')
    f.write('Header:'+str(bl_look_head.get())+'\n')
    f.write('Stub:'+str(bl_look_stub.get())+'\n')
    f.write('Super-row:'+str(bl_look_super.get())+'\n')
    f.write('Data:'+str(bl_look_data.get())+'\n')
    f.write('WordList:\n')
    for item in blacklist:
        f.write(item+'\n')
    f.close
     
    
def SaveBlackList(rule_path,blakclist):
    f = open(rule_path+'/BlackList.lst','w')
    for item in blakclist:
        f.write(item+'\n')
    f.close
def MakeRuleCFGFile(rule_path,vClsIn,vDefUnit,vPosUnit,pragVar,vRuleType,vLexSemRule,wl_look_head,wl_look_stub,wl_look_super,wl_look_data):
    f = open(rule_path+'/Rule.cfg','w')
    f.write("Class:"+str(vClsIn.get().replace('\n',''))+'\n')
    f.write("RuleType:"+str(vRuleType.get().replace('\n',''))+'\n')
    if(vRuleType.get()=="Numeric" or vRuleType.get()=="Categorical"):
        f.write("DefUnit:"+str(vDefUnit.get().replace('\n',''))+'\n')
        f.write("PosUnit:"+str(vPosUnit.get().replace('\n',''))+'\n')
    #if(vRuleType.get()=="Categorical"):
    #    f.write("PosCategories:"+str(vPosUnit.get().replace('\n',''))+'\n')
    f.write("PragClass:"+str(pragVar.get().replace('\n',''))+'\n')
    f.write("RuleCreationMech:"+str(vLexSemRule.get().replace('\n',''))+'\n')
    f.write("DataInHeader:"+str(wl_look_head.get())+'\n')
    f.write("DataInStub:"+str(wl_look_stub.get())+'\n')
    f.write("DataInSuperRow:"+str(wl_look_super.get())+'\n')
    f.write("DataInData:"+str(wl_look_data.get())+'\n')
    f.close()

def loadVariables(project_name):
    project_folder = 'Projects/'+project_name+'/'
    projects = [os.path.join("",o) for o in os.listdir(project_folder) if os.path.isdir(os.path.join(project_folder,o))]
    return projects

def loadRules(project_name,var_name):
    project_folder = 'Projects/'+project_name+'/'+var_name+'/'
    projects = [os.path.join("",o) for o in os.listdir(project_folder) if os.path.isdir(os.path.join(project_folder,o))]
    return projects
    
def loadWhiteList(project_name,rule_name,variable):
    Rule_path = "Projects/" + project_name + '/' + variable.replace('\n','') + '/' + rule_name + '/' + rule_name +'_WhiteList.lst'
    f = open(Rule_path,'r')
    whitelist = f.readlines()
    return whitelist

def loadBlackList(project_name,rule_name,variable):
    Rule_path = "Projects/"+project_name+'/'+variable.replace('\n','')+'/'+rule_name+'/'+rule_name+'_BlackList.lst'
    f = open(Rule_path,'r')
    blacklist = f.readlines()
    return blacklist


def loadRuleConfig(project_name,rule_name,variable):
    Rule_path = "Projects/"+project_name+'/'+variable+'/'+rule_name+'/Rule.cfg'
    f = open(Rule_path,'r')
    config = f.readlines()
    conf = {}
    for cfg in config:
        sp = cfg.split(':')
        if sp[0]=='Class':
            conf['Class']=sp[1]
        if sp[0]=='DefUnit':
            conf['DefUnit']=sp[1]
        if sp[0]=='PosUnit':
            conf['PosUnit']=sp[1]
        if sp[0]=='PragClass':
            conf['PragClass']=sp[1]
        if sp[0]=='RuleType':
            conf['RuleType']=sp[1]
        if sp[0]=='RuleCreationMech':
            conf['RuleCreationMech']=sp[1]
        if sp[0]=='PosCategories':
            conf['Categories']=sp[1]
        if sp[0]=='DataInHeader':
            conf['DataInHeader']=sp[1].replace('\n','')
        if sp[0]=='DataInStub':
            conf['DataInStub']=sp[1].replace('\n','')
        if sp[0]=='DataInSuperRow':
            conf['DataInSuperRow']=sp[1].replace('\n','')
        if sp[0]=='DataInData':
            conf['DataInData']=sp[1].replace('\n','')
    return conf

def LoadRules(path):
    f = open(path,'r')
    rules = f.readlines()
    return rules

def SaveSyntacticRules(rules,project_name,rule_name,variable_name):
    Rule_path = "Projects/"+project_name+'/'+variable_name+'/'+rule_name+'/SyntacticRules.sin'
    f = open(Rule_path,'w')
    f.write(rules)
    f.close()
    

            
    

        
#CreateFolderStructure()
#print readProjects()
