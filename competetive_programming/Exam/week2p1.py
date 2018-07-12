def func(li):

    letters={'a' :".-",
    'b' :"-...",
    'c' :"-.-.",
    'd' :"-..",
    'e' :".",
    'f' :"..-.",
    'g' :"--.",
    'h' :"....",
    'i' :"..",
    'j' :".---",
    'k' :"-.-",
    'l' :".-..",
    'm' :"--",	
    'n' :"-.",
    'o' :"---",
    'p' :".--.",
    'q' :"--.-",
    'r' :".-.",
    's' :"...",
    't' :"-",
    'u' :"..-",
    'v' :"...-",
    'w' :".--",
    'x' :"-..-",
    'y' :"-.--",
    'z' :"--.."}
    words={}
    for i in li:
        dummy=""
        for j in i:
            dummy+=letters[j]
        words[dummy]=i

    
   
    
    print(len(words))
    
func(["gin","zen","gig","msg"])
func(["a", "z", "g", "m"])
func(["bhi", "vsv", "sgh", "vbi"])
func( ["a", "b", "c", "d"] )
func( ["hig", "sip", "pot"] )


