import csv
FObj=open('D:\通讯录\微电子系名单_寝室安排_通讯录.csv','rU')
csvReader=csv.reader(FObj)

for row in csvReader:
    print(row)

FObj.close()


import csv
readFileObj=open('D:\通讯录\微电子系名单_寝室安排_通讯录.csv','rU')
csvReader=csv.reader(readFileObj)
sheet=[]
for row in csvReader:
    sheet.append(row)
readFileObj.close()

sheet[3][3]='100.00'
theSum=0
for fieldStr in sheet[3][1:-1]:
    theSum+=float(fieldStr)
avg=theSum/3
sheet[3][4]='%.2f'%avg

writeFileObj=open('NewWorkbook1.csv','w')
writer=csv.writer(writeFieldObj)
for row in sheet:
    writer.writerow(row)
writeFileObj.close()
    
