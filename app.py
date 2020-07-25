from flask import Flask, request
import requests

app = Flask(__name__)

#https://www.youtube.com/watch?v=QjtW-wnXlUY

#https://scotch.io/bar-talk/processing-incoming-request-data-in-flask

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        critter = request.form['critter']
        critter = critter.replace(' ', '_')
        response = requests.get("http://acnhapi.com/v1/sea/" + critter)
        response2 = requests.get("https://en.wikipedia.org//w/api.php?action=query&format=json&list=search&srsearch=" + critter)
        data = response.json()
        name = (data['name']['name-EUen'])
        price = (data['price'])
        icon = (data['icon_uri'])
        image = (data['image_uri'])
        wikiData = response2.json()
        creatureInfoTitle = wikiData['query']['search'][1]['title']
        creatureInfoSnippet = wikiData['query']['search'][1]['snippet']
        return '''<body align=center>
            <h1>The creature is {}.</h1>
            <table style="width:50%" border=1 align=center>
            <tr>
            <th>Name</th>
            <th> {} </th>
            </tr>
            <tr align=center>         
            <td><b> Price: </b></td> 
            <td>{} bells</td>
            </tr>
            <tr align=center>
            <td><img src="{}"></img></td>
            <td><img src="{}"></img></td>
            </tr>
            <tr align=center>
            <td>Wikepedia results</td>
            <td>
            {}
            </br>
            {}
            </td>
            </tr>
            <tr align=center>
            <td>
            <p>Enter another sea creature:</p>
            </td>
            <td>
            <form method="POST" padding: 20px 20px>
            <p><input name="critter"/></p>
            <p><input type="submit" value="Find Sea Creature"/></p>
            </form>
            </td>
            </tr>
            </table>
            </body>
            '''.format(critter, name, price, icon, image, creatureInfoTitle, creatureInfoSnippet)
    return '''<table align="center">
            <tr align=center>
            <td>
            <p>Enter sea creature:</p>
            </td>
            <td>
            <form method="POST" padding: 20px 20px>
            <p><input name="critter"/></p>
            <p><input type="submit" value="Find Sea Creature"/></p>
            </form>
            </td>
            </tr>
            </table>
            '''


    
            



