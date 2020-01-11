import pytest
from bs4 import BeautifulSoup

import crawler


class TestCase:
    def test_connect_main_get_cookie_data(self):
        # Act
        act = crawler.get_cookie_data()

        # Assert
        assert isinstance(act, dict)
        assert act.get("JSESSIONID") is not None
        assert act.get("WMONID") is not None

    def test_given_local_parameter_return_html_page(self):
        # Arrange
        sidogungu = {
            "sido": "서울특별시",
            "sigungu": "종로구",
        }

        cookie = crawler.get_cookie_data()

        # Act
        act = crawler.get_gas_station_html_data(sidogungu, cookie)

        # Assert
        assert isinstance(act, BeautifulSoup)
        table_data = act.select('td.rlist > a')
        assert table_data[0].text.split()[0] == '㈜지에스이앤알'

    def test_given_expire_cookie_then_exception(self):
        # Arrange
        sidogungu = {
            "sido": "서울특별시",
            "sigungu": "종로구",
        }

        cookie = {
            "WMONID": "sxqrVZOZPPi",
            "JSESSIONID": "WiANyxNa0ZwnJTX1abBONM7Plye1aClC9PzsYA78DHYVTbv84a60uHXsGimaRJMl.opwas_1_servlet_engine1",
            "NetFunnel_ID": ''
        }

        # Act
        with pytest.raises(Exception) as excinfo:
            crawler.get_gas_station_html_data(sidogungu, cookie)

        # Assert
        assert "Failed!" in str(excinfo.value)

    def test_given_local_parameter_return_gas_station_data(self):
        pass
