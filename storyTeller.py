import random
when = ['Once upon a time', 'Yesterday', 'Last night', 'A long time ago','On 1st April']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle','a cat']
name = ['Zaza', 'Rari','Kazi', 'Hoola', 'Nani']
residence = ['Barcelona','India', 'Germany', 'Venice', 'England']
went = ['cinema', 'university','picnic', 'school', 'shopping']
who2 = ['a lion','a gorilla','an alien', 'a magician']
name2= ['Koka', 'Azar','Robert','Rile']
happened = ['made a lot of other friends','ate a pizza', 'found a secret key', 'solved a mistery', 'wrote a book']
print( random.choice(when) + ', ' + random.choice(who) + ' named ' + random.choice(name)+ ' who lived in ' + random.choice(residence)
     + ' went to the ' + random.choice(went) + ' where he met '+ random.choice(who2) + ' whose name was '+ random.choice(name2) + 
     '. They became best friends and ' + random.choice(happened) + ' together.')
