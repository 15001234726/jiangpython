import codecs



with codecs.open ('/Users/katyjiang/Desktop/.txt', 'w','gbk') as f:

    f.write("hello double")

with codecs.open ('/Users/katyjiang/Desktop/python.txt', 'r','gbk') as f:

    print(f.read())