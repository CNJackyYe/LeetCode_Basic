using System;
using System.Collections.Generic;
using System.Linq;

namespace Question
{
    class Program
    {
        public static string[] panChar { get; set; }

        static void Main(string[] args)
        {
            string[] _panChar = {" ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"};
            panChar = _panChar;
            Gobang();
        }

        public static void Gobang()
        {
            var Chess = new Dictionary<string, string>();
            int Count = 0;
            while (true)
            {
                Count += 1;
                Console.WriteLine(Count % 2 == 1 ? "●请输入：" : "○请输入：");
                string str = Console.ReadLine();
                if (str.Length == 2)
                {
                    var strlist = str.ToCharArray();
                    var type = Count % 2 == 1 ? "●" : "○";
                    Chess = GeneralGoBang(strlist[0].ToString(), strlist[1].ToString(), type, Chess);
                    if (CheckWin(strlist[0].ToString(), strlist[1].ToString(), type, Chess))
                    {
                        Console.WriteLine(type + " 恭喜你获得胜利");
                        break;
                    }
                }
                else
                {
                    Console.WriteLine("请重新输入");
                }
            }
        }

        public static Dictionary<string, string> GeneralGoBang(string str1, string str2, string type,
            Dictionary<string, string> Chess)
        {
            if (panChar.Contains(str1) && panChar.Contains(str2) && !Chess.ContainsKey(str1 + str2))
            {
                Chess.Add(str1 + str2, type);
                string printStr = "";
                for (var i = 0; i < panChar.Length; i++)
                {
                    for (var j = 0; j < panChar.Length; j++)
                    {
                        if (i == 0)
                        {
                            printStr += panChar[j] + " ";
                        }
                        else if (j == 0)
                        {
                            printStr += panChar[i] + " ";
                        }
                        else
                        {
                            printStr += CheckType(panChar[i], panChar[j], Chess) + " ";
                        }
                    }

                    printStr += "\n";
                }

                Console.WriteLine(printStr);
            }
            else
            {
                Console.WriteLine("输入错误的值");
            }

            return Chess;
        }

        public static string CheckType(string str1, string str2, Dictionary<string, string> Chess)
        {
            if (Chess.ContainsKey(str1 + str2))
            {
                return Chess[str1 + str2];
            }
            else
            {
                return "+";
            }
        }

        public static bool CheckWin(string str1, string str2, string type, Dictionary<string, string> chess)
        {
            var count = 0;
            bool winmark = false;
            int str1location = 4;
            int str2localtion = 4;

            for (var i = 0; i < 8; i++) //rowcheck
            {
                if (GetLocationChessType(str1location - 4 + i, str2localtion, chess, type))
                {
                    count++;
                }
                else
                {
                    count = 0;
                }

                if (count == 5)
                {
                    winmark = true;
                }
            }

            for (var j = 0; j < 8; j++) //colcheck
            {
                if (GetLocationChessType(str1location, str2localtion - 4 + j, chess, type))
                {
                    count++;
                }
                else
                {
                    count = 0;
                }

                if (count == 5)
                {
                    winmark = true;
                }
            }

            for (var k = 0; k < 8; k++) //xcheck
            {
                if (GetLocationChessType(str1location - 4 + k, str2localtion - 4 + k, chess, type))
                {
                    count++;
                }
                else
                {
                    count = 0;
                }

                if (count == 5)
                {
                    winmark = true;
                }
            }

            for (var k = 0; k < 8; k++) //xcheck
            {
                if (GetLocationChessType(str1location - 4 + k, str2localtion + 4 - k, chess, type))
                {
                    count++;
                }
                else
                {
                    count = 0;
                }

                if (count == 5)
                {
                    winmark = true;
                }
            }

            return winmark;
        }

        public static bool GetLocationChessType(int i, int j, Dictionary<string, string> chess, string type)
        {
            string dicstr = panChar[i] + panChar[j];
            if (chess.ContainsKey(dicstr))
            {
                return chess[dicstr] == type;
            }
            else
            {
                return false;
            }
        }
    }
}