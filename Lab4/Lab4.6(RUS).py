#6. Средствами NLTK выделить именованные сущности с тэгами (Person, Organisation, GSP и проч.) для английского и русского текста

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

text = "Санкт-Петербург - город на северо-западе Российской Федерации, расположенный на реке Нева."

tokens = word_tokenize(text)
pos_tags = nltk.pos_tag(tokens, lang='rus')
chunks = nltk.ne_chunk(pos_tags, binary=False)

print(chunks)
