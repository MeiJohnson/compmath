#include<stdlib.h>
#include<stdio.h>
#include<locale.h>
#include<math.h>
#include"myfunc.h"
double a, b;
int n;

double rectLeft(double h, double sm);
double rectR(double h);
double trap(double h);
double simpson(double h);
double intfunc(double x);
void mainMenu();
void secondMenu();
void thirdMenu();
void submenu();
void firstAlg();
void secondAlg();
int getValue(int count);
double mch(int num);
void clear_screen();
double derive(double x0, int num);
double countR(int num);

int main() {
    char *locale = setlocale(LC_ALL, "");

    printf("Enter a,b:\n");
    scanf("%lf %lf", &a, &b);
    printf("Enter n:\n");
    scanf("%d", &n);

    mainMenu();

    return 0;
}


double intfunc(double x){
  return 1 / (x + 5);
}

void clear_screen() {
#ifdef WINDOWS
    system("cls");
#else
    // Assume POSIX
    system ("clear");
#endif
}

void mainMenu() {
    clear_screen();
    printf("Main menu\n");
    printf("1. Constant step's methods\n");
    printf("2. Variable step's methods\n");
    printf("3. Exit\n");


    int value = getValue(3);

    switch (value)
    {
        case 1:
        {
            secondMenu();
            break;
        }
        case 2:
        {
            thirdMenu();
            break;
        }
        case 3:
        {
            exit(0);
            break;
        }
    }
}

void secondMenu() {
    clear_screen();
    printf("Constant step's methods menu\n");
    printf("1. Left rectangle\n");
    printf("2. Right rectangle\n");
    printf("3. Trapezi\n");
    printf("4. Simpson's method\n");
    printf("5. Return to main menu\n");

    int value = getValue(5);
    clear_screen();

    double d = b - a;
    double step = d / n;
    switch (value)
    {
        case 1:
        {
            double I = rectLeft(step,0);
            double rch = countR(1);
            printf("Definite integral %lf\nR = %lf\n", I, rch);
            submenu();
            break;
        }
        case 2:
        {
            double I = rectR(step);
            double rch = countR(2);
            printf("Definite integral %lf\nR = %lf\n", I, rch);
            submenu();
            break;
        }
        case 3:
        {
            double I = trap(step);
            double rch = countR(5);
            printf("Definite integral %lf\nR = %lf\n", I, rch);
            submenu();
            break;
        }
        case 4:
        {
            double I = simpson(step);
            printf("Definite integral %lf\n", I);
            submenu();
            break;
        }
        case 5:
        {
            mainMenu();
            break;
        }
    }
}

void thirdMenu() {
    clear_screen();
    printf("Main menu\n");
    printf("1. First algorithm\n");
    printf("2. Second algorithm\n");
    printf("3. Return to main menu\n");

    int value = getValue(3);
    clear_screen();
    switch (value)
    {
        case 1:
        {
            firstAlg();
            submenu();
            break;
        }
        case 2:
        {
            secondAlg();
            submenu();
            break;
        }
        case 3:
        {
            mainMenu();
            break;
        }
    }
}

void submenu() {

    printf("1. Back to main menu\n");
    printf("2. Exit\n");
    int value = getValue(2);
    switch (value)
    {
        case 1:
            mainMenu();
            break;

        case 2:
            exit(0);
            break;
    }
}

int getValue(int count) {
    int value;

    while (scanf("\n%d", &value) != 1 || value < 1 || value > count) {
        printf("Incorrect input. Try again: ");
        //scanf_s("%d", &value);
    }

    return value;
}

double rectLeft(double h, double sm) {
    double s = 0, x;
    x = a + sm;

    while (x <= (b - h))
    {
        s += intfunc(x);
        x += h;
    }
    double I = h * s;
    return I;
}

double rectR(double h) {

    double s = 0, x;

    x = a + h;

    while (x <= b)
    {
        s += intfunc(x);
        x += h;
    }
    double I = h * s;
    return I;
}

double trap(double h) {

    double s = (intfunc(a) + intfunc(b)) / 2;
    double x = a + h;
    while (x <= (b - h))
    {
        s += intfunc(x);
        x = x + h;
    }
    double I = h * s;

    return I;
}

double simpson(double h) {

    double s = (intfunc(a) + intfunc(b)), s1 = 0, s2 = 0;
    double x = a + h;

    while (x <= (b - h))
    {
        s1 += intfunc(x);
        x = x + 2 * h;
    };

    x = a + 2 * h;

    while (x <= (b - 2 * h))
    {
        s2 += intfunc(x);
        x = x + 2 * h;
    };

    double I = h / 3 * (s + 4 * s1 + 2 * s2);

    return I;
}

void firstAlg() {
    double eps;
    printf("Enter your accuracy\n");
    scanf("%lf", &eps);

    double step = pow(eps,1./2);
    double I1, I2;
    do {
        I1 = trap(step);
        I2 = trap(step / 2);
        step /= 2;
    } while (abs(I1 - I2) >= eps);

    printf("Definite integral %lf\n", I2);

}

void secondAlg() {
  double eps;
  printf("Enter your accuracy\n");
  scanf("%lf", &eps);

  double s1,s2,I1,I2;
  double hv = pow(eps,1./2), hs = hv/2;
  I1 = rectLeft(hv, 0.);
  I2 = 0;
  hv = hs;
  do {
      hs=hv/2;
      I1 = rectLeft(hv,hs);
      hv = hs;
      hs=hv/2;
      I2 = rectLeft(hv,hs);
      hv = hs;
  } while (abs(I1 - I2) >= eps);

  printf("Definite integral %lf\n", I2);
}

double derive(double x0, int num){
  switch (num) {
  case 1: return(-(1/((x0+5)*(x0+5))));
  case 2: return(2/((x0+5)*(x0+5)*(x0+5)));
  case 5: return(24/((x0+5)*(x0+5)*(x0+5)*(x0+5)*(x0+5)));
  }
}

double mch(int num){
  double x = a;
  double h = 0.1;
  double maxF = fabs(derive(x,num));
  x+=h;
  double derFunc1;
  while( x<=b ){
    derFunc1 = fabs(derive(x,num));
    maxF = fmax(derFunc1,maxF);
    x+=h;
    }
  return fabs(maxF);
}

double countR(int num){
  switch (num) {
  case 1: return (((b - a)*(b - a))/(2*n))*mch(1);
  case 2: return (((b - a)*(b - a))/(2*n))*mch(2);
  case 5: return (((b - a)*(b - a))/(2*n))*mch(1);
  }
}
