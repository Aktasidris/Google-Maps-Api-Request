'''
text search yap yerleri al
gelen json dosyasındean places idleri yer ayrıntıları apısı ile verielri al
gelen verileri filitrele mongo db ve excel dosyasına yazdır
bir istekte 20 sonuç döner daha fazla sonuç için next page token ile 20 değer daha alır
'''
import json
from detail_Search import get_place_details
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')
url="https://maps.googleapis.com/maps/api/place/textsearch/json"
text="elazığ,merkez,giyim"
from text_Search import text_Search
response = text_Search(text, api_key,url)

with open("google_maps_results.json", "w", encoding="utf-8") as json_file:
    json.dump(response, json_file, ensure_ascii=False, indent=4)
with open("google_maps_results.json","r", encoding="utf-8") as json_file:
    data=json.load(json_file)

detailed_results = []
# Her bir "id" için ayrıntılı bilgileri almak için döngü oluşturun
for entry in data:
    place_id = entry.get("place_id")
    if place_id:
        detailed_data = get_place_details(api_key, place_id)
        detailed_results.append(detailed_data)
# Ayrıntılı sonuçları JSON dosyasına yazma
with open("google_maps_detailed_results.json", "w", encoding="utf-8") as json_file:
    json.dump(detailed_results, json_file, ensure_ascii=False, indent=4)
print("Ayrıntılı sonuçlar JSON dosyasına yazıldı: google_maps_detailed_results.json")

