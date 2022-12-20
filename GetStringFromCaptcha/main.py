import os
import string
from shutil import copyfile

import ddddocr


# 判断是否存在中文字符
def is_Chinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


# 破解识别验证码
def crack_captcha():
    predict_dir = "./captcha_organic/"

    predict_dir_list = os.listdir(predict_dir)

    for i, (sub_path) in enumerate(predict_dir_list):
        dir_name = sub_path

        sub_path = predict_dir + "/" + sub_path

        predict_list = os.listdir(sub_path)

        ocr = ddddocr.DdddOcr()

        total_images = predict_list.__len__()

        total_file = 0
        for i, (image_path) in enumerate(predict_list):
            # 拼接路径
            image_path = sub_path + "/" + image_path

            with open(image_path, 'rb') as f:
                img_bytes = f.read()
            res = ocr.classification(img_bytes)

            # 不仅只有数字、英文时，跳过
            if not res.encode().isalnum():
                continue

            # 字符数不等于4时，跳过
            if res.__len__() != 4:
                continue

            # 有中文字符时，跳过
            if is_Chinese(res):
                continue

            # print('正在破解 ' + image_path + ' -------> ' + res)

            # 创建文件夹
            save_dir = 'captcha_decoded\\' + dir_name
            folder = os.path.exists(save_dir)
            if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
                os.makedirs(save_dir)  # makedirs 创建文件时如果路径不存在会创建这个路径

            # 保存名称：captcha_decoded\btime.com_test\abcd_btime.com-test_captcha_12546.jpg
            copyfile(image_path,
                     save_dir + "\\" + res + '_' + dir_name + '_captcha_' + i.__str__() + '.jpg')

            total_file += 1

            print("完成率：{} %".format(total_file / total_images * 100))


if __name__ == '__main__':
    crack_captcha()
    print('done!')
