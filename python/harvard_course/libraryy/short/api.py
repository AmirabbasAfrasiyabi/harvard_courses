import requests

def main():
    artist = input()
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search",
            {"q" :input}
            
            )
        response.raise_for_status()

    except requests.HTTPError:
        print('could not complete request')
        return
    
    content = response.json()
    for artwork in content["data"]:
        print(f"* {artwork['title']}")

main()