import json
import re
import time
import requests
import tldextract
import execjs

with open("FunctionToSign.js", "r", encoding="utf-8") as f:
	js = execjs.compile(f.read())
def crwal(word):
    cookies = {
        'REALTIME_TRANS_SWITCH': '1',
        'FANYI_WORD_SWITCH': '1',
        'HISTORY_SWITCH': '1',
        'SOUND_SPD_SWITCH': '1',
        'SOUND_PREFER_SWITCH': '1',
        'BIDUPSID': 'BF3BA452F46A21D1C86A5D2651F67524',
        'PSTM': '1694960585',
        'APPGUIDE_10_6_6': '1',
        'APPGUIDE_10_6_7': '1',
        'APPGUIDE_10_6_9': '1',
        'BAIDUID': '8984CD3662EE810E97CE09A1EBCACE25:SL=0:NR=10:FG=1',
        'BAIDUID_BFESS': '8984CD3662EE810E97CE09A1EBCACE25:SL=0:NR=10:FG=1',
        'ZFY': '4rCPnQzlGmouqHNjndQcQ4onl:BGtprbd0MdWMdL:Babc:C',
        '__bid_n': '18a036b674813281467590',
        'BAIDU_WISE_UID': 'wapp_1703151022664_108',
        'BDUSS': 'B3RHpybFVXdEhxbXB-Z0ROVC1qMXJhamZvMExyWWU1d293Q2prMkp4Q3JVNjFsSVFBQUFBJCQAAAAAAAAAAAEAAAAfaNnpMTKwojg3MgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKvGhWWrxoVlMT',
        'BDUSS_BFESS': 'B3RHpybFVXdEhxbXB-Z0ROVC1qMXJhamZvMExyWWU1d293Q2prMkp4Q3JVNjFsSVFBQUFBJCQAAAAAAAAAAAEAAAAfaNnpMTKwojg3MgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKvGhWWrxoVlMT',
        'RT': 'z=1&dm=baidu.com&si=3c0d1995-d3c5-4273-afd2-7ee07b2008d5&ss=lqgwkhaw&sl=b&tt=8hc&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=6ox0&ul=6rxj&hd=6rxp',
        'H_PS_PSSID': '39839_39935_39936_39932_39946_39939_39996_39990_40042_40050_40033',
        'MCITY': '-340%3A',
        'Hm_lvt_64ecd82404c51e03dc91cb9e8c025574': '1703310372,1703342743,1703398222,1703519700',
        'Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574': '1703519819',
        'ab_sr': '1.0.1_NDE4ZGZkNWI3MWM1NGM2Yjg3MWQyMDM5NTZmODc2NjRiMWQzNTljZTYyMTZhMTM4ZmQ1ZjgyM2U5NWFlMDM2Yzg2MmQzNzFjZTdkODQ3YWE3Njc0YjRhOTExM2UxOTY3ZjQwMjY4YThlY2M4ZDM1NWU5Y2VmMzMyM2ZlYzVlYjJhYjhmZmNmZGY5ODQyNmQ5NTczZTlkZjAyZWM4MjkxZDZlZTE5ZmNhNWY1NGQyYzMxN2YyMDkwNDZhZjZkY2Uz',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Acs-Token': '1703476878072_1703520336148_phV3SSsvdmhPThJ/dei+RfrILjEHt3gZMZphYdHj02+B+QU1KHYeTycLhGgT+qXdZhMteVtDOTVzdW7B46NjljXOk+QRoOrc2JLLp1mqeyvl20dxlfpZAcUVb/Y8A1UYwJCBPi4PMed+zbT1vYT6QpDSI10C3Cdodt4q0A77QZ+IB2tb99MGoX+1fIiGuJG6aCvN+9M6c5bzWyNQRwjh45Pm+P7sNPY8GOIlngyd0pgWtUgyHY9aE4FcoqmBXBYZgglVTVGeUMBGx2/sb/Vt22m24AT0EyteAhWAjzYR6lvy0lPS9AHhp0Rpo6FJQzvsrkBBsLQdvQ/wwyxQNFmW0OxKkrfjNWrW2tWeCNlS3MBQA1Wl/sz6Aqp7u/0VufhfkVV8OEx+AuhKIN1MBASWTGLb37rPXXkTjymFb+fpteZdVR2z2dldmAosWBVgV4J+XPdlv++VMvaMTwB4/A7d4/dWQsOVbkaU3xSv5Z74NrKvNvZUXFyAIMFU+5UGwvVF',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://fanyi.baidu.com',
        'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = (
        ('from', 'en'),
        ('to', 'zh'),
    )

    data = {
        'from': 'en',
        'to': 'zh',
        'query': word,
        'transtype': 'realtime',
        'simple_means_flag': '3',
        'sign': js.call("b", word),
        'token': '00c35283641a58c80640036ead3d200e',
        'domain': 'common',
        'ts': '1703519823989'
    }

    response = requests.post('https://fanyi.baidu.com/v2transapi', headers=headers, params=params, cookies=cookies,
                             data=data)
    return response



