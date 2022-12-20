"""
      [Captcha Deep Learning Project] Copyright (C) 2022 liukaiyuan@sjtu.edu.cn Inc.

      FileName : predict.py
      Developer: liukaiyuan@sjtu.edu.cn (Odysseus.Yuan)
"""
import os

import torch
from PIL import Image
from torch.utils.data import DataLoader
from torchvision import transforms

import captcha_info
import data_load
import device_cfg
import one_hot


# 批量预测
def predict_all():
    # 明确测试目录
    predict_dir = "./data/bjd.com.cn-test"

    # 加载目录下所有文件
    predict_list = os.listdir(predict_dir)

    # 获取总文件数
    total_images = predict_list.__len__()

    # 正确数
    total_correct = 0
    for i, (image_path) in enumerate(predict_list):
        # 拼接路径
        image_path = predict_dir + "/" + image_path

        # 预测并返回结果
        result = predict_img(image_path)
        print("剩余：{} 张".format(total_images - i))

        # 累加正确数量
        if result == 1:
            total_correct += 1

    print("正确率{}".format(total_correct / total_images * 100))


# 预测某一张图片
def predict_img(img_path):
    # 获取文件名
    img_filename = img_path.split("/")[-1]

    # 获取正确的值
    correct_label = img_filename.split("_")[0]

    # 加载指定路径的图片
    img = Image.open(img_path)

    # 初始化灰度图
    tensor_img = transforms.Compose([
        transforms.Grayscale(),
        transforms.Resize((captcha_info.pix_y, captcha_info.pix_x)),
        transforms.ToTensor()
    ])

    # img转换为tenser的img
    img = tensor_img(img).to(device_cfg.device)

    # 三维Vec转换为torch的四维Vec
    img = torch.reshape(img, (-1, 1, captcha_info.pix_y, captcha_info.pix_x))

    # 加载训练模型
    m = torch.load("cnn_model_bjd.com.cn_240x60_29900.pth").to(device_cfg.device)

    # 标记为预测模式
    m.eval()

    # 获得预测概率
    outputs = m(img)

    # 匹配预测值
    outputs = outputs.view(-1, len(captcha_info.Dictionary))

    # 将线性值输出为标签值
    predict_label = one_hot.vec2text(outputs)

    # 判断预测结果（不区分大小写）
    if correct_label.lower() == predict_label.lower():
        # print("预测 ---> 正确。原值:{}，预测值:{}".format(correct_label, predict_label))
        return 1
    else:
        print("预测 ---> 失败。原值:{}，预测值:{}。争议图片地址：{}".format(correct_label, predict_label, img_path))
        return 0


if __name__ == '__main__':
    predict_all()
    # predict_img("data/for_training/0Bh6.jpg")
