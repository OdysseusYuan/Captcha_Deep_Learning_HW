"""
      [Captcha Deep Learning Project] Copyright (C) 2022 liukaiyuan@sjtu.edu.cn Inc.

      FileName : train.py
      Developer: liukaiyuan@sjtu.edu.cn (Odysseus.Yuan)
"""
import os

import torch
from torch import nn
from torch.utils.data import DataLoader
from tensorboardX import SummaryWriter

import data_load
import device_cfg
from cnn_model import CnnModel
import captcha_info


# 训练环境：pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu117
if __name__ == '__main__':
    # 训练的文件夹名称，修改后，一定要修改验证码尺寸
    train_name = 'bjd.com.cn'

    # 加载训练数据
    train_datas = data_load.DataLoad("./data/" + train_name + "-training/")

    # 批量处理验证码数据
    train_dataloader = DataLoader(train_datas, batch_size=40, shuffle=True)

    # 调试：用于tensorboard
    w = SummaryWriter("tensor_logs")

    # 初始化模型
    m = CnnModel().to(device_cfg.device)

    # 使用多标签损失函数计算
    loss_fn = nn.MultiLabelSoftMarginLoss().to(device_cfg.device)

    # 使用亚当优化器，0.0003学习速率
    optimizer = torch.optim.Adam(m.parameters(), lr=0.0003)

    # 总训练次数
    total_step = -100

    # 上次保存的pth文件名
    last_pth_filename = ''

    # 执行100次训练
    for i in range(100):
        print("集合模型已训练 {} 次 ...".format(i))

        # 执行一次训练
        for j, (images, label) in enumerate(train_dataloader):

            # 自适应运算
            images = images.to(device_cfg.device)
            label = label.to(device_cfg.device)

            # 开启训练
            m.train()

            # 获得卷积后数据
            outputs = m(images)

            # 获得损失
            loss = loss_fn(outputs, label)

            # 使用优化器梯度归零
            optimizer.zero_grad()

            # 反向传播计算
            loss.backward()

            # 优化器迭代
            optimizer.step()

            if j % 100 == 0:

                total_step += 100

                print("内核已训练 {} 次，损失 {}".format(total_step, loss.item()))

                # 调试：用于tensorboard
                w.add_scalar("loss 100e " + train_name, loss, total_step)

                # 周期性的写出训练模型，防止中途关机导致前功尽弃
                last_pth_path = os.getcwd() + '/' + last_pth_filename
                if last_pth_filename.__len__() != 0 & os.path.exists(last_pth_path):
                    # 删除旧的 last_pth_filename 文件
                    os.remove(last_pth_path)

                # 生成新的pth文件名
                last_pth_filename = "cnn_model_" + train_name + '_' \
                                    + captcha_info.pix_x.__str__() + 'x' + captcha_info.pix_y.__str__() \
                                    + '_' + total_step.__str__() + ".pth"

                # 保存最新的训练模型（GPU训练，CPU读取）
                torch.save(m, last_pth_filename)
