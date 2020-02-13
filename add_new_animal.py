# -*- coding: utf-8 -*-
import sys
import os
from subprocess import call



def fillDicts(string):
    data=string.rstrip().split('\t')
    if data[-2]!='None':
        dad[data[0]]=data[-2]
    if data[-1]!='None':
        mom[data[0]]=data[-1]
    mg[data[2]]=data[0]
    golden[data[0]]=[data[6],data[7],data[8]]
    nan.add(data[2])
    if data[1]=='F':
        #F1
        fknd=data[3].lower()+'\t'+data[4]+'\t'+data[5]
        if data[3]!='None' and data[4]!='None' and data[5]!='None':
            if fknd not in f_klich_nom_dr:
                f_klich_nom_dr[fknd]=set([data[0]])
            else:
                f_klich_nom_dr[fknd].add(data[0])
        if len(data[4])>6:
            #F2
            fn=data[4]
            if fn not in f_nom:
                f_nom[fn]=set([data[0]])
            else:
                f_nom[fn].add(data[0])
        #F3
        fnd=data[4]+'\t'+data[5]
        if data[5]!='None':
            if fnd not in f_nom_dr:
                f_nom_dr[fnd]=set([data[0]])
            else:
                f_nom_dr[fnd].add(data[0])
    elif data[1]=='M':
        #M1
        mkn=data[3].lower()+'\t'+data[4]
        if data[3]!='None' and data[4]!='None':
            if mkn not in m_klich_nom:
                m_klich_nom[mkn]=set([data[0]])
            else:
                m_klich_nom[mkn].add(data[0])
        #M2
        mnd=data[4]+'\t'+data[5]
        if data[4]!='None' and data[5]!='None':
            if mnd not in m_nom_dr:
                m_nom_dr[mnd]=set([data[0]])
            else:
                m_nom_dr[mnd].add(data[0])
        #M3
        if len(data[4])>5:
            if data[4] not in m_nom:
                m_nom[data[4]]=set([data[0]])
            else:
                m_nom[data[4]].add(data[0])



def checkMg(data1,match_set):
    #if len(match_set)>1:
        #print data1+' совпало с несколькими MG!!!'
    return list(match_set)[0]

count_mgf = 1
count_mgm = 1

print "print full path to dirs with testfiles: "
directorys= raw_input()
print "print prefix for mg: "
prefix= raw_input()
print "print date for files: "
date = raw_input()
#directorys = '/5500disk/home/rusmari/Ilya/Rodstvo/Rodstvo_july/testfiles2/'
dirs = os.listdir(directorys)
#testfile=sys.argv[1]
testfile='testfile'
ch=0
for d in dirs:
    ch+=1
    print ch
    golden = {}
    mg = {}
    nan = set()

    f_klich_nom_dr={}
    f_nom_dr={}
    f_nom={}
    m_klich_nom={}
    m_nom_dr={}
    m_nom={}

    dad = {}
    mom = {}
    print d
    for l in open('/5500disk/home/rusmari/Ilya/Rodstvo/Rodstvo_july/File_sootv_unite_'+date+'.tsv'):
        fillDicts(l)

    with open(directorys+d+'/'+testfile+'_decision.tsv','w') as f:
        for l in open(directorys+d+'/'+testfile):
            data=l.rstrip().split('\t')
            flag = 0
            if (data[1] in mg):
                f.write(data[1]+'\t'+'уже в базе данных. MG:'+'\t'+mg[data[1]]+'\n')
                flag = 1
            elif (data[1] not in mg):
                if data[0]=='F':
                    fknd=data[2].lower()+'\t'+data[3]+'\t'+data[4]
                    if fknd in f_klich_nom_dr:
                        f.write(data[1]+'\t'+'совпадает по кличке, номеру, дате рождения с : '+'\t'+' '.join(list(f_klich_nom_dr[fknd]))+'\n')
                        mg[data[1]]=checkMg(data[1],f_klich_nom_dr[fknd])
                        flag = 1

                    if flag == 0:
                        fn=data[3]
                        if fn in f_nom:
                            f.write(data[1]+'\t'+'совпадает по номеру (>=7) :'+'\t'+' '.join(list(f_nom[fn]))+'\n')
                            mg[data[1]]=checkMg(data[1],f_nom[fn])
                            flag = 1

                    if flag == 0:
                        fnd=data[3]+'\t'+data[4]
                        if fnd in f_nom_dr:
                            f.write(data[1]+'\t'+'совпадает номеру, дате рождения с :'+'\t'+' '.join(list(f_nom_dr[fnd]))+'\n')
                            mg[data[1]]=checkMg(data[1],f_nom_dr[fnd])
                            flag = 1

                    if flag == 0:
                        mg[data[1]]='MGF'+prefix+str('0'*(7-len(str(count_mgf))))+str(count_mgf)
                        count_mgf+=1
                        f.write(data[1]+'\t'+' совпадений не найдено. Новый MG : '+'\t'+mg[data[1]]+'\n')
                        golden[mg[data[1]]]=[data[2],data[3],data[4]]


                elif data[0]=='M':
                    mkn=data[2].lower()+'\t'+data[3]
                    if mkn in m_klich_nom:
                        f.write(data[1]+'\t'+'совпадает по кличке, номеру с : '+'\t'+' '.join(list(m_klich_nom[mkn]))+'\n')
                        mg[data[1]]=checkMg(data[1],m_klich_nom[mkn])
                        flag = 1

                    if flag == 0:
                        mnd=data[3]+'\t'+data[4]
                        if mnd in m_nom_dr:
                            f.write(data[1]+'\t'+'совпадает по номеру, дате рождения с :'+'\t'+' '.join(list(m_nom_dr[mnd]))+'\n')
                            mg[data[1]]=checkMg(data[1],m_nom_dr[mnd])
                            flag = 1

                    if flag == 0:
                        n = data[3]
                        if n in m_nom:
                            f.write(data[1]+'\t'+'совпадает по номеру (>5):'+'\t'+' '.join(list(m_nom[n]))+'\n')
                            mg[data[1]]=checkMg(data[1],m_nom[n])
                            flag = 1

                    if flag == 0:
                        mg[data[1]]='MGM'+prefix+str('0'*(7-len(str(count_mgm))))+str(count_mgm)
                        count_mgm+=1
                        f.write(data[1]+'\t'+' совпадений не найдено. Новый MG : '+'\t'+mg[data[1]]+'\n')
                        golden[mg[data[1]]]=[data[2],data[3],data[4]]

    with open(directorys+d+'/'+testfile+'_temp','w') as f:
        for l in open(directorys+d+'/'+testfile):
            data=l.rstrip().split('\t')
            for k in [-2,-1,1]:
                if data[k] not in mg:
                    mg[data[k]]='None'
            wr=[mg[data[1]],'\t'.join(data[:-2]),mg[data[-2]],data[-2],mg[data[-1]],data[-1]]
            f.write('\t'.join(wr)+'\n')
    with open(directorys+d+'/'+testfile+'_add_to_filesootv.tsv','w') as f:
        with open(directorys+d+'/'+testfile+'_warnings.tsv','w') as war:
            for l in open(directorys+d+'/'+testfile+'_temp'):
                data=l.rstrip().split('\t')
                if (data[0] in dad) and (data[-4]!='None') and (dad[data[0]]!='None'):
                    if data[-4]!=dad[data[0]]:
                        war.write('Отец '+data[2]+' не совпадает!'+'\n')
                        war.write('У нас в БД '+dad[data[0]]+' '+' '.join(golden[dad[data[0]]])+'\n')
                        war.write('В файле '+testfile+' '+data[-4]+' '+' '.join(golden[data[-4]])+'\n')
#                        mg[data[-3]]=dad[data[0]]
                elif (data[0] not in dad) and (data[-4]!='None'):
                    dad[data[0]]=data[-4]

                if (data[0] in mom) and (data[-2]!='None') and (mom[data[0]]!='None'):
                    if data[-2]!=mom[data[0]]:
                        war.write('Мать '+data[2]+' не совпадает!'+'\n')
                        war.write('У нас в БД '+mom[data[0]]+' '+' '.join(golden[mom[data[0]]])+'\n')
                        war.write('В файле '+testfile+' '+data[-2]+' '+' '.join(golden[data[-2]])+'\n')
#                        mg[data[-1]]=mom[data[0]]
                elif (data[0] not in mom) and (data[-2]!='None'):
                    mom[data[0]]=data[-2]

        for l in open(directorys+d+'/'+testfile+'_temp'):
            data=l.rstrip().split('\t')
            #if data[2] not in nan:
            if data[0] not in dad:
                dad[data[0]]='None'
            if data[0] not in mom:
                mom[data[0]]='None'
            line=mg[data[2]]+'\t'+'\t'.join(data[1:6])+'\t'+'\t'.join(data[3:6])+'\t'+dad[data[0]]+'\t'+mom[data[0]]+'\n'
            f.write(line)

    command = ('python /5500disk/home/rusmari/Ilya/Rodstvo/Rodstvo_july/unite_res_filesootv.py '+directorys+d+'/'+testfile+'_add_to_filesootv.tsv '+date).split(' ')
    print command
    call(command)

