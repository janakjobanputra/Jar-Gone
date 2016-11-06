import requests
import xml.etree.ElementTree as ET


# Find definitions for text
def get_definitions():
    annotations = []

    dictionary_api = "http://www.dictionaryapi.com/api/references/medical/v2/xml/"
    apikey = "?key=34d82344-06fc-4e6f-baf0-8e6811eb2f18"

    text_to_annotate = "blah melanoma test"
    words = text_to_annotate.split()
    print words

    # Annotate each word
    for word in words:
        print "** "+word+" **"
        r = requests.get(dictionary_api+word+apikey)
        print type(r)

        if r.status_code == 200:
            response = r.text
            # print response

            response_string = response.encode('utf-8')
            root = ET.fromstring(response_string);
            print root.tag
            print root.attrib

            # print root['entry_list']

            for child in root.findall('entry'):
                key = child.get('id')
                value = child.find('def/sensb/sens/dt').text
                print (key, value);

            # print root.find('entry_list/entry/def/sensb/sens/dt')




# Main
if __name__ == '__main__':
    get_definitions()
