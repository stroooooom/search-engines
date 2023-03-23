from yargy import rule, or_, and_, not_
from yargy.interpretation import fact
from yargy.predicates import gram, type, is_capitalized, Predicate


# Аббревиатура имени/отчества
class NameAbbr(Predicate):
    def __call__(self, token):
        return token.value[0].isupper() and len(token.value) == 1


FullName = fact(
    'FullName',
    ['first', 'last', 'middle']
)

ABBR = NameAbbr()

''' Правила для имени, фамилии, отчества '''
# Фамилия
LAST = is_capitalized().interpretation(FullName.last)

# Имя
FIRST = and_(
    gram('Name'),
    is_capitalized(),
    not_(ABBR)
).interpretation(FullName.first)
# Сокращенное имя
FIRST_ABBR = ABBR.interpretation(FullName.first)

# Отчество
MIDDLE = and_(
    gram('Patr'),
    is_capitalized(),
    not_(ABBR)
).interpretation(FullName.middle)

# Сокращенное отчество
MIDDLE_ABBR = ABBR.interpretation(FullName.middle)

''' Полное имя '''
# Имя-Фамилия (Василий Пупкин)
FIRST_LAST = rule(FIRST, LAST)
# Фамилия-Имя (Пупкин Василий)
LAST_FIRST = rule(LAST, FIRST)
# И-Фамилия (В. Пупкин)
ABBR_FIRST_LAST = rule(FIRST_ABBR, '.', LAST)

# Имя-Отчество-Фамилия (Василий Иванович Пупкин)
FIRST_MIDDLE_LAST = rule(FIRST, MIDDLE, LAST)
# Фамилия-Имя-Отчество (Пупкин Василий Иванович)
LAST_FIRST_MIDDLE = rule(LAST, FIRST, MIDDLE)
# И-О-Фамилия (В. П. Пупкин)
ABBR_FIRST_MIDDLE_LAST = rule(FIRST_ABBR, '.', MIDDLE_ABBR, '.', LAST)

FULL_NAME = or_(
    FIRST_LAST,
    LAST_FIRST,
    ABBR_FIRST_LAST,

    FIRST_MIDDLE_LAST,
    LAST_FIRST_MIDDLE,
    ABBR_FIRST_MIDDLE_LAST,
).interpretation(
    FullName
)
