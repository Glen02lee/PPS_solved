#include <string>
#include <iostream>
#include <stdbool.h>
using namespace std;

bool solution(string s)
{
    bool answer = true;
    int p = 0, y = 0;
    
    for (char& c : s){
        c = tolower(c);
        if(c == 'p') p++;
        if(c == 'y') y++;
    }
    if (p != y) answer = false; 
    

    return answer;
}
/*
아스키코드값을 이용하던지, 대소문자 다 봐주던지해도 되지만
최대한 간결하게 코드를 작성해보고 싶어서
변환후 바로 조건문을 걸었다.
*/