import struct

num = int(input('>>>'))

file = open('Двоичный_файл', 'wb')

for i in range(1, num + 1):

	file.write(struct.pack('h', i))

file.close()
