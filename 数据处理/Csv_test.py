import csv#引入csv库（用来处理csv格式文件

with open('input.csv', mode='r', encoding='utf-8') as infile:#读取文件用到方法DictReader
    reader = csv.DictReader(infile)
    data = list(reader)

data_sorted = sorted(data, key=lambda x: int(x['Score']), reverse=True)#使用sort方法（要排序的，以什么关键字排（key=lambda x：（参数）），升降序（默认为False降序，升序True

with open('output.csv', mode='w', encoding='utf-8', newline='') as outfile:
    fieldnames = ['Name', 'Score']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in data_sorted:
        writer.writerow(row)
