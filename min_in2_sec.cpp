#include <iostream>
using namespace std;

void Convert(int value, int &hour, int &minute, int &seconds) {
    hour = value / 3600;           // Hour component
    minute = (value % 3600) / 60;  // Minute component
    seconds = value % 60;          // Second component
}

int main() {
    int hour;
    int seconds;
    int Seconds_To_Convert = 5432; // User-specified seconds

    // Calling Convert function
    Convert(Seconds_To_Convert, hour, minute, seconds);

    // Display the result
    cout << hour << " hours and " << minute << " minutes and " << seconds << " seconds";
    return 0;
}
