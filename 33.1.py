import requests

sites = {
    "wikipedia":
        "https://www.wikipedia.org/rovots.txt",
    "twitter": "https://twitter.com/robots.txt",
}

for name, url in sites.items():
    response = requests.get(url)

    if response.status_code == 200:
        filename = f"{name}_robots.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(response.text)
            print(f"Saved {filename}")
    else:
        print(f"Failed to download robots.txt from {url}")

