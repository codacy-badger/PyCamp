RUS_TO_EN_EXT = {
            'г': 'g',
            'ё': 'yo',
            'м':'m',
            'ф':'f',
            'х':'h',
            'ч':'ch',
            'ш':'sh',
            'щ':'sh',
            'ы':'u',
            'й':'y',
            'ю':'yu',
            'я':'ya',
            'з':'z',
            'ж':'zh'
            }

EX_RUS = "Эта строка будет подверена транслитерации".replace(' ','').lower()
EX_EN = "Eta stroka budet podverena transliteracii".replace(' ', '').lower()

RUS_TO_EN = {EX_RUS[i]:EX_EN[i] for i in range(len(EX_RUS))}
RUS_TO_EN.update(RUS_TO_EN_EXT)
PUNCT_MARKS = r"'\"-_\\/.,:;`~ !?\n"


class TranslitError(Exception):
    def __init__(self, message):

        super(TranslitError, self).__init__(message)


def get_translator(lan_from, lan_to):
    if lan_from == 'rus' and lan_to == 'en':
        return RUS_TO_EN
    return False

def translate(translator, text):
    translit_text = []
    for letter in text:
        up = False

        if letter.isupper():
            up = True
        letter = letter.lower()

        if letter in PUNCT_MARKS or letter.isdigit() or letter.isspace():
            translit_text.append(letter)
        elif letter in translator:
            if up:
                 new_let = translator[letter.lower()].upper()
                 translit_text.append(new_let)
            else:
                translit_text.append(translator[letter])
        else:
            raise TranslitError("Can't translate symbol: {}".format(letter))
    return ''.join(translit_text)


def main():
    text = ''
    with open('text', 'r') as f:
        text = f.read()
    print("Native text: \n" + text)
    translator = get_translator('rus', 'en')
    translit_text = translate(translator, text)
    print("Translated text: \n" + translit_text)

if __name__ == "__main__":
    main()
