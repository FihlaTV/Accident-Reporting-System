from pygeocoder import Geocoder
def mapLocation(lat,lon):
	results = Geocoder.reverse_geocode(float(lat),float(lon))
	#results = Geocoder.reverse_geocode(30.97548,76.53786)#iit ropar
	#results = Geocoder.reverse_geocode(30.76239,76.78031)#women's hostel
	#results = Geocoder.reverse_geocode(23.76239,76.98031)
	#print results[0]

	#print results[1]
	#print results[2]
	#print results
	return results

