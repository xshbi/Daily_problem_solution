#include <iostream>
using namespace std;

int main() {
    const int size = 5; // Change the size as needed
    int numbers[size];

    // Input: Assume you have an array of numbers
    cout << "Enter " << size << " integers: ";
    for (int i = 0; i < size; ++i) {
        cin >> numbers[i];
    }

    int divisor; // The integer to divide by
    cout << "Enter the divisor: ";
    cin >> divisor;

    // Divide each element by the divisor
    for (int i = 0; i < size; ++i) {
        numbers[i] /= divisor;
    }

    // Display the updated array
    cout << "Updated array elements: ";
    for (int i = 0; i < size; ++i) {
        cout << numbers[i] << " ";
    }

    return 0;
}
