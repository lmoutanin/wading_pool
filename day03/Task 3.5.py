import numpy as np

# Task 3.5

LETTER = 'abcdefghijklmnopqrstuvwxyz'
FREQUENCY_COUNT = {
    'en': {'a': 8.16, 'b': 1.49, 'c': 2.78, 'd': 4.25, 'e': 12.70, 'f': 2.22, 'g': 2.01, 'h': 6.09, 'i': 6.96,
           'j': 0.15, 'k': 0.77, 'l': 4.02, 'm': 2.40, 'n': 6.74, 'o': 7.50, 'p': 1.92, 'q': 0.09, 'r': 5.98, 's': 6.32,
           't': 9.05, 'u': 2.75, 'v': 0.97, 'w': 2.36, 'x': 0.15, 'y': 1.97, 'z': 0.07},
    'fr': {'a': 7.63, 'b': 0.90, 'c': 3.26, 'd': 3.66, 'e': 14.71, 'f': 1.06, 'g': 0.86, 'h': 0.73, 'i': 7.52,
           'j': 0.61, 'k': 0.07, 'l': 5.45, 'm': 2.96, 'n': 7.09, 'o': 5.79, 'p': 2.52, 'q': 1.36, 'r': 6.69, 's': 7.94,
           't': 7.24, 'u': 6.31, 'v': 1.83, 'w': 0.04, 'x': 0.42, 'y': 0.12, 'z': 0.32}}

SENTENCES = "La persévérance : la clé de la croissance et du succès. La vie est un voyage rempli de défis, d’échecs et de détours inattendus. Peu importe qui vous êtes ou d’où vous venez, les difficultés finiront par croiser votre chemin. Certains voient les obstacles comme des signes d’arrêt, tandis que d’autres les considèrent comme des occasions de devenir plus forts. Cette différence repose souvent sur une qualité essentielle : la persévérance. La persévérance, c’est la capacité à continuer d’avancer même lorsque les choses deviennent difficiles. C’est la détermination à continuer d’essayer malgré les échecs, les refus ou les moments de doute. L’histoire regorge d’exemples inspirants qui montrent la force de la persévérance. Thomas Edison, par exemple, a échoué des milliers de fois avant d’inventer avec succès l’ampoule électrique. Au lieu d’abandonner, il voyait chaque échec comme une leçon qui le rapprochait de son objectif. De la même manière, J.K. Rowling, l’auteure de la saga Harry Potter, a essuyé de nombreux refus d’éditeurs avant que ses livres ne deviennent un phénomène mondial. Sans persévérance, leurs réussites n’auraient jamais vu le jour. Sur le plan personnel, la persévérance est tout aussi essentielle. Que vous soyez en train de préparer un examen, d’apprendre une nouvelle compétence ou de travailler vers un objectif professionnel, la constance compte bien plus que les résultats immédiats. Le progrès n’est presque jamais instantané. Il arrive souvent par petites étapes, parfois si discrètes que vous ne vous en rendez compte qu’en regardant en arrière pour mesurer le chemin parcouru. La persévérance nous apprend la patience, la discipline et la résilience, autant de qualités qui nous préparent non seulement à réussir, mais aussi à affronter les défis de la vie adulte. Toutefois, persévérer ne signifie pas répéter obstinément les mêmes actions sans réfléchir. La véritable persévérance implique une capacité d’adaptation. Il s’agit d’analyser ce qui n’a pas fonctionné, d’apporter des améliorations puis de réessayer avec une vision plus claire. En ce sens, la persévérance n’est pas un effort aveugle mais une combinaison de constance et d’intelligence. Dans le monde d’aujourd’hui, où tout semble aller vite, beaucoup s’attendent à des récompenses immédiates. Nous vivons dans une culture de gratification instantanée où l’attente paraît inconfortable. Pourtant, les réussites les plus significatives—terminer un diplôme, construire une carrière, entretenir des relations solides ou même améliorer sa santé—demandent du temps et un effort régulier. C’est pourquoi la persévérance reste une qualité si précieuse. Elle nous rappelle que les grandes choses ne sont presque jamais faciles, mais qu’elles valent toujours la peine d’être poursuivies. En fin de compte, la persévérance est plus qu’une stratégie de réussite : c’est un état d’esprit. C’est la conviction que les difficultés sont temporaires mais que la croissance est permanente. Lorsque vous choisissez de persévérer, vous ne vous contentez pas de travailler vers un objectif, vous façonnez votre caractère. Et ce caractère vous accompagnera à chaque étape de votre vie, peu importe les défis que l’avenir mettra sur votre route."


def count_letter(sentence):
    letterCount = {}
    EFFECTIVE_TOTAL = 1

    for i in LETTER:
        if i in sentence:
            letterCount[i] = {}
            letterCount[i]['count'] = sentence.count(i)

    for i in letterCount:
        EFFECTIVE_TOTAL += letterCount[i]['count']

    for i in letterCount:
        frequency = letterCount[i]['count'] / EFFECTIVE_TOTAL * 100
        letterCount[i]['frequency'] = round(frequency, 2)
    return letterCount


def distance(frequency_country, frequency_sentences):
    country = []
    sentences = []
    for x in frequency_sentences:
        country.append(frequency_country[x])
        sentences.append(frequency_sentences[x]['frequency'])
    a = np.array(country)
    b = np.array(sentences)
    dist = np.linalg.norm(a - b)
    return dist


def distance_count(frequency_country, frequency_sentences):
    small_frequency = []
    small_distance = 0
    for x in frequency_country:
        small_distance = distance(frequency_country[x], frequency_sentences)
        try:
            if small_distance < small_frequency[1]:
                small_frequency[0] = x
                small_frequency[1] = small_distance
        except:
            small_frequency.append(x)
            small_frequency.append(small_distance)
    return small_frequency[0]


frequency_letter = count_letter(SENTENCES)
print(frequency_letter)
print(distance_count(FREQUENCY_COUNT, frequency_letter))
