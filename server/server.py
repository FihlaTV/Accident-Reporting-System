import socket
import os
import emailtest
import image
import dbconnect
from subprocess import call
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("", 5000))
server_socket.listen(5)
while (1):
	client_socket, address = server_socket.accept()
	fileName = client_socket.recv(1024)
	#print fileName
	finalFileName = ""
	for i in range(0,len(fileName)):
	        if fileName[i] == '.':
	                if fileName[i+1] =='j' and fileName[i+2] == 'p' and fileName[i+3] == 'g':
	                        finalFileName +=".jpg"
	                        break
	                else:
	                        finalFileName += fileName[i]
	        elif fileName[i] == '\0':
	                continue
	        	               
	        elif fileName[i]=="_" or fileName[i].isdigit() or fileName[i].isalpha():
	                finalFileName += fileName[i]
	tag=0	          
	fileName=""      
	for i in range(0, len(finalFileName)):
		if tag==0:
			if finalFileName[i]=='.':
				tag=1
			else:
				fileName+=finalFileName[i]
		elif tag==1:
			fileName+=finalFileName[i]
	lat = ""
	lon = ""
	tag=0
	tag1=0
	for i in range(0, len(fileName)):
		if fileName[i]=='n':
			tag=1
		elif fileName[i]=='t':
			tag=2
		elif tag==2:
			if fileName[i] =='.' and tag1==1:
					break
			elif fileName[i].isalpha()==False:
				lat+=fileName[i]
				if fileName[i] =='.':
					tag1 =1 			
			else:
				tag=0		
		elif tag==1:
			if fileName[i].isalpha()==False:
				lon+=fileName[i]		
			else:
				tag=0
		 		
	#print lat,lon	 						                    	       
	#print "Name of the file is: ",fileName
	print "Recieving File..."
	fname = '../android/'+fileName
	fp = open(fname,'w')
	while True:
		strng = client_socket.recv(512)
		if not strng:
			break
		fp.write(strng)
	fp.close()
	print "Data Received successfully"
	array = image.IMG(fname)
	call(["tesseract",array[0],"../android/out_original"])
	call(["tesseract",array[1],"../android/out_grey"])
	call(["tesseract",array[2],"../android/out_black_white"])

	string=""
	fo = open("../android/out_black_white.txt", "r+")
	In = fo.read().splitlines();
	fo.close()

	string_bw=""
	for i in In:
		if len(i)>5:
			string_bw = i
	fo = open("../android/out_original.txt", "r+")
	In = fo.read().splitlines();
	fo.close()
	string_o=""
	for i in In:
		if len(i)>5:
			string_o = i		
	#print string,len(string)

	if len(string_bw)>len(string_o):
		string =string_bw.replace(" ", "")
	else:
		string =string_o.replace(" ", "")	
	print string	
	print len(string)
	
	parameter_list = dbconnect.db(string,lat,lon)
	print parameter_list
	ans = emailtest.email(parameter_list)		
	if not ans:
		print "Failed"
