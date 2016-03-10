import json
from pprint import pprint

# variables:
data = None
col1 = 'Survey/ranch_address/Location_fromweb'
col2 = 'Survey/ranch_address/Location_GPS'
col3 = '_geolocation'
col4 = 'merged_column'
col5 = 'Survey/available_land_details/shape_available'

attachmentCol = '_attachments'
attachmentLinks = 'mergedAttachmentLinks'
download_url='download_url'

# function that prints out just the geometry columns:
def print_geometries(data):
	print '-'*160
	print '{:30} {:30} {:15} {:15} {:50}'.format('Location_GPS', 'Location_fromweb', 'lat', 'long', 'available_poly')
	print '-'*160
	for rec in data:
		print '{:30} {:30} {:15} {:15} {:50}'.format(
			rec.get(col2),
			rec.get(col1),
			str(rec.get(col3)[0]),
			str(rec.get(col3)[1]),
			rec.get(col5)
		)

# function that merges col1 and col2 together and 
# adds a new column to each entry of the dictionary:
def merge_geometries(data):
	for rec in data:
		# Simplest way: just use the "or" keyword to merge.
		# If you gave me more complex data, a few more steps might be necessary,
		# so it would be good to get a more complete data file for testing
		# purposes:
		rec[col4] = rec.get(col1) or rec.get(col2)

def merge_attachmentLinks(data):
	# new column for image, new column for sound
	for rec in data:
		count = 0
		rec['photoLink'] = ""
		rec['audioLink'] = ""
		
		# print("NEW REC")

		# processing attachments
		for attachment in rec['_attachments']:
			fullLink = "https://ona.io" + rec['_attachments'][count]['download_url']
			if (fullLink.endswith(".jpg") or fullLink.endswith(".png")):
				rec['photoLink'] = fullLink
				print "photo: ", rec['photoLink']
			else:
				rec['audioLink'] = fullLink
				print "audio: ", rec['audioLink']
			count+=1

		# # processing soil type
		# rec['Soil Type'] = ""
		# soilType = rec['soil_type']
		# if (soilType == ""):
		# 	rec['Soil Type'] = ""
		# elif (soilType == ""):
		# 	rec['Soil Type'] = ""
		# elif (soilType == ""):
		# 	rec['Soil Type'] = ""
		# elif (soilType == ""):
		# 	rec['Soil Type'] = ""

		# # processing 
		# rec['variable'] = ""
		# variable = rec['']
		# if (variable == ""):
		# 	rec['variable'] = ""
		# elif (variable == ""):
		# 	rec['variable'] = ""

# function that prints out all of the values in the dictionary (just useful to see):
def print_records(data):
	for rec in data:
		for key in rec.keys():
			try: print '{:70}: {}'.format(key[:68], rec[key][:80])
			except: pass


def geojson_output(data):
	features_point = []
	features_polygon = []
	for rec in data:
		if 'Survey/available_land_details/shape_available' in rec and rec['Survey/available_land_details/shape_available'] != None:
			block = {}
			block['type'] = 'Feature'
			shape = rec['Survey/available_land_details/shape_available']
			shape = shape.replace(';', ' ').split()
			coordinates = []
			for i in range(0, len(shape) / 4):
				coordinates.append([float(shape[4*i+1]), float(shape[4*i])])
			block['geometry'] = {'type' : 'Polygon', 'coordinates' : [coordinates]}
			block['properties'] = rec
			features_polygon.append(block)
		elif '_geolocation' in rec and rec['_geolocation'] != [None, None]:
			block = {}
			block['type'] = 'Feature'
			location = rec['_geolocation']
			block['geometry'] = {'type' : 'Point', 'coordinates' : [location[1], location[0]]}
			block['properties'] = rec
			features_point.append(block)
		else:
			pass
	json_point = {}
	json_polygon = {}
	json_point['type'] = 'FeatureCollection'
	json_polygon['type'] = 'FeatureCollection'
	json_point['features'] = features_point
	json_polygon['features'] = features_polygon
	return (json_point, json_polygon)

# ---------------
# start execution
# ---------------
if __name__ == "__main__":
	with open('Farmland_Monitoring_beta1-2015-10-16-18-45-46.json') as data_file:
		data = json.load(data_file)
		merge_attachmentLinks(data)
		# merge_geometries(data) 
		#print_records(data) #uncomment this to see all of the data
		#print_geometries(data)
		#geojson_output(data)
	
	#save out new file:
	with open('data_point.geojson', 'w') as fp:
		json.dump(geojson_output(data)[0], fp)
	with open('data_polygon.geojson', 'w') as fp:
		json.dump(geojson_output(data)[1], fp)
	