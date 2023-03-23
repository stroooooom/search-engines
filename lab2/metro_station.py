from yargy import rule, or_, and_, not_
from yargy.interpretation import fact
from yargy.pipelines import morph_pipeline
from yargy.predicates import gram, type, is_capitalized, Predicate

ANY_RU_WORD = type('RU')

MetroStation = fact(
    'MetroStation',
    ['s', 'm', 'name']
)

STATION_ABBR = morph_pipeline(['ст']).interpretation(MetroStation.s)
STATION_FULL = morph_pipeline(['станция']).interpretation(MetroStation.s)
METRO = morph_pipeline(['метро']).interpretation(MetroStation.m)
KNOWN_NAME = morph_pipeline([
    'Авиамоторная',
    'Академическая',
    'Александровский сад',
    'Алексеевская',
    'Алтуфьево',
    'Аннино',
    'Арбатская',
    'Автозаводская',
    'Алма-Атинская',
    'Аэропорт',
    'Бабушкинская',
    'Багратионовская',
    'Баррикадная',
    'Бауманская',
    'Беговая',
    'Белорусская',
    'Беляево',
    'Бибирево',
    'Библиотека Ленина',
    'Битцевский парк',
    'Борисово',
    'Боровицкая',
    'Ботанический сад',
    'Братиславская',
    'Бульвар Дмитрия Донского',
    'Бульвар Рокоссовского',
    'Бульвар адмирала Ушакова',
    'Бунинская Аллея',
    'Бутырская',
    'ВДНХ',
    'Варшавская',
    'Верхние Лихоборы',
    'Владыкино',
    'Волгоградский проспект',
    'Волжская',
    'Волоколамская',
    'Воробьевы горы',
    'Водный стадион',
    'Войковская',
    'Выставочная',
    'Выхино',
    'Деловой центр',
    'Дмитровская',
    'Добрынинская',
    'Достоевская',
    'Дубровка',
    'Динамо',
    'Домодедовская',
    'Жулебино',
    'Зябликово',
    'Измайловская',
    'Калужская',
    'Кантемировская',
    'Каховская',
    'Каширская',
    'Киевская',
    'Киевская',
    'Китай-город',
    'Кожуховская',
    'Комсомольская',
    'Коньково',
    'Котельники',
    'Коломенская',
    'Краснопресненская',
    'Красносельская',
    'Красные ворота',
    'Крестьянская застава',
    'Кропоткинская',
    'Красногвардейская',
    'Крылатское',
    'Кузнецкий мост',
    'Кузьминки',
    'Кунцевская',
    'Курская',
    'Кутузовская',
    'Ленинский проспект',
    'Лермонтовский проспект',
    'Лесопарковая',
    'Лубянка',
    'Люблино',
    'Марксистская',
    'Марьина роща',
    'Марьино',
    'Медведково',
    'Международная',
    'Менделеевская',
    'Митино',
    'Молодежная',
    'Мякинино',
    'Нагатинская',
    'Нагорная',
    'Нахимовский Проспект',
    'Новогиреево',
    'Новокосино',
    'Новокузнецкая',
    'Новослободская',
    'Новоясеневская',
    'Новые Черёмушки',
    'Окружная',
    'Октябрьская',
    'Октябрьское Поле',
    'Орехово',
    'Отрадное',
    'Охотный ряд',
    'Павелецкая',
    'Парк Культуры',
    'Парк Победы',
    'Партизанская',
    'Первомайская',
    'Перово',
    'Петровско-Разумовская',
    'Печатники',
    'Пионерская',
    'Планерная',
    'Площадь Ильича',
    'Площадь Революции',
    'Полежаевская',
    'Полянка',
    'Пражская',
    'Преображенская площадь',
    'Пролетарская',
    'Проспект Вернадского',
    'Проспект Мира',
    'Профсоюзная',
    'Пушкинская',
    'Пятницкое шоссе',
    'Речной вокзал',
    'Рижская',
    'Римская',
    'Румянцево',
    'Рязанский проспект',
    'Савеловская',
    'Саларьево',
    'Свиблово',
    'Севастопольская',
    'Семеновская',
    'Селигерская',
    'Серпуховская',
    'Славянский бульвар',
    'Смоленская',
    'Сокол',
    'Сокольники',
    'Спартак',
    'Спортивная',
    'Сретенский бульвар',
    'Строгино',
    'Студенческая',
    'Сухаревская',
    'Сходненская',
    'Таганская',
    'Текстильщики',
    'Теплый стан',
    'Тверская',
    'Театральная',
    'Тимирязевская',
    'Третьяковская',
    'Тропарёво',
    'Трубная',
    'Тульская',
    'Тургеневская',
    'Тушинская',
    'Улица 1905 года',
    'Улица Горчакова',
    'Улица Скобелевская',
    'Улица Старокачаловская',
    'Улица академика Янгеля',
    'Университет',
    'Филевский парк',
    'Фили',
    'Царицыно',
    'Фонвизинская',
    'Фрунзенская',
    'Цветной бульвар',
    'Черкизовская',
    'Чертановская',
    'Чеховская',
    'Чистые пруды',
    'Чкаловская',
    'Шаболовская',
    'Шипиловская',
    'Шоссе Энтузиастов',
    'Щелковская',
    'Щукинская',
    'Электрозаводская',
    'Юго-Западная',
    'Южная',
    'Ясенево'
]).interpretation(MetroStation.name)
UNKNOWN_NAME = rule(
    and_(
        ANY_RU_WORD,
        or_(
            gram('NOUN'),
            gram('ADJF'),
            gram('NUMR'),
        ),
    )
).repeatable(min=1, max=4).interpretation(MetroStation.name)

QUOTE_LEFT = '«'
QUOTE_RIGHT = '»'
QUOTED_KNOWN_NAME = rule(QUOTE_LEFT, KNOWN_NAME, QUOTE_RIGHT)
QUOTED_UNKNOWN_NAME = rule(QUOTE_LEFT, UNKNOWN_NAME, QUOTE_RIGHT)
QUOTED_NAME = or_(QUOTED_KNOWN_NAME, QUOTED_UNKNOWN_NAME)

STATION = or_(
    STATION_FULL,
    STATION_ABBR,
    rule(STATION_ABBR, '.')
)
STATION_METRO_NAME = rule(STATION, METRO, QUOTED_NAME)
STATION_NAME = rule(STATION, QUOTED_NAME)

METRO_STATION = or_(
    STATION_METRO_NAME,
    STATION_NAME,
    QUOTED_KNOWN_NAME,
).interpretation(
    MetroStation
)
