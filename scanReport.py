#python环境：3.5.2
import os
import sys
import re
#公共子目录
rootdir = "/Users/GaoSir/Desktop/virustotal/GENOME"
#定义一个空列表来存储所有子文件夹名称
dirlist = []
#获取所有子文件夹名称保存到dirlist中
def getFiles(path):
	files = os.listdir(path)
	for file in files:
		tempdir = rootdir+"/"+file
		if(os.path.isdir(tempdir)):#判断子路径是否有效
			dirlist.append(file)
	return dirlist
def getreport():
	for file in dirlist:
		reportdir = rootdir+"/"+file
		#print(reports)
		reports = os.listdir(reportdir)
		for report in reports:
			#print(report)
			scanReport(file,report)
def scanReport(file,filename):
	#filename = filename[-47:-7]
	if(filename[-3:]!="txt"):#不读取后缀为txt的文件，本例中读取的都是后缀为.report的文件
		tempdir = rootdir+"/"+file+"/"+filename
		f = open(tempdir,"r")
		lines = f.readlines()
		#line = f.readline()
		#print(line)
		num = 0	
		n = len(lines)
		#print(n)
		total = ''
		for line in lines:
			templine = line.lower()
			#print (line)
			if(templine.count(file.lower())):
				num+=1
			if (n==3):
				#print(line)
				total = line[20:22]
				#print(total)
			n-=1
		scan = file+": "+str(num)+"/"+total
		f.close()
		f = open(tempdir,"a+")
		f.write("\n"+scan)
		f.close()



dirlist = getFiles(rootdir)
getreport()