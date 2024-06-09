#include <iostream>
#include <random>
#include <ctime> // Include <ctime> for time(0) to seed the random number generator

int main() {
    int x;

    std::cout << "Give an input: ";
    std::cin >> x;

    // Define the range for the random number generation
    int lower_bound = 1;
    int upper_bound = 100;
    std::mt19937 gen(time(0)); // Seed the generator using time(0)
    std::uniform_int_distribution<> distr(lower_bound, upper_bound);

    // Generate a random number based on user input
    int random_number = distr(gen);

    std::cout << "Random number between " << lower_bound << " and " << upper_bound << ": " << random_number << std::endl;

    return 0;
}
