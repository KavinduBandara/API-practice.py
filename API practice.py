import sys
import requests
import json
if len(sys.argv) != 2:
    sys.exit("Too few arguments")
response = requests.get("https://itunes.apple.com/search?entity=song&term=" + sys.argv[1])

needed_output = response.json()
for outs in needed_output["results"]:
    print(f"{outs["trackName"]} by {outs["artistName"]}")




