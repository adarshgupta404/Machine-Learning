# working with JSON in python
book = {}
book['tom'] = {
    'name':'tom',
    'address':'1 red street',
    'phone':'34928023'
}
book['jerry'] = {
    'name':'jerry',
    'address':'1 green street',
    'phone':'44922133'
}
import json
s=json.dumps(book)
with open("d://Git Hub//Machine-Learning//Basics Python//book.txt", "w") as f:
    f.write(s)
    f.close()

