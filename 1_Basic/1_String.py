
message1 = 'Bobby\'s world'
print(message1)

message2 = "Body's world"
print(message2)

message3 = """Body's world was a good
cartoon int he 1990's"""
print(message3)

message = 'Hello world'
print(len(message))
print(message[0])
print(message[0:7])
print(message[:8])
print(message[3:])
print(message.lower())
print(message.upper())
print(message.count('Hello'))
print(message.count('l'))
print(message.find('world'))
print(message.find('universe'))
new_message = message.replace('world','Universe')
print(message)
print(new_message)

message = message.replace('world','Universe')
print(message)

greeting = 'Hello'
name = 'Michael'

message = greeting + ', ' + name + '. Welcome!'
print(message)

message = '{},{}.Welcome'.format(greeting,name)
print(message)

message= f'{greeting}, {name.upper()}. Welcome'
print(message)

print(dir(name))
print(help(name.lower()))






