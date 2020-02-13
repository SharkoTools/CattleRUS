# -- coding: utf-8 --
from collections import Counter
import sys
date=sys.argv[1]
nom = []
day = []
nam = []
mom = []
dad = []
prev_num='MGF0000001'
di= {}
golden_parents = {}
k = 0
#for l in open('Sort_Replace_new_sootv_bulls.tsv'):
for l in open('/5500disk/home/rusmari/Ilya/Rodstvo/Rodstvo_july/Sort_For_File_sootv_unite_'+date+'.tsv'):
	data=l.rstrip().split('\t')
	if len(data)<=1:
		continue
	else:
		if data[0] == prev_num:
				day.append(data[5])
				nom.append(data[4])
				nam.append(data[3])
				mom.append(data[-1])
				dad.append(data[-2])
				prev_num = data[0]
		else:
			if len(Counter(nam).most_common()) > 1:
				if str(dict(Counter(nam).most_common(1)).keys()[0]).isdigit() or len(str(dict(Counter(nam).most_common(1)).keys()[0]))<2 or str(dict(Counter(nam).most_common(1)).keys()[0]) == 'None':
					c_nam = dict(Counter(nam).most_common()[1:2]).keys()
				else:
					c_nam = dict(Counter(nam).most_common(1)).keys()
			else:
				c_nam = dict(Counter(nam).most_common(1)).keys()
			if len(Counter(nom).most_common()) > 1:
				if str(dict(Counter(nom).most_common(1)).keys()[0]) == 'None':
					c_nom = dict(Counter(nom).most_common()[1:2]).keys()
				else:

					c_nom = dict(Counter(nom).most_common(1)).keys()
			else:
				c_nom = dict(Counter(nom).most_common(1)).keys()
			if len(Counter(day).most_common()) > 1:
				if str(dict(Counter(day).most_common(1)).keys()[0]) == 'None':
					c_day= dict(Counter(day).most_common()[1:2]).keys()
				else:
					c_day = dict(Counter(day).most_common(1)).keys()
			else:
				c_day = dict(Counter(day).most_common(1)).keys()

			if len(Counter(dad).most_common()) > 1:
				if str(dict(Counter(dad).most_common(1)).keys()[0]) == 'None':
					c_dad= dict(Counter(dad).most_common()[1:2]).keys()
				else:
					c_dad = dict(Counter(dad).most_common(1)).keys()
			else:
				c_dad = dict(Counter(dad).most_common(1)).keys()

			if len(Counter(mom).most_common()) > 1:
				if str(dict(Counter(mom).most_common(1)).keys()[0]) == 'None':
					c_mom= dict(Counter(mom).most_common()[1:2]).keys()
				else:
					c_mom = dict(Counter(mom).most_common(1)).keys()
			else:
				c_mom = dict(Counter(mom).most_common(1)).keys()
			#c_day = dict(Counter(day).most_common(1)).keys()
			#print data
			#print c_nam
			#print c_nom
			#print c_day

			summ = c_nam[0] + '\t' + c_nom[0] + '\t' + c_day[0]
			if prev_num in di:
				print 'ooops'
				print prev_num
			di[prev_num] = summ
			golden_parents[prev_num]=[c_dad[0],c_mom[0]]
			#print di_grand
			summ = ''
			prev_num = data[0]
			nam = []
			nom = []
			day = []
			mom = []
			dad = []

			k += 1

			nam.append(data[3])
			nom.append(data[4])
			day.append(data[5])
			mom.append(data[-1])
			dad.append(data[-2])
			#if k % 100 == 0:
			#	print k

	#for last group	
else:		
			if len(Counter(nam).most_common()) > 1:
				if str(dict(Counter(nam).most_common(1)).keys()[0]).isdigit() or len(str(dict(Counter(nam).most_common(1)).keys()[0]))<2:
					c_nam = dict(Counter(nam).most_common()[1:2]).keys()
				else:
					c_nam = dict(Counter(nam).most_common(1)).keys()
			else:
				c_nam = dict(Counter(nam).most_common(1)).keys()
			if len(Counter(nom).most_common()) > 1:
				if str(dict(Counter(nom).most_common(1)).keys()[0]) == 'None':
					c_nom = dict(Counter(nom).most_common()[1:2]).keys()
				else:

					c_nom = dict(Counter(nom).most_common(1)).keys()
			else:
				c_nom = dict(Counter(nom).most_common(1)).keys()
			if len(Counter(day).most_common()) > 1:
				if str(dict(Counter(day).most_common(1)).keys()[0]) == 'None':
					c_day= dict(Counter(day).most_common()[1:2]).keys()
				else:
					c_day = dict(Counter(day).most_common(1)).keys()
			else:
				c_day = dict(Counter(day).most_common(1)).keys()
			if len(Counter(dad).most_common()) > 1:
				if str(dict(Counter(dad).most_common(1)).keys()[0]) == 'None':
					c_dad= dict(Counter(dad).most_common()[1:2]).keys()
				else:
					c_dad = dict(Counter(dad).most_common(1)).keys()
			else:
				c_dad = dict(Counter(dad).most_common(1)).keys()

			if len(Counter(mom).most_common()) > 1:
				if str(dict(Counter(mom).most_common(1)).keys()[0]) == 'None':
					c_mom= dict(Counter(mom).most_common()[1:2]).keys()
				else:
					c_mom = dict(Counter(mom).most_common(1)).keys()
			else:
				c_mom = dict(Counter(mom).most_common(1)).keys()
			#print c_nam
			#print c_nom
			#print c_day
			summ = c_nam[0] + '\t' + c_nom[0] + '\t' + c_day[0]
			di[prev_num] = summ
			golden_parents[prev_num]=[c_dad[0],c_mom[0]]
#for l in open('Sort_Replace_new_sootv_bulls.tsv'):
for l in open('/5500disk/home/rusmari/Ilya/Rodstvo/Rodstvo_july/Sort_For_File_sootv_unite_'+date+'.tsv'):
	data=l.rstrip().split('\t')
	if data[2].isdigit()==False:
		di[data[0]]=data[3] + '\t' +data[4] + '\t' +data[5]
		golden_parents[prev_num]=[data[-2],data[-1]]

#with open('Sort_Replace_new_sootv_bulls_golden.tsv','w') as f:
#	with open('Check2.tsv','w') as check:
with open('/5500disk/home/rusmari/Ilya/Rodstvo/Rodstvo_july/File_sootv_unite_'+date+'.tsv','w') as f:
	#with open('Check2.tsv','w') as check:
		for l in open('/5500disk/home/rusmari/Ilya/Rodstvo/Rodstvo_july/Sort_For_File_sootv_unite_'+date+'.tsv'):
			data=l.rstrip().split('\t')
			f.write('\t'.join(data[:6])+'\t'+di[data[0]]+'\t'+'\t'.join(golden_parents[data[0]])+'\n')
			# if (data[-4]!=golden_parents[data[0]][0] and data[-4]!='None') or (data[-2]!=golden_parents[data[0]][1] and data[-2]!='None'):
			# 	check.write('\t'.join(data[:-4])+'\t'+golden_parents[data[0]][0]+'\t'+data[-4]+'\t'+golden_parents[data[0]][1]+'\t'+data[-2]+'\n')
		