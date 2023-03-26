import json,random

with open('jokes.json') as f:
    jokes = json.load(f)
    
        
#fat,stupid,old,ugly        
#print(jokes.keys())


generate_joke = lambda qkey: random.choice(jokes[qkey])



if __name__=='__main__':
    
    key = input ('Enter query key: [fat, stupid, old, ugly, poor, nasty] : ')
    output= generate_joke(key)
    print('='*30)
    print(output)

