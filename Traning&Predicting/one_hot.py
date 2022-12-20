"""
      [Captcha Deep Learning Project] Copyright (C) 2022 liukaiyuan@sjtu.edu.cn Inc.

      FileName : one_hot.py
      Developer: liukaiyuan@sjtu.edu.cn (Odysseus.Yuan)
"""

import captcha_info
import torch


# 将文本转换为向量矩阵
def text2vec(text):
    vectors = torch.zeros((captcha_info.CharLen, captcha_info.Dictionary.__len__()))

    for i in range(len(text)):
        # 通过字母，匹配到索引
        vectors[i, captcha_info.Dictionary.index(text[i])] = 1
    return vectors


# 将向量矩阵转换为文本
def vec2text(vector):
    vector = torch.argmax(vector, dim=1)

    text_label = ""
    for v in vector:
        # 通过索引，对应到字母
        text_label += captcha_info.Dictionary[v]
    return text_label


if __name__ == '__main__':
    vec = text2vec("Haag")
    vec = vec.view(1, -1)[0]
    print(vec, vec.shape)
