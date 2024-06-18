import requests
from bs4 import BeautifulSoup


class Scrapper:
    html_path = None

    def __init__(self):
        page = requests.get(self.html_path)
        self.soup = BeautifulSoup(page.content, "html.parser")

    @property
    def data(self):
        raise NotImplementedError


class ScrapperBulldog(Scrapper):
    barchart_keys = None

    def _extract_barchart_data(self, website_key, website_text):
        results = self.soup.find(id=website_key)

        bars = results.find_all("div", class_="bar-wrapper")
        for bar in bars:
            title = bar.findNext("div", class_="label").text.strip()
            if title == website_text:
                value_str = bar.findNext("div", class_="value").text.strip()
                return int("".join([c for c in value_str if c.isdigit()]))

    @property
    def data(self):
        data = {}
        for parameter_name, parameter_points in self.barchart_keys.items():
            parameter_data = {}
            for dict_key, website_id, website_text in parameter_points:
                parameter_data[dict_key] = self._extract_barchart_data(website_id, website_text)
            data[parameter_name] = parameter_data
        return data


class ScrapperBulldog2023(ScrapperBulldog):
    html_path = "https://bulldogjob.com/it-report/2023"
    barchart_keys = {
        "Earnings and experience": [
            ("Junior", "general-earnings-and-experience_0", "Junior"),
            ("Mid / Regular", "general-earnings-and-experience_0", "Mid / Regular"),
            ("Senior", "general-earnings-and-experience_0", "Senior"),
            ("Team Lead / Tech Lead", "general-earnings-and-experience_0", "Tech Lead / Team Lead")
        ],
        "Earnings and specialization": [
            ("Tester / QA", "general-earnings-and-specialization_0", "Developer, QA or test"),
        ]
    }


class ScrapperBulldog2022(ScrapperBulldog):
    html_path = "https://bulldogjob.com/it-report/2022"
    barchart_keys = {
        "Earnings and experience": [
            ("Junior", "general-salary-vs-experience_0", "Junior"),
            ("Mid / Regular", "general-salary-vs-experience_0", "Mid / regular"),
            ("Senior", "general-salary-vs-experience_0", "Senior"),
            ("Team Lead / Tech Lead", "general-salary-vs-experience_0", "Team Lead / Tech Lead")
        ]
    }


class ScrapperBulldog2021(ScrapperBulldog):
    html_path = "https://bulldogjob.com/it-report/2021"
    barchart_keys = {
        "Earnings and experience": [
            ("Junior", "salary-vs-experience_0", "Employment contract"),
            ("Mid / Regular", "salary-vs-experience_1", "Employment contract"),
            ("Senior", "salary-vs-experience_2", "Employment contract"),
            ("Team Lead / Tech Lead", "salary-vs-experience_3", "Employment contract")
        ],

    }

