from string import upper
from string import uppercase

EDICT = {'A': ".-", 'B': "-...", 'C': "-.-.", 'D': "-..", 'E': ".",
         'F': "..-.", 'G': "--.", 'H': "....", 'I': "..", 'J': ".---",
         'K': "-.-", 'L': ".-..", 'M': "--", 'N': "-.", 'O': "---",
         'P': ".--.", 'Q': "--.-", 'R': ".-.", 'S': "...", 'T': "-",
         'U': "..-", 'V': "...-", 'W': ".--", 'X': "-..-", 'Y': "-.--", 'Z': "--.."}

DDICT = {'---': 'O', '--.': 'G', '-...': 'B', '-..-': 'X',
         '.-.': 'R', '--.-': 'Q', '--..': 'Z', '.--': 'W', '.-': 'A',
         '..': 'I', '-.-.': 'C', '..-.': 'F', '-.--': 'Y',
         '-': 'T', '.': 'E', '.-..': 'L', '...': 'S', '..-': 'U',
         '-.-': 'K', '-..': 'D', '.---': 'J', '.--.': 'P',
         '--': 'M', '-.': 'N', '....': 'H', '...-': 'V'}


def morse_decode(x):
    return ' '.join(map(lambda i: DDICT[i], x.split()))


def morse_encode(x):
    return ' '.join(map(lambda i: EDICT[i], list(filter(lambda i: i in uppercase, upper(x)))))

if __name__ == '__main__':
    print morse_encode('this is a test')
    print morse_decode('.. .-.. --- ...- . -.-- --- ..-')
