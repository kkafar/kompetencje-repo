import requests

from bs4 import BeautifulSoup
from pathlib import Path
import polars


def bulldog_url_factory(year: int) -> str:
    return f"https://bulldogjob.com/it-report/{year}"


def main():
    raport_year = 2024
    bulldog_url = bulldog_url_factory(raport_year)
    cached_response_path = Path(f'cached_response_{raport_year}.html')

    if not cached_response_path.is_file():
        response = requests.get(bulldog_url)
        with open(cached_response_path, 'wb') as file:
            file.write(response.content)

        response_content = response.content
    else:
        response_bytes = None
        with open(cached_response_path, 'r') as file:
            response_bytes = file.read()

        if response_bytes is None:
            raise RuntimeError("Failed to read cached data. Remove the file and run again")

        response_content = response_bytes

    soup = BeautifulSoup(response_content, 'html.parser')




if __name__ == "__main__":
    main()
