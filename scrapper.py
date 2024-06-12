import requests
from bs4 import BeautifulSoup


class Scrapper:
    html_path = None

    def __init__(self):
        page = requests.get(self.html_path)
        self.soup = BeautifulSoup(page.content, "html.parser")

    def get_data(self):
        raise NotImplementedError


class Scrapper2023(Scrapper):
    html_path = "https://bulldogjob.com/it-report/2023"

    def _extract_barchart_data(self, key):
        data = {}
        results = self.soup.find(id=key)

        bars = results.find_all("div", class_="bar-wrapper")
        for bar in bars:
            title = bar.findNext("div", class_="label").text.replace("\n", "")
            value = bar.findNext("div", class_="value inside").text.replace("\n", "")

            data[title] = value

        return data

    @property
    def data(self):
        data = {}

        # pay per type
        current_key = "Earnings and experience"
        data["Earnings and experience"] = self._extract_barchart_data("general-earnings-and-experience_0")
        data["Earnings and specialization"] = self._extract_barchart_data("general-earnings-and-specialization_0")

        return data


result_data = Scrapper2023().data

for key, value in result_data.items():
    print(f"{key}:")
    for k, v in value.items():
        print(f"  {k}: {v}")

