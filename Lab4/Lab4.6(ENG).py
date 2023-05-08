#6. Средствами NLTK выделить именованные сущности с тэгами (Person, Organisation, GSP и проч.) для английского и русского текста

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

text = "Barack Obama was the 44th president of the United States of America. He was born in Honoluly, Hawaii in 1961"

tokens = nltk.word_tokenize(text)
pos_tags = nltk.pos_tag(tokens)
chunks = nltk.ne_chunk(pos_tags)

print(chunks)
