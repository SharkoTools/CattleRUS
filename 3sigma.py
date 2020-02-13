import sys
import statistics as st

elements=[-6,-5,-4,-3,-2,-1]
# for elem in elements:
# 	hoz={}
# 	lakt={}
# 	m=[]
# 	for l in open('5DB_1-3lakt.tsv'):
# 		data=l.rstrip().split('\t')
# 		h=data[0][1:8]
# 		if data[elem]=='nan':
# 			data[elem]='None'
# 		if h not in hoz and data[elem]!='None':
# 			hoz[h]=[float(data[elem])]
# 		elif h in hoz and data[elem]!='None':
# 			hoz[h].append(float(data[elem]))

# 	sigma_hoz={}
# 	mean_hoz={}
# 	max_hoz={}
# 	min_hoz={}
# 	for l in hoz:
# 		try:
# 			max_hoz[l]=str(max(hoz[l]))
# 			min_hoz[l]=str(min(hoz[l]))
# 			mean_hoz[l]=str(st.mean(hoz[l]))
# 			sigma_hoz[l]=str(st.stdev(hoz[l]))
# 		except:
# 			print l
# 	with open('Stat_'+str(elem)+'tsv','w') as f:
# 		for l in hoz:
# 			f.write(l+'\t'+min_hoz[l]+'\t'+max_hoz[l]+'\t'+mean_hoz[l]+'\t'+sigma_hoz[l]+'\n')
for elem in elements:
	minim={}
	maxim={}
	for l in open('Stat_'+str(elem)+'.tsv'):
		data=l.rstrip().split('\t')
		minim[data[0]+str(elem)]=float(data[-2])-3*float(data[-1])
		maxim[data[0]+str(elem)]=float(data[-2])+3*float(data[-1])

with open('5DB_1-3lakt_3sigm.tsv','w') as f:
	for l in open('5DB_1-3lakt.tsv'):
		data=l.rstrip().split('\t')
		h=data[0][1:8]
		if data[-6]=='nan':
			data[-6]='None'
		for elem in elements:
			if data[elem]!='None':
				if h+str(elem) in minim:
					if float(data[elem])<minim[h+str(elem)] or float(data[elem])>maxim[h+str(elem)]:
						data[elem]='None'
		flag=0
		if data[-6]!='None':# and data[-5]!='None' and data[-4]!='None' and data[-3]!='None' and data[-2]!='None' and data[-1]!='None':
			flag=1
		if flag==1:
			f.write('\t'.join(data)+'\n')


