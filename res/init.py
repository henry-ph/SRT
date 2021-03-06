# -*- coding: utf-8 -*-

import re
import jieba

dataFile = open("公共参与.csv", encoding="utf-8")
result = open("processed.csv", "w", encoding="utf-8")

for lines in dataFile:
    rawCommentList = []  # 原始评论
    comment = []  # 单条评论
    commentList = []  # 最终列表
#    print(lines)
    lines = lines.replace('\n', "")  # 去除末尾回车
    lines = "@default:" + lines
    lines = re.sub(r'((http|ftp|https)://)'
                   r'(([a-zA-Z0-9\._-]+\.[a-zA-Z]{2,6})|([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}))'
                   r'(:[0-9]{1,4})*(/[a-zA-Z0-9\&%_\./-~-]*)?|'
                   r'[【】]|'
                   r'#.*?#|'
                   r'\[.*?\]|'
                   r'\?*', "", lines)  # 匹配网址，【】、[]、##间所有内容
#    print(lines)
    rawCommentList = lines.split("//")  # 以//分割评论，最后一条即为原内容
    for items in rawCommentList:
        comment = items.split(":")  # 以:分割评论者与内容
        for words in comment:
            if words == '':
                continue
            if not words[0] == '@':
                if re.search('@', words):
                    pos = words.find('@')
                    words = words[:pos] + '\n' + words[pos:]
                    cutList = jieba.cut(words)
                    words = " ".join(cutList)  # 换行得到被转发的微博
                else:
                    cutList = jieba.cut(words)
                    words = " ".join(cutList)
            result.write(words + ',')
        result.write('\n')
        commentList.append(comment)
#    print(commentList)
result.close()

