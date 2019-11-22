import json
import csv

with open('accoutnts.txt','r')as jfile:
	json_parsed=json.loads(jfile.read())
	# print(json_parsed)
	employ_data=open('./parse.csv','w')
	csvwriter=csv.writer(employ_data)
	count=0
	for emp in json_parsed:
		if count==0:
			header=emp.keys()
			csvwriter.writerow(header)
		count+=1
		csvwriter.writerow(emp.values())
	# employ_data.close()











# with open('accoutnts.json','r')as jfile:json_parsed=json.loads(jfile)
# employ_data=open('./parse.csv','w')
# csvwriter=csv.writer(employ_data)
# count=0
# for emp in json_parsed:if count==0:header=emp.keys()
# csvwriter.writerow(header)
# count+=1
# csvwriter.writerow(emp.values())
# employ_data.close()