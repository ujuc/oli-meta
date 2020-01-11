import httpx
from bs4 import BeautifulSoup


def get_cookie_data() -> dict:
    """
    Main 화면으로 접근하여 cookie 값을 가지고 온다.

    :return: cookie 정보를 반환한다.
    :rtype: dict
    """
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:72.0) "
                      "Gecko/20100101 Firefox/72.0",
        "accept": "text/html,application/xhtml+xml,application/xml;"
                  "q=0.9,image/webp,*/*;q=0.8",
        "content-type": "application/x-www-form-urlencoded",
    }

    main = httpx.get('http://www.opinet.co.kr/user/main/mainView.do',
                     headers=headers)

    raw_cookie = main.request.headers.get('cookie').split('; ')

    cookie = {}
    for cookie_data in raw_cookie:
        k, v = cookie_data.split('=')
        cookie[k] = v

    return cookie


def get_gas_station_html_data(sidogungu: dict, cookie: dict) -> BeautifulSoup:
    """
    HTML을 가져오자.

    :param sidogungu:
    :return:
    """
    send_data = (
        f"BTN_DIV=os_btn"
        f"&BTN_DIV_STR="
        f"&POLL_ALL=all"
        f"&SIDO_NM={sidogungu['sido']}"
        f"&SIGUNGU_NM={sidogungu['sigungu']}"
        f"&SIDO_CD=01"
        f"&SIGUN_CD=0101"
        f"&MAP_CENTER_X="
        f"&MAP_CENTER_Y="
        f"&MAP_ZOOM="
        f"&MAP_FIRST_X="
        f"&MAP_FIRST_Y="
        f"&LPG_YN="
        f"&SESSION_USER_ID="
        f"&SIDO_NM0={sidogungu['sido']}"
        f"&SIGUNGU_NM0={sidogungu['sigungu']}"
        f"&DONG_NM="
        f"&GIS_X_COOR="
        f"&GIS_Y_COOR="
        f"&GIS_X_COOR_S="
        f"&GIS_X_COOR_E="
        f"&GIS_Y_COOR_S="
        f"&GIS_Y_COOR_E="
        f"&SEARCH_MOD=addr"
        f"&OS_NM="
        f"&NORM_YN=on"
        f"&SELF_DIV_CD=on"
        f"&VLT_YN=on"
        f"&KPETRO_YN=on"
        f"&KPETRO_DP_YN=on"
        f"&POLL_DIV_CD=SKE"
        f"&POLL_DIV_CD=GSC"
        f"&POLL_DIV_CD=HDO"
        f"&POLL_DIV_CD=SOL"
        f"&POLL_DIV_CD=RTO"
        f"&POLL_DIV_CD=ETC"
    )

    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:72.0) "
                      "Gecko/20100101 Firefox/72.0",
        "accept": "text/html,application/xhtml+xml,application/xml;"
                  "q=0.9,image/webp,*/*;q=0.8",
        "content-type": "application/x-www-form-urlencoded",
    }

    response = httpx.post(
        "http://www.opinet.co.kr/searRgSelect.do",
        params=send_data, headers=headers, cookies=cookie
    )

    if 'smartPhones' in response.text:
        raise Exception("Failed! cookies change!!!")

    return BeautifulSoup(response.text, "html.parser")


def get_gas_station_data() -> list:
    """
    HTML에서 가져온 주유소 정보를 짜르자.

    :return:
    :rtype: list
    """
    pass
