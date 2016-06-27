import requests, json
import dropbox, os
from geoprocess2 import merge_attachmentLinks, geojson_output

# using survey data 63362
url = 'https://api.ona.io/api/v1/data/63362'
header = {'Authorization': 'Token '+os.environ.get('ONA_AUTH_TOKEN')}
res = (requests.get(url, headers=header)).json()

def run_geoprocess(data):
    merge_attachmentLinks(data)
    with open('api_data_point.geojson', 'w') as fp:
        json.dump(geojson_output(data)[0], fp)
    with open('api_data_polygon.geojson', 'w') as fp:
        json.dump(geojson_output(data)[1], fp)

def upload_dropbox(*args):
    client = dropbox.client.DropboxClient(os.environ.get('DROPBOX_AUTH_TOKEN'))
    print 'linked account: ', client.account_info()
    f = open('api_data_point.geojson', 'rb')
    response = client.put_file('farmview/api_data_point.geojson', f)
    print 'uploaded: ', response

run_geoprocess(res)
upload_dropbox()
