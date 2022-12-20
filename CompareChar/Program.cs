using System;
using System.Collections.Generic;
using System.IO;

namespace CompareChar
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string run_path = Environment.CurrentDirectory;

            //获取所有 原值
            string old_filepath = run_path + "\\" + "old.txt";

            //获取原值内容
            string old_content = File.ReadAllText(old_filepath).Replace("\r", "");

            //获取数组
            var old_char = old_content.Split('\n');

            //获取所有 预测值
            string predict_filepath = run_path + "\\" + "new.txt";

            //获取预测值内容
            string predict_content = File.ReadAllText(predict_filepath).Replace("\r", "");

            //获取数组
            var predict_char = predict_content.Split('\n');

            int only_lower = 0; //因为大小写不一样产生的错误
            Dictionary<string, string> err_dic = new Dictionary<string, string>();  //和大小写无关的错误

            for (int i = 0; i < old_char.Length; i++)
            {
                if (old_char[i].ToLower() == predict_char[i].ToLower())
                {
                    //找出因为大小写不一样，进而判断失败的字符
                    only_lower++;
                }
                else
                {
                    err_dic[old_char[i]] = predict_char[i];
                }
            }

            Console.WriteLine("大小写问题：" + only_lower);

            //输出与大小写无关的错误预测字典
            foreach (var now_char in err_dic)
            {
                Console.WriteLine(now_char.Key + ", " + now_char.Value);
            }
        }
    }
}
