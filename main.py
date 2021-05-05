import os, sys
import wikipedia
import re
import numpy as np
from PIL import Image
from wordcloud import WordCloud
from mask import fetch_image
from word_cloud import plot_cloud
from stop_words import get_stop_words


search_by = str(input('Введите слово/словосочетание: '))
shape_image_url = str(input('Введите ссылку на картинку, в форме которой будет облако: '))

wikipedia.set_lang('ru')

try:
    wiki = wikipedia.page(search_by)
except wikipedia.exceptions.PageError:
    print('Слишком тредно собрать информацию, введите запрос точнее')
    os.execl(sys.executable, sys.executable, *sys.argv)

text = wiki.content
text = re.sub(r'==.*?==+', '', text)
text = text.replace('\n', '')


# def plot_cloud(wordcloud):
#     plt.figure(figsize=(40, 30))
#     plt.imshow(wordcloud)
#     plt.axis('off')



if __name__ == '__main__':
    fetch_image(shape_image_url)
    
    shape = np.array(Image.open('media/mask.png'))

    wordcloud = WordCloud(width=2000, 
                      height=1500, 
                      random_state=1, 
                      background_color='black', 
                      margin=20, 
                      colormap='Pastel1', 
                      collocations=False, 
                      stopwords=get_stop_words('russian'),
                      mask=shape).generate(text)

    plot_cloud(wordcloud)
    wordcloud.to_file('media/your_wordcloud.png')

    os.remove("media/mask.png")
    print("Готово! Картинка ждет Вас в папке 'media' ")
