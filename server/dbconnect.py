import MySQLdb
def db(license_no,lat,lon):
	#print license_no
	lat=30.9740749
	lon=76.5367649
	db = MySQLdb.connect(host="localhost", user="root", passwd="arjun", db="csl343") 
	cur = db.cursor() 
	cur.execute("SELECT * FROM VehicleRegistration where Vehicle_No = '"+license_no+"'")
	parameter_list =[]
	for row in cur.fetchall() :
		parameter_list.append(row[0])
		parameter_list.append(row[1])
		parameter_list.append(row[2])
		parameter_list.append(row[3])
		parameter_list.append(str(lat))
		parameter_list.append(str(lon))
	#print parameter_list	
	return parameter_list		    
if __name__ == '__main__':
	db("MH01KA1007")    
