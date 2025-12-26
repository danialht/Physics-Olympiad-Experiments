#include <iostream>
#include <time.h>
#include <string>
#include <stdlib.h>
#include <math.h>
#include <iomanip>
#include "answers.hpp"

using namespace std;

void getInput(double * const heightPtr, double * const massPtr) {

    while (true)
    {
        cout << "Enter a height in meters between 0.00 and 10.00." << endl;
        cin >> *heightPtr;
        if(*heightPtr >= 0.0 && *heightPtr <= 10.0) break;
        else cout << "Invalid height." << endl;
    }
    
    while (true)
    {
        cout << "Enter a mass in kg between 0.10 and 5.00." << endl;
        cin >> *massPtr;
        if(*massPtr >= 0.1 && *massPtr <= 5.0) break;
        else cout << "Invalid mass." << endl;
    }
}

double applyNewtonMethod(const double constant) {
    // solves this equation numerically to 8 decimal places: 
    // constant = x + exp(-x) - 1
    double answer = 1.0;
    double answerCopy = 0;
    while (answer - answerCopy > 1E-8)
    {
        answerCopy = answer;
        answer = (constant + 1 - (answer + 1) * exp(-answer)) / (1 - exp(-answer));
    }
    return answer;
}

void generateAnswer(const double height, const double mass) {

    double heightCoefficient = height * pow(gamma(mass), 2) / g;
    double gammaTimesT = applyNewtonMethod(heightCoefficient);
    double fallTime = gammaTimesT / gamma(mass);
    //generate random statistical error
    double randomNoise = (double)(rand() % 20 - 10) / 100000;
    fallTime += randomNoise;
    cout << "Fall time: ";
    cout << fixed << setprecision(5) << fallTime;
    cout << " secs." << endl;
}

bool testingIsFinished() {

    cout << "If you want to exit, type EXIT and press enter, otherwise press any key then enter." << endl;
    string command;
    string keywordStr = "EXIT";
    cin >> command;
    if(command.compare(keywordStr) == 0) return true;
    return false;
}

int main() {

    srand(time(NULL));
    double heightInput;
    double massInput;
    while(true)
    {
        getInput(&heightInput,&massInput);
        generateAnswer(heightInput,massInput);
        if(testingIsFinished()) break;
    }
    return 0;
}
