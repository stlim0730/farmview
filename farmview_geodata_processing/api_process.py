import requests, json, string
import dropbox, os
from geoprocess2 import merge_attachmentLinks, geojson_output
from .models import DataForm

# runs geoprocess and changes the files downloaded from ONA into geojsons.
def run_geoprocess(data):
    merge_attachmentLinks(data)
    with open('new_data_point.geojson', 'w') as fp:
        json.dump(geojson_output(data)[0], fp)
    with open('new_data_polygon.geojson', 'w') as fp:
        json.dump(geojson_output(data)[1], fp)

# Upload files to dropbox account and retrives urls
def upload_dropbox(*args):
    client = dropbox.client.DropboxClient(os.environ.get('DROPBOX_AUTH_TOKEN'))
    for file_name in args:
        f = open(file_name, 'rb')
        response = client.put_file('farmview/'+file_name, f, overwrite=True)
        # Convert to shareable url showing parsable dropbox files on browser.
        share_link = string.replace(client.share('farmview/'+file_name, short_url=False)['url'], 'www.dropbox', 'dl.dropboxusercontent')
        print 'uploaded: ', response
        print 'share link: ', share_link
        return share_link


# create new data set and save the returned id (=import_id needed for force_sync)
# curl -v -H "Content-Type: application/json" -d '{"url":"https://dl.dropboxusercontent.com/s/6ngyvp8hy78qh4z/new_data_point.geojson?dl=0", "interval":"36000"}' "https://calo1.cartodb.com/api/v1/synchronizations/?api_key=API_KEY"
# response = {"data_import":{"endpoint":"/api/v1/imports","item_queue_id":"120fd905-df10-49ba-99c6-20b2f515f169"},"id":"f874b4d4-4081-11e6-8c2a-0ecfd53eb7d3","name":null,"interval":36000,"url":"https://dl.dropboxusercontent.com/s/6ngyvp8hy78qh4z/new_data_point.geojson?dl=0","state":"created","user_id":"476e377b-b926-4595-9c71-1a73574ef706","created_at":"2016-07-02T18:22:44+00:00","updated_at":"2016-07-02T18:22:44+00:00","run_at":"2016-07-03T04:22:44+00:00","ran_at":"2016-07-02T18:22:44+00:00","modified_at":null,"etag":null,"checksum":"","log_id":null,"error_code":null,"error_message":null,"retried_times":0,"service_name":null,"service_item_id":null,"type_guessing":true,"quoted_fields_guessing":true,"content_guessing":false,"visualization_id":null,"from_external_source":false}
# Takes in
def create_sync_table(ona_id):
    download_ona_data(ona_id)
    # Create shared Dropbox URL
    db_url = upload_dropbox('new_data_point.geojson','new_data_polygon.geojson')
    url = 'https://calo1.cartodb.com/api/v1/synchronizations/?api_key=' + os.environ.get('CARTODB_API_KEY')
    header = {'Content-Type':'application/json'}
    res = requests.post(headers = header, data = {'url': file_url, 'interval':'36000'})
    form = FormData(import_id = res['id'], dropbox_url = db_url)
    form.save()

# calls sync_now. should have at least 15 min interval
# curl -v -X "PUT" "https://calo1.cartodb.com/api/v1/synchronizations/import_id/sync_now?api_key=API_KEY" -H "Content-Length:0"
def force_sync(import_id):
    url = 'https://calo1.cartodb.com/api/v1/synchronizations/' + import_id + '/sync_now?api_key=' + os.environ.get('CARTODB_API_KEY')
    header = {'Content-Length':0}
    requests.put(url, headers=header)

# using survey data 63362 and change the formats to geoJSON
def download_ona_data(data_id):
    url = 'https://api.ona.io/api/v1/data/'+data_id
    header = {'Authorization': 'Token ' + os.environ.get('ONA_AUTH_TOKEN')}
    run_geoprocess((requests.get(url, headers=header)).json())

form = FormData.objects.filter(ona_id = 63362)
# if form data is already present with the given Ona survey data, force sync. If not, create a new sync table
if form:
    force_sync(form.import_id)
else:
    create_sync_table(63362)
