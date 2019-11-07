#include<stdlib.h>
#include<stdio.h>
#include<locale.h>
#include<math.h>

double intfunc(double x, double y){
  return 1/(x + 5 + y);
}

int main(){
  double a = 2,b = 8,c = 10,d = 15;
  //scanf("Введите a, b, c, d\n %lf %lf %lf %lf",a,b,c,d);
  printf("a = %lf, b = %lf, c = %lf, d = %lf\n", a, b, c, d);
  double nx = 10000, ny = 10000;
  printf("nx = %lf, ny = %lf\n", nx, ny);
  double hx = (b - a) / nx, hy = (d - c) / ny;
  printf("hx = %lf, hy = %lf\n", hx, hy);
  double sx = 0;
  double x = a;
  while(x <= b){
    double sy = 0;
    double y = c;
    while(y <= d){
      sy += fabs(intfunc(x, y));
      y += hy;
    }
    double IY = hy * sy;
    sx += IY;
    x += hx;
  }
  double IX = hx * sx;
  printf("Answer: %lf\n", IX);
  return 0;
}
