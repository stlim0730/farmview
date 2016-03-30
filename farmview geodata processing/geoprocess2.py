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
        # processing attachments
        for attachment in rec['_attachments']:
            fullLink = "https://ona.io" + rec['_attachments'][count]['download_url']
            if (fullLink.endswith(".jpg") or fullLink.endswith(".png")):
                rec['photoLink'] = fullLink
                # print "photo: ", rec['photoLink']
            else:
                rec['audioLink'] = fullLink
                # print "audio: ", rec['audioLink']

        renameField(rec, 'survey_available_land_details_acres_avail', 'Acres available')
        renameField(rec, 'survey_available_land_details_ageasment', 'Agricultural easement status')
        renameField(rec, 'survey_available_land_details_equipment_available', 'Equipment available')
        renameField(rec, 'survey_available_land_details_equipment_type', 'Equipment type')
        renameField(rec, 'survey_available_land_details_lease_rate_expected', 'Expected lease rate ($/acre)')
        renameField(rec, 'survey_available_land_details_livestock_allowed', 'Livestock allowed')
        renameField(rec, 'survey_available_land_details_property_description2', 'Property description')
        renameField(rec, 'survey_available_land_details_shape_available', 'Geometry of available land')
        renameField(rec, 'survey_available_land_details_tenure_arrangement_offered', 'Lease offered')
        renameField(rec, 'survey_contacts_contact_name', 'Contact name')
        renameField(rec, 'survey_farmer_details_commute_time_current', 'Commute time')
        renameField(rec, 'survey_farmer_details_desiredacreage', 'Acres desired')
        renameField(rec, 'survey_farmer_details_foundproperty', 'How property was identified')
        renameField(rec, 'survey_farmer_details_lease_current_op', 'Current lease type')
        renameField(rec, 'survey_farmer_details_loan_needed', 'Loan need')
        renameField(rec, 'survey_farmer_details_org_specify', 'Organization names')
        renameField(rec, 'survey_farmer_details_orgs', 'Organizations')
        renameField(rec, 'survey_farmer_details_yearsfarming', 'Years farming')
        renameField(rec, 'survey_land_availability', 'Land availability')

        renameField(rec, 'Survey/ranch_address/land_county', 'County')
        # REQUIRES ONE OR THE OTHER
        # renameField(rec, 'survey_ranch_address_location_gps', 'Location')
        # renameField(rec, 'Survey/ranch_address/Location_fromweb', 'Location')
        renameField(rec, 'survey_ranch_address_city', 'City')
        renameField(rec, 'survey_ranch_address_number', 'Number')
        renameField(rec, 'survey_ranch_address_ranch_name', 'Ranch name')
        renameField(rec, 'survey_ranch_address_street', 'Street')
        renameField(rec, 'survey_ranch_address_zip', 'ZIP')

        renameField(rec, 'Survey/ranch_details/desc_general', 'General description')
        renameField(rec, 'Survey/ranch_details/fallowtime', 'Time fallow')
        renameField(rec, 'Survey/ranch_details/farm_size', 'Farm size (acres)')
        renameField(rec, 'Survey/ranch_details/farming_practices', 'Farming Practices')
        renameField(rec, 'Survey/ranch_details/fence_status', 'Fence Status')
        renameField(rec, 'Survey/ranch_details/infrastructure', 'Existing Infrastructure')
        renameField(rec, 'Survey/ranch_details/infrastructure_other', 'Other infrastructure')
        renameField(rec, 'Survey/ranch_details/land_owner_lives_where', 'Land Owner Location')
        renameField(rec, 'Survey/ranch_details/current', 'Current lease rate ($/acre)')
        renameField(rec, 'Survey/ranch_details/neighboringfarm', 'Neighboring farm type')
        renameField(rec, 'Survey/ranch_details/neighbors', 'Neighboring land')
        renameField(rec, 'Survey/ranch_details/parcelid', 'APN or parcel ID')
        # renameField(rec, 'Survey/ranch_details/', '')
        # renameField(rec, 'Survey/ranch_details/', '')
        # rec['Photo filename'] = rec['Survey/ranch_details/photo1'] #NULL CASE
        # rec['Photo filename'] = rec['Survey/ranch_details/photo2'] #NULL CASE
        renameField(rec, 'Survey/ranch_details/previousfarming', 'Previous farming activity')
        renameField(rec, 'Survey/ranch_details/previousfarming_other', 'Other previous farming')
        renameField(rec, 'Survey/ranch_details/soil_type', 'Soil type (general)')
        renameField(rec, 'Survey/ranch_details/soil_qual_audio', 'Soil description (audio)')
        renameField(rec, 'Survey/ranch_details/soil_qual_text', 'Soil description')
        renameField(rec, 'Survey/ranch_details/WaterDetails/irrigation_permit', 'Irrigation permit status')
        renameField(rec, 'Survey/ranch_details/WaterDetails/mainline_diam', 'Mainline diameter (inches)')
        renameField(rec, 'Survey/ranch_details/WaterDetails/irrigation_permit', 'Irrigation permit status')
        renameField(rec, 'Survey/ranch_details/WaterDetails/mainline_diam', 'Mainline diameter (inches)')
        renameField(rec, 'Survey/ranch_details/WaterDetails/water_infrastructure', 'Water infrastructure')
        renameField(rec, 'Survey/ranch_details/WaterDetails/water_investment', 'Water investment')
        renameField(rec, 'Survey/ranch_details/WaterDetails/water_payment', 'Water payment type')
        renameField(rec, 'Survey/ranch_details/WaterDetails/water_source', 'Water source')
        renameField(rec, 'Survey/ranch_details/WaterDetails/water_volume', 'Water volume (gallons per minute)')
        renameField(rec, 'Survey/ranch_details/WaterDetails/well_access', 'Well access')
        renameField(rec, 'Survey/ranch_details/WaterDetails/well_depth', 'Well depth (feet)')       
        renameField(rec, 'Survey/ranch_details/weed_mgmt', 'Weed management practices')
        renameField(rec, 'Survey/ranch_details/winter_potential', 'Growing season (months)')

        #REQUIRES SOME SORT OF ERROR CHECKING 
        renameField(rec, 'survey_rapid_survey_desc_short', 'Land description')
        renameField(rec, 'survey_rapid_survey_farm_size_short', 'Farm size (acres)')
        renameField(rec, 'survey_rapid_survey_land_status_short', 'Availability status')
        renameField(rec, 'survey_rapid_survey_lease_rate_short', 'Lease rate offered ($/acre)')     
        renameField(rec, 'survey_rapid_survey_location_fromweb_short', 'Location')
        renameField(rec, 'survey_rapid_survey_location_gps_short', 'Location')
        renameField(rec, 'survey_rapid_survey_water_short', 'Water source')


        renameField(rec, 'survey_session_desc', 'Data entry type')
        
        #Renaming values
        
        oldLivestock = ['cows', 'chickens', 'goats', 'sheep', 'any', 'none']
        newLivestock = ['Cows', 'Chickens', 'Goats', 'Sheep', 'Any of the above', 'None']
        renameValues(rec, 'Livestock allowed', oldLivestock, newLivestock)
        
        oldArrangements = ['short_term', 'long_term', 'crop_share', 'partnership', 'worktoown', 'farmmanage']
        newArrangements = ['Short term lease', 'Long term lease', 'Crop Share', 'Partnership', 'Work to own', 'Farm manage']
        renameValues(rec, 'Lease offered', oldArrangements, newArrangements)

        oldAvailability = ['whole_farm_available', 'part_of_farm_available', 'no_land_availalble']
        newAvailability = ['The whole property is available', 'Part of the property is available', "The property isn't available"]
        renameValues(rec, 'Land availability', oldAvailability, newAvailability)

        oldCounty = ['monterey', 'santa_cruz', 'san_benito']
        newCounty = ['Monterey', 'Santa Cruz', 'San Benito']
        renameValues(rec, 'County', oldCounty, newCounty)
        
        oldFallowTime = ['1', '2', '3']
        newFallowTime = ['Less than 1 year', '1 to 3 years', 'Greater than 3 years']
        renameValues(rec, 'Time fallow', oldFallowTime, newFallowTime)

        oldPractices = ['organic', 'conventional', 'nospray', 'mixed', 'transitioning', 'livestock_only', 'fallow', 'livestock_and_crops']
        newPractices = ['Certified Organic', 'Conventional', 'Organic, but without certification', 'Some organic, some conventional', 'Transitioning to organic', 'Just livestock', 'Fallow', 'Some livestock, some crops']
        renameValues(rec, 'Farming Practices', oldPractices, newPractices)

        oldInfrastructure = ['housing','greenhouse','garage','barn','cooler']
        newInfrastructure = ['Housing','Greenhouse','Garage','Barn','Cooler']
        renameValues(rec, 'Existing Infrastructure', oldInfrastructure, newInfrastructure)

        oldOwner = ['lives_on_property', 'lives_elsewhere', 'unknown']
        newOwner = ['The land owner lives on this property', 'The land owner lives somewhere else', 'Unknown']
        renameValues(rec, 'Land Owner Location', oldOwner, newOwner)

        oldNeigboringFarm = ['conventional', 'certified_organic', 'fallow', 'unknown']
        newNeigboringFarm = ['Conventional', 'Certified organic', 'Fallow', 'Not sure']
        renameValues(rec, 'Neighboring farm type', oldNeigboringFarm, newNeigboringFarm)

        oldNeigbors = ['farming', 'residential', 'commerical', 'public', 'habitat', 'unknown']
        newNeigbors = ['Farming', 'rRsidential', 'Commerical', 'Public', 'Habitat', 'Not sure']
        renameValues(rec, 'Neighboring land', oldNeigbors, newNeigbors)

        oldPrevFarming = ['rowcrops', 'strawberries', 'raspberries', 'tomatoes', 'potatoes', 'flowers', 'no_farming', 'unknown']
        newPrevFarming = ['Row crops, vegetables', 'Strawberries', 'Raspberries', 'Tomatoes', 'Potatoes', 'Flowers', 'No farming history', 'Unknown']
        renameValues(rec, 'Previous farming activity', oldPrevFarming, newPrevFarming)

        oldSoilType = ['sand', 'sandloam', 'loam', 'clayloam', 'clay']
        newSoilType = ['Very light (sand)', 'Somewhat light (sandy loam)', 'Medium (loam)', 'Somewhat heavy (clay loam)', 'Heavy (clay)']
        renameValues(rec,'Soil type (general)', oldSoilType, newSoilType)

        oldWaterInfrastructure = ['sprinklers', 'tape', 'mainline', 'investment_needed']
        newWaterInfrastructure = ['Sprinklers', 'Tape', 'Mainline', 'Infrastructure needed']
        renameValues(rec,'Water infrastructure', oldWaterInfrastructure, newWaterInfrastructure)
        
        oldWaterInvestment = ['Low', 'Medium', 'High']
        newWaterInvestment = ['Low Investment, infrastructure present ', 'Medium, some investment needed', 'High, lots of investment needed']
        renameValues(rec, 'Water investment', oldWaterInvestment, newWaterInvestment)

        oldWaterPayment = ['ownerpays', 'farmerpays', 'costshare']
        newWaterPayment = ['Owner pays', 'Farmer pays', 'Shared costs']
        renameValues(rec, 'Water payment type', oldWaterPayment, newWaterPayment)

        #SAME FOR SHORT OR LONG SURVEY --> ERROR CHECK EARLIER
        oldWaterSource = ['wellonsite', 'welloffsite', 'countywater', 'residential', 'unknown']
        newWaterSource = ['Well on site', 'Well off site', 'County water', 'Residential', 'Unknown']
        renameValues(rec, 'Water source', oldWaterSource, newWaterSource)

        oldWeedMgmt = ['clean_cult', 'summer_fallow', 'cover_cropping', 'invasives', 'unknown']
        newWeedMgmt = ['Clean cultivation', 'Dry summer fallow', 'Cover cropping', 'Invasive present', 'Unknown']
        renameValues(rec, 'Weed management practices', oldWeedMgmt, newWeedMgmt)

        oldLandStatus = ['forsale', 'forlease', 'vacant', 'unknown']
        newLandStatus = ['Farmland for sale', 'Farmland for lease', 'Unfarmed land, has potential', 'Not sure']
        renameValues(rec, 'Availability status', oldLandStatus, newLandStatus)

        oldSurveySessDesc = ['site_visit', 'land_listing', 'exisiting_ranch', 'available_parcel']
        newSurveySessDesc = ['Farmland site visit form', 'Detailed farmland listing', 'Description of an existing farm operation', 'Quickly record an available piece of farmland']
        renameValues(rec,'Data entry type', oldSurveySessDesc, newSurveySessDesc)


def renameField(arr, oldName, newName):
    if oldName in arr.keys():
        arr[newName] = arr[oldName]
    else:
        arr[newName] = ""

def renameValues(arr, field, oldVals, newVals):
    for old, new in map(None, oldVals, newVals):
        arr[field] = arr[field].replace(old, new)


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
    