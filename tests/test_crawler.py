from pathlib import Path

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
        gas_station_list = [''.join(x.text.split()) for x in table_data]
        assert gas_station_list is not []
        assert '자하문주유소' in gas_station_list
        assert '안풍주유소' in gas_station_list

    def test_given_expire_cookie_then_exception(self):
        # Arrange
        sidogungu = {
            "sido": "서울특별시",
            "sigungu": "종로구",
        }

        cookie = {
            "WMONID": "sxqrVZOZPPi",
            "JSESSIONID": "WiANyxNa0ZwnJTX1abBONM7Plye1aClC9PzsYA78DHYVTbv84a60uHXsGimaRJMl.opwas_1_servlet_engine1",
            "NetFunnel_ID": '',
        }

        # Act
        with pytest.raises(Exception) as excinfo:
            crawler.get_gas_station_html_data(sidogungu, cookie)

        # Assert
        assert "Failed!" in str(excinfo.value)

    def test_given_local_parameter_return_gas_station_data(self):
        # Arrange
        test_file = f"{Path(__file__).parent}/gas_station_table_data.txt"
        with open(test_file, "r") as f:
            table_html = f.read()

        soup = BeautifulSoup(table_html, 'html.parser')

        # Act
        act = crawler.get_gas_station_data(soup)

        # Assert
        assert isinstance(act, list)
        assert act[0]["brand"] == "현대오일뱅크"
        assert act[1]["name"] == "안풍주유소"
        assert act[2]["gasoline"] == 1648
        assert act[0]["diesel"] == 1458
