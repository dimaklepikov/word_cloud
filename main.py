import os, sys
import wikipedia
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from stop_words import get_stop_words

wikipedia.set_lang('ru')
STOPWORDS_RU = get_stop_words('russian')

search_by = str(input('Введите слово/словосочетание: '))


try:
    wiki = wikipedia.page(search_by)
except wikipedia.exceptions.PageError:
    print('Слишком тредно собрать информацию, введите запрос точнее')
    # exit()
    os.execl(sys.executable, sys.executable, *sys.argv)


text = wiki.content

text = re.sub(r'==.*?==+', '', text)
text = text.replace('\n', '')


def plot_cloud(wordcloud):
    plt.figure(figsize=(40, 30))
    plt.imshow(wordcloud)
    plt.axis('off')


wordcloud = WordCloud(width=2000, 
                      height=1500, 
                      random_state=1, 
                      background_color='black', 
                      margin=20, 
                      colormap='Pastel1', 
                      collocations=False, 
                      stopwords=STOPWORDS_RU).generate(text)

if __name__ == '__main__':
    plot_cloud(wordcloud)
    wordcloud.to_file('your_wordcloud.png')
