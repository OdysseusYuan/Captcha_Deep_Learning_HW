"""
      [Captcha Deep Learning Project] Copyright (C) 2022 liukaiyuan@sjtu.edu.cn Inc.

      FileName : captcha_info.py
      FileInfo : 全局验证码的基础信息类库
      Developer: liukaiyuan@sjtu.edu.cn (Odysseus.Yuan)
"""
import torch

# 明确验证码的组成内容。由10个数字、26个字母组成
Dictionary = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

# 基于jAccount的验证码可知，验证码由4个字符组成
CharLen = 4

# 验证码尺寸信息，110 x 40
pix_x = 240
pix_y = 60

# board调试：tensorboard --logdir=./tensor_logs

if __name__ == '__main__':
    print(torch.__version__)
    print(torch.cuda.is_available())
