#v.	Выделить даты и вывести их в формате число-месяц-год
import natasha
from natasha import MorphVocab, DatesExtractor

morph_vocab = natasha.MorphVocab()
extractor = DatesExtractor(morph_vocab)

text = "Встреча должна была состояться 23 июня 2020 года"
matches = extractor(text)

for match in matches:
    print(match.fact.as_dict()['year']['year'], '-', match.fact.as_dict()['month']['value'], '-', match.fact.as_dict()['day'])
