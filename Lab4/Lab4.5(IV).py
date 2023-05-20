#iv.	Нормализовать именованные сущности в тексте
from natasha import Doc, MorphVocab

morph_vocab = MorphVocab()

text = """ В 1001 году правитель Венгрии Иштван Святой принял титул короля, было провозглашено тем самым Королевство Венгрия. 
До 1301 года в Венгрии правила династия Арпадов, причём в тот период Венгерское королевство и имело отношения с Византийской империей, и раздиралось от конфликтов между представителями своей династии, и воевало с русскими князьями, и пережило монгольское нашествие. 
Затем престол Венгрии вначале оказался в руках правителей Богемского королевства из династии Пржемысловичей, а затем попал в руки баварских Виттельсбахов и представителей Анжу — Сицилийского и Люксембургского домов. 
В 1438 году герцог Австрии Альбрехт II из династии Габсбургов стал королём Венгрии, но вскоре Венгерское королевство попало в руки короля Польши Владислава III Варненчика из династии Ягеллонов. 
Последний погибает во время войны с турками-османами, и венгерским королём становится Ладислав Постум из Альбертинской линии династии Габсбургов. 
Однако в 1458 году во главе Венгерского королевства встаёт трансильванский магнат Матьяш Хуньяди, причём время его правления принято считать временем последнего возвышения независимого Венгерского королевства. 
В 1490 году на венгерском престоле окончательно утверждаются Ягеллоны, однако их власть в Венгрии завершается во время европейских походов султана Османской империи Сулеймана Кануни.'''"""

doc = Doc(text)
doc.segment(segmenter)
doc.tag_morph(morph_vocab)

entities = list(doc.spans)
for entity in entities:
    entity.normalize(morph_vocab)
    text = text[:entity.start] + entity.normal + text[entity.stop:]

print(text)