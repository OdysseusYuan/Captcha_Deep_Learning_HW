using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net.NetworkInformation;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace SelectNumberCaptcha
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //获取根目录
            string root_test = Environment.CurrentDirectory + "\\bjd.com.cn-fix-test";
            string root_training = Environment.CurrentDirectory + "\\bjd.com.cn-fix-training";

            //获取所有文件
            var test_files = Directory.GetFiles(root_test);
            var training_files = Directory.GetFiles(root_training);

            //过滤test集
            foreach (var now_test in test_files)
            { 
                string captcha = Path.GetFileNameWithoutExtension(now_test).Split('_')[0];

                //正则获取是否有英文字符
                int EngCount = Regex.Matches(captcha, "[a-zA-Z]").Count;

                //包含英文，将文件移动到 eng 文件夹
                if (EngCount > 0)
                {
                    string dest_dir = Path.GetDirectoryName(now_test) + "\\eng\\";
                    Directory.CreateDirectory(dest_dir);
                    string file_name = Path.GetFileName(now_test);
                    File.Move(now_test, dest_dir + file_name);
                    Console.WriteLine(dest_dir + file_name);
                }
            }

            //过滤training集
            foreach (var now_test in training_files)
            {
                string captcha = Path.GetFileNameWithoutExtension(now_test).Split('_')[0];

                //正则获取是否有英文字符
                int EngCount = Regex.Matches(captcha, "[a-zA-Z]").Count;

                //包含英文，将文件移动到 eng 文件夹
                if (EngCount > 0)
                {
                    string dest_dir = Path.GetDirectoryName(now_test) + "\\eng\\";
                    Directory.CreateDirectory(dest_dir);
                    string file_name = Path.GetFileName(now_test);
                    File.Move(now_test, dest_dir + file_name);
                    Console.WriteLine(dest_dir + file_name);
                }
            }
        }
    }
}
