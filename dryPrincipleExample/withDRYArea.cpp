#include <iostream>
#include <cmath> // For mathematical functions like M_PI
using namespace std;

// Function to calculate area of rectangle
int calculateRectangleArea(int length, int width) {
    return length * width;
}

// Function to calculate area of square
int calculateSquareArea(int side) {
    return side * side;
}

// Function to calculate area of circle
double calculateCircleArea(double radius) {
    return M_PI * radius * radius; // M_PI is the value of π from <cmath>
}

int main() {
    // Output the area of different shapes
    cout << "Area of rectangle: " << calculateRectangleArea(5, 10) << endl;
    cout << "Area of square: " << calculateSquareArea(7) << endl;
    cout << "Area of circle: " << calculateCircleArea(4.5) << endl;
    
    return 0;
}
