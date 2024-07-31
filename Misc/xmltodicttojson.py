'''
XMLからJSONに変換
'''

import xmltodict
import pprint
import json

DIR = "./XMLSample/" 
XML_PATH = "fuzokushoB_p.maiml"

# XMLファイルの処理
with open(DIR+XML_PATH, encoding='utf-8') as fp:
    # xml読み込み
    xml_data = fp.read()
 
    # xml → dict
    dict_data = xmltodict.parse(xml_data, process_namespaces=True)
    
    # print(dict_data)
    
    # dict型を整形して出力
    # pprint.pprint(dict_data)
    # print(pprint.pformat(dict_data))

    # dict → json
    pprint.pprint(json.dumps(dict_data))