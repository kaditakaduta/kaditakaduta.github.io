import codecs
inputf = codecs.open("README.md",'r',encoding='utf-8')
page = 1
outputf = codecs.open("page" + str(page) + ".md", "w", encoding='utf-8')
linenum = 0
for line in inputf:
    linenum += 1
    outputf.write(line)
    if linenum % 20 == 0:
        page += 1
        outputf.write("\r\n[next](page" + str(page) + ")")
        outputf.close()
        outputf = codecs.open("page" + str(page) + ".md", "w", encoding='utf-8')
        linenum = 0
outputf.close()