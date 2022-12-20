/*
 *      [LKY Common Tools] Copyright (C) 2022 liukaiyuan@sjtu.edu.cn Inc.
 *      
 *      FileName : Program.cs
 *      Developer: liukaiyuan@sjtu.edu.cn (Odysseus.Yuan)
 */

using Common;
using System;
using System.IO;
using System.Threading.Tasks;

namespace GetJaccountCaptcha
{
    internal class Program
    {
        static void Main(string[] args)
        {
            GetCharImg(10300, 11500);

            Console.WriteLine("done!");
            Console.Read();
        }

        /// <summary>
        /// 读取静态验证码的类型。需要先从网页中找到验证码地址
        /// </summary>
        /// <param name="start_index"></param>
        /// <param name="end_index"></param>
        static void SplitAndGetCharImg(int start_index, int end_index)
        {
            try
            {
                string Jaccount_Url = "https://zw.nrta.gov.cn:8444/authcenter/zwfw/personInfo/personInfoReg.jsp?appCode=zwfwmh";
                string Captcha_Dir = Environment.CurrentDirectory + "\\captcha_training";

                Directory.CreateDirectory(Captcha_Dir);

                for (int index = start_index; index <= end_index; index++)
                {
                    //保存文件名
                    string save_to_name = $@"CFA-PLA_captcha_forDL_{index}.jpg";

                    //先获取验证码地址
                    var html = Com_WebOS.Visit_WebClient(Jaccount_Url);

                    StreamReader sr = new StreamReader(html);

                    //获取图片地址
                    var img_url = Com_TextOS.GetCenterText(sr.ReadToEnd(), "class=\"bxm_button\" src=\"", "\">");

                    //获取Jaccount验证码流
                    var captcha = Com_WebOS.Visit_WebClient(img_url);

                    //保存至文件
                    Com_FileOS.Covert.StreamToFile(captcha, $@"{Captcha_Dir}\{save_to_name}");

                    Console.WriteLine(save_to_name);
                }

            }
            catch (Exception e)
            {
                Console.WriteLine(e);
            }
        }

        static void GetCharImg(int start_index, int end_index)
        {
            try
            {
                //string Jaccount_Url = "https://jaccount.sjtu.edu.cn/jaccount/captcha";
                string Jaccount_Url = "http://cp.xinnet.com/captcha";
                string Captcha_Dir = Environment.CurrentDirectory + "\\captcha_training";

                Directory.CreateDirectory(Captcha_Dir);

                for (int index = start_index; index <= end_index; index++)
                {
                    //保存文件名
                    string save_to_name = $@"CFA-PLA_captcha_forDL_{index}.jpg";

                    //获取Jaccount验证码流
                    var captcha = Com_WebOS.Visit_WebClient(Jaccount_Url);

                    //保存至文件
                    Com_FileOS.Covert.StreamToFile(captcha, $@"{Captcha_Dir}\{save_to_name}");

                    Console.WriteLine(save_to_name);
                }

            }
            catch (Exception e)
            {
                Console.WriteLine(e);
            }
        }
    }
}
