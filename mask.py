import urllib.request


def fetch_image(url: str):
    img = urllib.request.urlopen(url).read()
    out = open("media/mask.png", "wb")
    out.write(img)
    out.close
