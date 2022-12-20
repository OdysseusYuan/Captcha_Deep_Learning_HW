"""
      [Captcha Deep Learning Project] Copyright (C) 2022 liukaiyuan@sjtu.edu.cn Inc.

      FileName : device_cfg.py
      FileInfo : 选择是否使用cuda进行训练或预测
      Developer: liukaiyuan@sjtu.edu.cn (Odysseus.Yuan)
"""
import torch

# 如果存在可用的cuda，则使用cuda，否则使用cpu
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
