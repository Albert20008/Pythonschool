import struct

file = open('Двоичный_файл', 'rb')

num = file.read(2)

while num:

	print(struct.unpack('h', num)[0])

	num = file.read(2)

file.close()
