import requests

def get_peport_info(시작일, 기업코드):
    api_key = "a61de3bdebbc6a830abdeea61a407717e958072a"
    url = f"https://opendart.fss.or.kr/api/list.json"

    params = {
        "crtfc_key": api_key,
        "corp_code": 기업코드,
        "pblntf_ty": "A",
        "bgn_de": 시작일,
        "corp_cls": "Y",
        "page_no":1,
        "page_count":10
    }

    resp = requests.get(url, params=params)
    data = resp.json()

    for item in data['list']:
        print(item['corp_name'], item['report_nm'])

get_peport_info("20000101", "00164779")


