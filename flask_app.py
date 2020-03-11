import generating as gen
import json
from flask import Flask, jsonify, request



app = Flask(__name__)

genre = "Pop"
artist = "Justin Bieber"
year = "2015"
album = "Purpose"
song_name = "Love Yourself"

context = "[s:genre]" + genre + "[e:genre]" + \
          "[s:artist]" + artist + "[e:artist]" + \
          "[s:year]" + year + "[e:year]" + \
          "[s:album]" + album + "[e:album]" + \
          "[s:song_name]" + song_name + "[e:song_name]" + \
          "[s:lyrics]"


@app.route('/get_lyrics', methods=["POST"])
def get_lyrics():
    if request.method == 'POST':
        r = json.loads(request.data)
        cond = ""
        if r["genre"] is not "":
            cond += "[s:genre]" + r["genre"] + "[e:genre]"

        if r["artist"] is not "":
            cond += "[s:artist]" + r["artist"] + "[e:artist]"

        if r["year"] is not "":
            cond += "[s:year]" + r["year"] + "[e:year]"

        if r["album"] is not "":
            cond += "[s:album]" + r["album"] + "[e:album]"

        if r["song_name"] is not "":
            cond += "[s:song_name]" + r["song_name"] + "[e:song_name]"

        cond += "[s:lyrics]"

        lyrics_list = gen.main(cond)
        return jsonify({"lyrics": lyrics_list[0]})

# # Simulates POST request
# with app.test_client() as c:
#     condtions = {
#         "genre": "Pop",
#         "artist": "Justin Bieber",
#         "year": "",
#         "album": "",
#         "song_name": ""
#     }
#
#     rv = c.post("http://127.0.0.1:5000/get_lyrics", data=json.dumps(condtions))

if __name__ == '__main__':
    app.run(host='0.0.0.0')

