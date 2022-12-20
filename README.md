# 神经网络与深度学习-验证码训练&预测

 > 每个文件夹的作用如下：
 
 - GetJaccountCaptcha：从网站获取验证码图片的爬虫脚本

 - GetStringFromCaptcha：使用第三方验证码库，完成爬虫验证码图片的打标

 - SplitCaptchaBit：可以将验证码图片按照不同位数区分开

 - Traning&Predicting：自行构建 CNN 网络，通过 Python 3.10、Cuda 11.7 完成训练与预测。

 - CompareChar：用于分析自建 CNN 模型识别的验证码失败的原因。