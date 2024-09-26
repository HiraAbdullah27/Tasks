def punc(text):
    text = text
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    n_text = str()
    num = ['1','2','3','4','5','6','7','8','9','0']
    print('text: ',text)
    for i in text:
        if i == ' ' or i in num:
            n_text += i
        if i.lower() in alpha:
            n_text += i
            
    print('punctuation excluded: ',n_text)
text = input("Enter text: ")
punc(text)

