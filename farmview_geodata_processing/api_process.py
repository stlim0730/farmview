import requests, json, string
import dropbox, os
from geoprocess2 import merge_attachmentLinks, geojson_output

# run geoprocess and change the files downloaded from ONA into geojsons.
# data: ONA survey data files in json
def run_geoprocess(data):
    merge_attachmentLinks(data)
    with open('new_data_point.geojson', 'w') as fp:
        json.dump(geojson_output(data)[0], fp)
    with open('new_data_polygon.geojson', 'w') as fp:
        json.dump(geojson_output(data)[1], fp)

# Upload files to dropbox account and retrives urls
# *args: can be one or more file names to be uploaded to dropbox
def upload_dropbox(*args):
    client = dropbox.client.DropboxClient(os.environ.get('DROPBOX_AUTH_TOKEN'))
    urls = []
    for file_name in args:
        f = open(file_name, 'rb')
        response = client.put_file('farmview/'+file_name, f, overwrite=True)
        # Convert to shareable url showing parsable dropbox files on browser.
        share_link = string.replace(client.share('farmview/'+file_name, short_url=False)['url'], 'www.dropbox', 'dl.dropboxusercontent')
        urls.append(share_link)
    return urls

# Create new data set and save one or more import ids(needed for force sync later) and dropbox urls
# ona_id: takes ONA survey form id
def create_sync_table(ona_id):
    download_ona_data(ona_id)
    db_urls = upload_dropbox('new_data_point.geojson','new_data_polygon.geojson')
    dropbox_url = ''
    import_ids = ''
    for db_url in db_urls:
        file_url = 'https://calo1.cartodb.com/api/v1/synchronizations/?api_key=' + os.environ.get('CARTODB_API_KEY')
        header = {'Content-Type':'application/json'}
        res = json.loads((requests.post(file_url, json = {'url': db_url, 'interval':'36000'}, headers=header)).text)
        dropbox_url +=  db_url + ','
        import_ids += res['id'] + ','
    return import_ids, dropbox_url

# Use ONA survey data id (curr=63362) and download geoJSON files
# data_id: ONA survey data id
def download_ona_data(data_id):
    url = 'https://api.ona.io/api/v1/data/' + str(data_id)
    header = {'Authorization': 'Token ' + os.environ.get('ONA_AUTH_TOKEN')}
    run_geoprocess((requests.get(url, headers=header)).json())
