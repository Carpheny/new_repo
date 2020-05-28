//
//  main.cpp
//
//  Created by Ｍac on 2020/4/8.
//  Copyright © 2020 Ｍac. All rights reserved.
//

#include <iostream>
#include <cstdlib>
#include <fstream>
#include <cstring>
#include <cstdio>
#include <cmath>
using namespace std;
class v{
public:
    v(double a,double b);
    friend v cal(double a,double b);
    friend ostream &operator << (ostream &o,v &f);
private:
    double x,y;
};
v::v(double a,double b){
    x=a;
    y=b;
}

v cal(double a,double b){
    v temp(0,0);
    temp.x=sqrt(1/(1+pow(b/a,2)));
     temp.y=sqrt(pow(b/a,2)/(1+pow(b/a,2)));
    return temp;
}
ostream &operator << (ostream &o,v &f){
    cout<<f.x<<","<<f.y;
    return o;
}
int main() {
    double a,b;
    cout<<"input: ";
    cin>>a>>b;
    v first(a,b);
    first = cal(a, b);
    cout<<first;
    return 0;
}

//third edition
