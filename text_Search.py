import requests
def text_Search(query,apikey,url):
    params = {
        'query': query,
        'key': apikey,
    }
    results = []
    while True:
        response = requests.get(url, params=params)
        data = response.json()
        results.extend(data.get("results", []))
        next_page_token = data.get("next_page_token")
        if not next_page_token:
            break
        params["next_page_token"] = next_page_token

        params = {
            "next_page_token": next_page_token,
            "key": apikey
        }
    return results
