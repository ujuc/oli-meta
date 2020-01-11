import crawler
import bs4


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
        assert isinstance(act, bs4.BeautifulSoup)
        assert act.html


def test_given_local_parameter_return_gas_station_data(self):
    pass
