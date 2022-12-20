using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SplitCaptchaBit
{
    internal class Program
    {
        static void Main(string[] args)
        {
            var files = Directory.GetFiles(@"O:\学校生活留念\上海交通大学\培养计划\神经网络与深度学习\大作业课设\数据集获取\神经网络与深度学习-大作业-第11组\GetStringFromCaptcha\SJTU_jAccount_captcha_decoded");

            foreach (var file in files)
            {
                string cap_pre = Path.GetFileName(file).Split('_')[0];

                if (cap_pre.Length == 4)
                {
                    string dest_path = Path.GetDirectoryName(file) + "\\4bit\\" + Path.GetFileName(file);
                    File.Move(file, dest_path);
                }
            }
        }
    }
}
