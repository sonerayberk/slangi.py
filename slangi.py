""" Inspired by (snatched?) tucnak """

import re


british = {
    'brother': 'bruv',
    'man': 'chap',
    'men': 'chaps',
    'guy': 'bloke',
    'boy': 'lad',
    'woman': 'lady',
    'women': 'ladies',
    'hello': 'ayy',
    'awesome': 'dog\'s bollocks',
    'brilliant': 'brill',
    'absolutely': 'total',
    'crazy': 'mental',
    'insane': 'bonkers',
    'shit': 'bollocks',
    'tired': 'knackered',
    'amazed': 'gobsmacked',
    'gay': 'puff',
    'saucy': 'cheeky',
}


shortcuts = {
    'you': 'u',
    'your': 'ur',
    'we': 'v',
    'this': 'dis',
    'these': 'dis',
    'that': 'dat',
    'eight': '8',
    'ate': '8',
    'for': '4',
    'too': '2',
    'to': '2',
}


def slangipy(text: str) -> str:
    text = text.lower()

    for replace, replace_with in british.items():
        text = text.replace(replace, replace_with)

    for replace, replace_with in shortcuts.items():
        regex = re.compile('\\b' + replace + '\\b')
        text = re.sub(regex, replace_with, text)

    return text


def test_slangipy() -> None:
    parametrize = (
        ('Hello brother!', 'ayy bruv!'),
        ('The film was awesome', 'the film was dog\'s bollocks'),
        ('This boy is too insane', 'dis lad is 2 bonkers'),
        ('The boy with the broken halo', 'the lad with the broken halo'),
    )

    for input, output in parametrize:
        cooked = slangipy(input)
        assert output == cooked
