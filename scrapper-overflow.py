from scrapper import *


class ScrapperOverflow(ScrapperBulldog):
    USD_TO_PLN = 0

    def _extract_barchart_data(self, website_key, website_text):
        results = self.soup.find(id=website_key)

        bars = results.find_all("tr")
        for bar in bars:
            title = bar.findNext("td", class_="label").text.strip()
            if title == website_text:
                value_str = bar.findNext("span", class_="js-bar-unit").text.strip()
                return int("".join([c for c in value_str if c.isdigit()]))

    @property
    def data(self):
        data = super().data

        earnings_refactored = {}
        for key, value in data["Earnings and specialization"].items():
            earnings_refactored[key] = round(value / 12 * self.USD_TO_PLN)
        data["Earnings and specialization"] = earnings_refactored

        return data
