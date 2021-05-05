import urllib.request



def fetch_image(url: str):
    img = urllib.request.urlopen(url).read()
    out = open("media/mask.png", "wb")
    out.write(img)
    out.close


# fetch_image('https://verol.net/images/virtuemart/product/WS00017.png')
