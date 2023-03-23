from natasha import NamesExtractor, DatesExtractor, MorphVocab, AddrExtractor
from yargy import Parser

from metro_station import METRO_STATION
from name import FULL_NAME
from person import PERSON

text = open('src.txt').read()

morph_vocab = MorphVocab()

print('Готовые правила')
for Extractor in [NamesExtractor, DatesExtractor, AddrExtractor]:
    print('natasha.' + Extractor.__name__ + ':')
    extractor = Extractor(morph_vocab)
    matches = [match.fact for match in extractor(text)]
    for match in matches:
        print(match)

print('Новые правила')
for rule in [PERSON, FULL_NAME, METRO_STATION]:
    print('Правило' + rule.__name__ + ':')
    parser = Parser(rule)
    matches = [match.fact for match in parser.findall(text)]
    for match in matches:
        print(match)
