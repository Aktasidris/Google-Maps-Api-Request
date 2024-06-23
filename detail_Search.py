import requests
def get_place_details(api_key, place_id):
    base_url = "https://maps.googleapis.com/maps/api/place/details/json"
    params = {
        "place_id": place_id,
        "key": api_key,
        'fields': 'name,rating,international_phone_number,place_id,type,url,website,user_ratings_total',
    }
    response = requests.get(base_url, params=params)
    detailed_data = response.json()
    return detailed_data

'''
respons nesnesinden dönen cevaptan alınacak bilgiler

veriler(7 adet)
-"name":name
-"rating":
-"formatted_address":adress
-"international_phone_number":tel_no
-"photos":photos
-"place_id"

-"types":
-"url":maps_konumu
-"website":mekan_sitesi
-user_ratings_total":yorum_sayısı
'''