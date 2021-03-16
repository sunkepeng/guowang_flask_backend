import json
import requests

headers = {'Content-Type': 'application/json'}
url = 'http://127.0.0.1:8000/contest'


def submit_state(contestant_id, checkout_num, fault_num):

    url_state = url + '/submit_state'
    state = {"contestantId": contestant_id,
             "checkoutNum": checkout_num,
             "faultNum": fault_num}

    state_json = json.dumps(state)
    current_state = requests.post(url=url_state, data=state_json, headers=headers)
    print(current_state.text)


def submit_result(contestant_id, is_end):
    url_result = url + '/submit_result'
    result_text = {"contestantId": contestant_id,
                   "isEnd": is_end,
                   "results": [{"id": "1",
                                "path": "D:/tmp/pic_anno/result/train/yw_gkxfw_23.jpg",
                                "type": "TaDiao",
                                "score": "1.0",
                                "xmin": "320",
                                "ymin": "771",
                                "xmax": "483",
                                "ymax": "928"},
                               {"id": "2",
                                "path": "D:/tmp/pic_anno/result/train/yw_gkxfw_24.jpg",
                                "type": "DiaoChe",
                                "score": "1.0",
                                "xmin": "447",
                                "ymin": "513",
                                "xmax": "582",
                                "ymax": "598"}]}
    result_json = json.dumps(result_text)
    current_result = requests.post(url=url_result, data=result_json, headers=headers)
    print(current_result.text)
