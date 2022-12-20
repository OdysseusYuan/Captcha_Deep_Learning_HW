"""
      [Captcha Deep Learning Project] Copyright (C) 2022 liukaiyuan@sjtu.edu.cn Inc.

      FileName : data_load.py
      Developer: liukaiyuan@sjtu.edu.cn (Odysseus.Yuan)
"""

import os
from PIL import Image
from torch.utils.data import Dataset
from torchvision import transforms
from tensorboardX import SummaryWriter
import one_hot
import captcha_info


# 创建一个继承torch的数据集加载类库
class DataLoad(Dataset):

    # 类初始化函数
    def __init__(self, root_dir):
        # 遍历获取目录下所有图片文件名
        super(DataLoad, self).__init__()

        # 将文件名转换为所对应的路径名
        self.list_image_path = [os.path.join(root_dir, image_name) for image_name in os.listdir(root_dir)]

        # 将image图片资源转换为cnn/torch能够识别的格式
        self.transforms = transforms.Compose([

            # 初始化图片
            transforms.ToTensor(),

            # 设置图片尺寸，jAccount的尺寸都是 110x40
            transforms.Resize((captcha_info.pix_y, captcha_info.pix_x)),

            # 转换为灰度图
            transforms.Grayscale()

        ])

    # 获取某个图像索引中，单个图片的信息
    def __getitem__(self, index):
        # 获取该数组索引对应的图片路径
        image_path = self.list_image_path[index]

        # 加载图片到内存中
        img_ = Image.open(image_path)

        # 从内存中读取图片资源，并转换为cnn/torch能够识别的格式
        img_tensor = self.transforms(img_)

        # 获取文件名
        image_name = image_path.split("/")[-1]

        # 从文件名中截取之前标记的正确验证码读数
        img_label = image_name.split("_")[0]

        # 把字符转换为独热编码
        img_label = one_hot.text2vec(img_label)

        # 将数据自乘，转换为线性值
        img_label = img_label.view(1, -1)[0]

        return img_tensor, img_label

    # 获取数据集文件数量
    def __len__(self):
        return self.list_image_path.__len__()


if __name__ == '__main__':

    # 遍历获取训练集所有图片，并转换为cnn可用图片格式
    d = DataLoad("./data/for_training/")

    # 获取tensor后的图片信息和正确的验证码值
    img, label = d[0]
    writer = SummaryWriter("logs")
    writer.add_image("img", img, 1)
    print(img.shape)
    writer.close()
    print(label)
