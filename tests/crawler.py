import crawler
from bs4 import BeautifulSoup


class TestCase:
    def test_given_local_parameter_return_html_page(self):
        # Arrange
        sidogungu = {
            "sido": "서울특별시",
            "sigungu": "종로구",
        }

        # Act
        act = crawler.get_gas_station_html_data(sidogungu)

        # Assert
        assert isinstance(act, BeautifulSoup)
        table_data = act.select('td.rlist > a')
        assert table_data[0].text.split()[0] == '㈜지에스이앤알'


def test_given_local_parameter_return_gas_station_data(self):
    pass
