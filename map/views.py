from django.shortcuts import render
from reportlab.pdfgen import canvas
from reportlab.pdfgen import textobject
from django.http import HttpResponse
from django.http import JsonResponse
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import simplejson as json
from .models import Config
from .models import Datafield
import requests
import os
import logging



def map(request):
    configObj = Config.objects.order_by('-pub_date')[0]
    vizjson = urllib2.urlopen(configObj.vizjson_url).read()
    config = {
        'vizjson_url': configObj.vizjson_url,
        'vizjson': vizjson,
        'pub_date': str(configObj.pub_date),
        'optional_note': configObj.optional_note
    }
    datafield_data = list(Datafield.objects.all())
    datafields = []
    for query_field in datafield_data:
        if not query_field.enabled:
            continue
        datafield_id = str(query_field.datafield_id)
        datafield_type = str(query_field.datafield_type)
        datafield_name = str(query_field.datafield_name).strip()
        datafield_label_eng = str(query_field.datafield_label_eng)
        # datafield_label_esp = unicode(query_field.datafield_label_esp)
        # str(query_field.data_sources).replace('\n', ',').replace('\r', '')
        data_sources = str(
            query_field.data_sources).replace(
            '\r', '').split('\n')
        query_choices_vals = str(query_field.query_choices_vals).split(
            '\n')  # .replace('\n', ',').replace('\r', '') # name in XLS Form
        query_choices_labels_eng = str(query_field.query_choices_labels_eng).split(
            '\n')  # .replace('\n', ',').replace('\r', '') # label_english in XLS Form
        # query_choices_labels_esp =
        # unicode(query_field.query_choices_labels_esp).split('\n')#.replace('\n',
        # ',').replace('\r', '') # label_espanol in XLS Form
        query_choices = []
        if len(query_choices_vals) == len(query_choices_labels_eng):
            for i in range(len(query_choices_vals)):
                choice_obj = {
                    'val': query_choices_vals[i].strip().replace('\r', ''),
                    'label_eng': query_choices_labels_eng[i].replace('\r', '')
                }
                # if len(query_choices_labels_esp) >= i + 1:
                #   choice_obj['label_esp'] = query_choices_labels_esp[i]
                query_choices.append(choice_obj)
        use_for_query_ui = query_field.use_for_query_ui
        use_for_detail_popup = query_field.use_for_detail_popup
        datafield_obj = {
            'id': datafield_id,
            'type': datafield_type,
            'name': datafield_name,
            'label_eng': datafield_label_eng,
            # 'label_esp': datafield_label_esp,
            # this is object type representation of data_sources for detailed
            # page
            'data_sources': data_sources,
            # this is stringified representation of data_sources for query ui
            'data_sources_str': json.dumps(data_sources),
            # this is object type representation of choices for query ui
            'choices': query_choices,
            # this is stringified representation of choices for human readable
            # values on detailed page
            # separators=(',', ':'), sort_keys=True),
            'choices_str': json.dumps(query_choices),
            'use_for_query_ui': use_for_query_ui,
            'use_for_detail_popup': use_for_detail_popup
        }
        datafields.append(datafield_obj)
    context = {
        'config_json': json.dumps(config),
        'datafields': datafields,
        'data_sources': ['central_coast_joined', 'data_point', 'data_polygon']
    }
    return render(request, 'map/map.html', context)


def geocode(request, location_query):
    CARTODB_API_KEY = os.environ.get('CARTODB_API_KEY')
    carto_geocoding_url_template = 'https://calo1.carto.com/api/v2/sql?q=SELECT%20cdb_geocode_street_point(\'{}\')&api_key={}'
    request_url = carto_geocoding_url_template.format(
        location_query, CARTODB_API_KEY)
    geocoding_api_response = requests.get(request_url)
    return JsonResponse(geocoding_api_response.json())

def gen_pdf(request, id, table):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="somefilename.pdf"'
    # Create the PDF object, using the response object as its "file."
    c = canvas.Canvas(response)

    CARTODB_API_KEY = os.environ.get('CARTODB_API_KEY')
    carto_api_request = 'https://calo1.carto.com/api/v2/sql?q=SELECT * FROM '+str(table)+' where cartodb_id = ' + str(id) +'&api_key=' + str(CARTODB_API_KEY)
    carto_api_response = requests.get(carto_api_request)  

    contents = carto_api_response.content
    stuff = json.loads(contents)  
    rows = stuff['rows'][0]
#     for k,v in rows.items():
# #     if v is not None:
#         print(k,': '+ str(v))
    # logger = logging.getLogger(__name__)
    # logger.debug(str(JsonResponse(carto_api_response.json())))
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    c.setFontSize(size= 24)
    c.drawString(210, 800, "Parcel Information")
    c.setFont('Helvetica', 12)
    # c.drawString(70, 775 - 15, 'cartodb_id' + ': ' + str(rows.items()[0][1]))
    response_data = rows.items()
    nextPage = False
    startOfPageIndex = 0
    for i in range(0, len(response_data)):
        if not nextPage:
            if startOfPageIndex:
                c.drawString(50, 830 - (13 * (i - startOfPageIndex) ), str(response_data[i][0]) + ': ' + str(response_data[i][1]))    
            else:
                c.drawString(50, 775 - (13 * (i - startOfPageIndex) ), str(response_data[i][0]) + ': ' + str(response_data[i][1]))
        if (775 - (13 * (i - startOfPageIndex))) < 10:
            c.showPage()
            startOfPageIndex = i - 1
            
        # factor += factor
    # c.drawString(70, 775 - 15, str(factor))
    # c.drawString(70, 775 - 30, str(len(response_data)))

    # Close the PDF object cleanly, and we're done.
    c.showPage()
    c.save()
    return response
