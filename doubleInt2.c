#include<stdlib.h>
#include<stdio.h>
#include<locale.h>
#include<math.h>


double intfunc(double x){
  return 1/(x + 5 + y);
}

int main(){
  double a = 2,b = 8,c = 8,d = 10;
  //scanf("Введите a, b, c, d\n %lf %lf %lf %lf",a,b,c,d);
  double nx = 10000,ny = 10000;
  double hx = (b - a)/nx, hy = (d - c)/ny;
  printf("hx = %lf, hy = %lf\n",hx,hy);
  double I = 0;
  while(x <= b){
    while(y <= d){
      xi = a + hx/2 + i*hx;
      yj = c + hy/2 + j*hy;
      I+=hx*hy*intfunc(xi,yj);
      y+=hy;
    }
    x +=hx;
  }
  printf("Answer: %lf\n",I);
  return 0;
}
