#!/usr/bin/python
import smtplib
import map_location
from pygeocoder import Geocoder
def email(parameter_list): 
	SMTP_SERVER = 'smtp.gmail.com'
	SMTP_PORT = 587
	lat = parameter_list[4]
	lon = parameter_list[5]
 	geoLocation = map_location.mapLocation(lat,lon)
 	location = str(geoLocation)
	sender = 'csl343reportingagency@gmail.com'
	recipient = parameter_list[3]
	subject = 'Emergency Report'
	link = "https://maps.google.co.in/?q="+lat+","+lon
	body = 'Respected Mam/Sir,\n\t\tThis is to imform you that car number : '+parameter_list[0]+' registered on the name of '+parameter_list[1]+' has met with an accident.\nThe approximate location is '+location+'.\n The Google Map link is: '+link+' \nThe required authorities havbn informed\n'

	#print body 
	body = "" + body + ""
	 
	headers = ["From: " + sender,
	           "Subject: " + subject,
	           "To: " + recipient,
	           "MIME-Version: 1.0",
	           "Content-Type: text/html"]
	headers = "\r\n".join(headers)
	 
	session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
	session.ehlo()
	session.starttls()
	session.ehlo
	session.login(sender, "kanaudsingh")
	 
	session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
	print "Done"
	return True
if __name__ == '__main__':
	parameter_list = ['PB12L3599','Prabhsharan','8146446458','arjunsunel0@gmail.com',30.962712,76.524895]
	email(parameter_list)    	
