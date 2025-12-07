import requests


class Brewery:
    def __init__(self, id: str, name: str, city: str, country: str, phone: str | None):
        self.id = id
        self.name = name
        self.city = city
        self.country = country
        self.phone = phone

    def __str__(self) -> str:
        return f"{self.name} | {self.city}, {self.country} | tel: {self.phone}"


url = "https://api.openbrewerydb.org/v1/breweries?per_page=20"
response = requests.get(url)
data = response.json()

breweries: list[Brewery] = [
    Brewery(
        id=item["id"],
        name=item["name"],
        city=item["city"],
        country=item["country"],
        phone=item.get("phone")
    )
    for item in data
]


for brewery in breweries:
    print(brewery)
