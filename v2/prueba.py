from sender import Sender

s = Sender(device='COM19')

s.send('2+2')
print(s.receive())