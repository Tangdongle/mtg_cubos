from mtgsdk import Card
import requests

MAGIC_GET_BASE = "https://api.magicthegathering.io/v1/cards"

HTML_HEADER = '<!doctype html> <html lang="en"> <head> <meta charset="utf-8"> <title>Card F**K City</title> <meta name="description" content="Card F**K City"></head> <body>'

HTML_FOOTER = '</body> </html>'

def main():
    with open("/home/tanger/dev/cubedraft/README.md", 'w') as outcubepage, open("/home/tanger/dev/cubedraft/failed_Cards.txt", 'w') as failed:
        outcubepage.write(HTML_HEADER)
        with open("unixdraft", 'r') as incubepage:
            for line in incubepage:
                params = {"name": line}
                response = requests.get(
                        MAGIC_GET_BASE,
                        params=params
                        )
                status = response.status_code
                if status == 200:
                    print("Writing %s" % line)
                    outcubepage.write('<a href="%s">%s</a><br />' % (response.url, line))
                else:
                    params = {"names": line}
                    response = requests.get(
                            MAGIC_GET_BASE,
                            params=params
                            )
                    status = response.status_code
                    if status == 200:
                        print("Writing %s" % line)
                        outcubepage.write('<a href="%s">%s</a><br />' % (response.url, line))
                    else:
                        print("Failed %s" % line)
                        failed.write(line)
        outcubepage.write(HTML_FOOTER)

if __name__ == '__main__':
    main()
