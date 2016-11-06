import requests
import xml.etree.ElementTree as ET
import json


# Find definitions for text
def get_definitions(text_to_annotate):
    annotations = []
    annotation_dict = {}

    dictionary_api = "http://www.dictionaryapi.com/api/references/medical/v2/xml/"
    apikey = "?key=34d82344-06fc-4e6f-baf0-8e6811eb2f18"

    stop_words = ['the', 'a', 'as', 'at', 'no', 'in', 'are', 'to', 'for', 'but', 'also', 'index', 'with', 'nuclei']
    # text_to_annotate = "blah melanoma test"
    words = text_to_annotate.split()
    # print words

    # Annotate each word if not a stop word
    for word in words:
        # print "** "+word+" **"
        formatted_word = word.replace(",", "").replace(".", "") .lower()
        # print "** "+formatted_word+" **"

        if not formatted_word in stop_words:
            r = requests.get(dictionary_api+formatted_word+apikey)

            if r.status_code == 200:
                response = r.text
                # print response

                response_string = response.encode('utf-8')
                root = ET.fromstring(response_string);
                # print root.tag
                # print root.attrib

                for child in root.findall('entry'):
                    key = child.get('id')
                    value = child.find('def/sensb/sens/dt').text
                    # print (key, value)

                    annotation_dict[key] = value
                # print annotation_dict

    annotations.append(annotation_dict)
<<<<<<< Updated upstream
    # print json.dumps(annotations)

    return annotations
=======
<<<<<<< HEAD
    #print json.dumps(annotations)
=======
    # print json.dumps(annotations)

    return annotations
>>>>>>> origin/Website
>>>>>>> Stashed changes


# TEST - open file
def open_file():
    with open('/medical_consult.txt') as data_file:
        lines = data_file.read()
        # print "Lines: ", lines
        data_file.close()
        return lines

# Main
if __name__ == '__main__':
    text_to_annotate = open_file()
    print("hello")
    the_annotations = get_definitions(text_to_annotate)
    print("Here")
    with open('data.json', 'w') as fp :
        json.dump(the_annotations, fp)
    # print the_annotations

