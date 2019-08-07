import requests
from config import *

headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
}

login_url = 'https://passport.ustc.edu.cn/login?service=https://jw.ustc.edu.cn/ucas-sso/login'

data = {
    'model': 'uplogin.jsp',
    'service': 'https://jw.ustc.edu.cn/ucas-sso/login',
    'warn': '',
    'showCode': '',
    'username': STUDENT_ID,
    'password': PASSWORD,
    'button': '',
}


def login():
    session = requests.Session()
    html = session.post(login_url, headers=headers,
                        data=data, allow_redirects=False)
    session2 = requests.Session()
    session2.get(
        html.headers['location'], headers=headers, allow_redirects=False)
    return session2


if __name__ == "__main__":
    # 无报错即可
    login()
