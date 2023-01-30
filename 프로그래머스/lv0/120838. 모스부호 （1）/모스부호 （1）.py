def solution(letter):
    answer = []
    morse = { 
        '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
        '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
        '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
        '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
        '-.--':'y','--..':'z'
    }
    letter = letter.replace('"','').split(' ')
    for i in range(len(letter)) :
        if letter[i] in morse :
            answer.append(morse[letter[i]])
    return ''.join(map(str, answer))