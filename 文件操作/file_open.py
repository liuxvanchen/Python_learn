with open('/文艺部/2023十佳歌手/文艺部例会.txt', 'r') as file:
    content = file.read()
print(content)

with open('/文艺部/2023十佳歌手/文艺部例会.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

fp=open('/文艺部/新建 文本文档.txt', 'w', encoding='utf-8')
fp.write("hello world")
fp.close()