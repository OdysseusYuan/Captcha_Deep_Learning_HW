"""
      [Captcha Deep Learning Project] Copyright (C) 2022 liukaiyuan@sjtu.edu.cn Inc.

      FileName : cnn_model.py
      Developer: liukaiyuan@sjtu.edu.cn (Odysseus.Yuan)
"""

import torch
from torch import nn
import captcha_info


# 定义卷积神经网络
class CnnModel(nn.Module):
    def __init__(self):
        # 初始化父类
        super(CnnModel, self).__init__()

        # 构建第1层
        self.layer1 = nn.Sequential(
            # 卷积层：灰度图初始值为1，输出64个通道，卷积核3x3，填充1层
            nn.Conv2d(in_channels=1, out_channels=64, kernel_size=3, padding=1),

            # 激活
            nn.ReLU(),

            # 池化
            nn.MaxPool2d(kernel_size=2)
        )

        # 构建第2层
        self.layer2 = nn.Sequential(
            # 卷积64->128
            nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, padding=1),

            # 激活
            nn.ReLU(),

            # 池化
            nn.MaxPool2d(2)
        )

        # 构建第3层
        self.layer3 = nn.Sequential(
            # 卷积128->256
            nn.Conv2d(in_channels=128, out_channels=256, kernel_size=3, padding=1),

            # 激活
            nn.ReLU(),

            # 池化
            nn.MaxPool2d(2)
        )

        # 构建第4层 [64, 512, 2, 6]
        self.layer4 = nn.Sequential(
            # 卷积256->512
            nn.Conv2d(in_channels=256, out_channels=512, kernel_size=3, padding=1),

            # 激活
            nn.ReLU(),

            # 池化
            nn.MaxPool2d(2)
        )

        # 构建第5层 [64, 1024, 1, 3]
        self.layer5 = nn.Sequential(
            # 卷积512->1024
            nn.Conv2d(in_channels=512, out_channels=1024, kernel_size=3, padding=1),

            # 激活
            nn.ReLU(),

            # 池化
            nn.MaxPool2d(2)
        )

        # 构建第6层（全连接层）
        self.layer6 = nn.Sequential(
            # 展平自乘
            nn.Flatten(),

            # 线性值，展平结果不考虑64，其不参与运算
            nn.Linear(in_features=7168, out_features=4096),

            # 丢弃20%，防止过拟合
            nn.Dropout(0.2),
            nn.ReLU(),

            # 与验证码组成内容关联，线性处理
            nn.Linear(in_features=4096, out_features=captcha_info.Dictionary.__len__() * captcha_info.CharLen)
        )

    # 启动正向方法，将输入张量映射到预测输出张量的映射
    def forward(self, result):
        result = self.layer1(result)
        result = self.layer2(result)
        result = self.layer3(result)
        result = self.layer4(result)
        result = self.layer5(result)

        # print(result.shape[1] * result.shape[2] * result.shape[3])

        result = self.layer6(result)

        return result


if __name__ == '__main__':
    # 测试构造64张jAccount图片
    data = torch.ones(1, 1, captcha_info.pix_y, captcha_info.pix_x)

    # 初始化CNN
    model = CnnModel()

    # 获得最终值
    x = model(data)

    # print(x.shape)
