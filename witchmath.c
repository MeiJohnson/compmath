#include<stdlib.h>
#include<stdio.h>
#include<locale.h>
#include<math.h>

double a, b;
int n;

double rectL(double h);
double rectR(double h);
double trap(double h);
double simpson(double h);
void mainMenu();
void secondMenu();
void thirdMenu();
void submenu();
void firstAlg();
void secondAlg();
int getValue(int count);
void firstM();
void clear_screen();

int main() {
    char *locale = setlocale(LC_ALL, "");

    printf("Enter a,b:\n");
    scanf("%lf %lf", &a, &b);
    printf("Enter n:\n");
    scanf("%d", &n);

    mainMenu();

    return 0;

}

void clear_screen()
{
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
            double I = rectL(step);
            printf("Definite integral %lf\n", I);
            submenu();
            break;
        }
        case 2:
        {
            double I = rectR(step);
            printf("Definite integral %lf\n", I);
            submenu();
            break;
        }
        case 3:
        {
            double I = trap(step);
            printf("Definite integral %lf\n", I);
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
    printf("2. Second algorithm(WiP)\n");
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

    while (scanf("%d", &value) != 1 || value < 1 || value > count) {
        printf("Incorrect input. Try again: ");
        //scanf_s("%d", &value);
    }

    return value;
}

double rectL(double h) {
    double s = 0, x;
    x = a;
    while (x <= (b - h)) {
        s += 1 / (x + 5);
        x += h;
    }
    double I = h * s;
    double R = (((b - a)*(b - a))/2*n);
    return I;
}

double rectR(double h) {

    double s = 0, x;

    x = a + h;

    while (x <= b)
    {
        s += 1 / (x + 5);
        x += h;
    }
    double I = h * s;
    return I;
}

double trap(double h) {

    double s = (1 / (a + 5) + 1 / (b + 5)) / 2;
    double x = a + h;
    while (x <= (b - h))
    {
        s += 1 / (x + 5);
        x = x + h;
    }
    double I = h * s;
    return I;
}

double simpson(double h) {

    double s = (1 / (a + 5) + 1 / (b + 5)), s1 = 0, s2 = 0;
    double x = a + h;

    while (x <= (b - h))
    {
        s1 += 1 / (x + 5);
        x = x + 2 * h;
    };

    x = a + 2 * h;

    while (x <= (b - 2 * h))
    {
        s2 += 1 / (x + 5);
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
}

void firstM(){

}
