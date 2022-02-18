using System;
using System.Linq;
using System.Windows.Forms;
using System.IO;

namespace pdf_parser
{
    static class Program
    {
        [STAThread]
        public static void Main()//string[] args)
        {   
            string mytext="";
            try{
                string[] args = {@"C:\Users\sglazkov\Documents\pythonProject\pdf_parser\test\079322C-AWP1A-300-CS-KMD-06810-D-0726_01.pdf"};
                var argsList = args.ToList();
                foreach(var file in argsList) 
                {
                    if (File.Exists(file)) 
                    {
                        string[] temp = file.Split(Convert.ToChar("\\"));
                        mytext += temp[temp.Length-1];
                        mytext += (char)10;
                        
                        try
                        {
                            mytext += recode(PdfExtractor.pdfText(file)); 
                        }
                        catch
                        {
                            throw new Exception($"Extracting from: {file} was interrupted\nor file is broken");
                        }
                        
                        mytext += "/////";
                    }
                    else
                    {
                        throw new Exception($"File: {file} not found");
                    }
                }
                Clipboard.SetText(mytext);
                if(Clipboard.GetText().Length ==0) {MessageBox.Show("Something goes wrong while extracting text from pdf");}
            }
            catch (Exception e)
            {
                MessageBox.Show($"EXCEPTION \n\nError occured while exporting file \n\nError details:\n{e.Message}");
            }
        }

        public static string recode(string content)
        {
            string temp = "";
            foreach(char letter in content)
            {
                if((int)letter-16<=239 & (int)letter-16>=224) 
                {
                    temp += (char)(int)letter+848;
                }
                else if((int)letter-64<=175 & (int)letter-64>=128)
                {
                    temp += (char)(int)letter+848;
                }
                else
                {
                    temp += letter;
                }
            }
            return temp;
        }
    }
}
