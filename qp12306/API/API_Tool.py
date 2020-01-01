from PyQt5.Qt import *
import requests


class API(object):

    # 验证码获取 URL
    GET_YZM_URL = "https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand"

    # 校验验证码 URL
    CHECK_YZM_URL = "https://kyfw.12306.cn/passport/captcha/captcha-check"

    # 登录验证 URL
    CHECK_ACCOUNT_PWD = "https://kyfw.12306.cn/passport/web/login"
    # username: Youngcs12306
    # password: yC1204112018
    # appid: otn


class APITool(QObject):
    session = requests.session()

    @classmethod
    def download_yzm(cls):
        response = cls.session.get(API.GET_YZM_URL)

        # print(response.content)
        with open("API/yzm.jpg", "wb") as f:
            f.write(response.content)
        # print(cls.session.cookies)

        return "API/yzm.jpg"

    @classmethod
    def check_yzm(cls, yzm):

        data_dict = {
            "answer": yzm,
            "login_site": "E",
            "rand": "sjrand"
        }
        response = cls.session.post(API.CHECK_YZM_URL, data=data_dict)
        dict = response.json()
        return dict["result_code"] == "4"

    @classmethod
    def check_account_pwd(cls, account, pwd):
        data_dict = {
            "username": account,
            "password": pwd,
            "appid": "otn"
        }
        response = cls.session.post(API.CHECK_ACCOUNT_PWD, data=data_dict)
        dict = response.json()
        # return dict["result_code"] == "4"

        print(dict)



if __name__ == "__main__":
    APITool.download_yzm()