from yargy import rule, or_, and_, not_
from yargy.interpretation import fact
from yargy.pipelines import morph_pipeline
from yargy.predicates import gram, type

from name import FULL_NAME

Person = fact(
    'Person',
    ['position', 'description', 'name']
)

# Любое слово русского языка
ANY_RU_WORD = type('RU')

''' Специальность '''
POSITION = morph_pipeline(['инженер', 'профессор', 'скульптор', 'художник', 'руководитель', 'архитектор'])

''' Описание (специальности) '''
# Описание - некоторое опциональное дополнение к специальности
# Например: руководитель [Московских городских железных дорог])
# Правило описывает любой набор идущих подряд слов русского языка (не более 5),
# не включающих глаголы, предлоги и союзы
DESCRIPTION = rule(
    and_(
        ANY_RU_WORD,
        not_(
            or_(
                gram('VERB'),
                gram('PREP'),
                gram('CONJ'),
            ),
        ),
    )
).repeatable(max=5).optional()

''' Персона '''
# Включает в себя специальность + описание (опционально) + полное имя
PERSON = rule(
    POSITION.interpretation(Person.position.inflected()),
    DESCRIPTION.interpretation(Person.description),
    FULL_NAME.interpretation(Person.name)
).interpretation(Person)
