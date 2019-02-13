from Translation import translait

fail = open('файл №2', 'r')

Pre_content = fail.read()
Pre_content = Pre_content.split()

fail.close()

fail = open('файл №2', 'w')

for i in range(len(Pre_content) - 1):

	fail.write(translait(int(Pre_content[i])) + ', ')

fail.write(translait(int(Pre_content[-1])))

fail.close()
