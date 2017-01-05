import human_curl as requests
import json

MURL = "https://api.deckbrew.com/mtg/cards?name={}"

def main():

    with open("/home/tanger/dev/cubedraft/README.md", 'w') as outcubepage, open("/home/tanger/dev/cubedraft/failed_Cards.txt", 'w') as failed:
        with open("unixdraft", 'r') as incubepage:
            for line in incubepage:
                if not line: continue
                card = line.replace(',','').replace('\n','').replace('\r','')
                print card
                r = requests.get(MURL.format(card))
                results = json.loads(r.content)
                try:
                    url = results[0]['store_url']
                    outcubepage.write("<a href='%s'>%s</a><br />" % (url, line))
                except IndexError:
                    continue

if __name__ == '__main__':
    main()
