
#include <iostream>
#include <chrono>

int main() {
    // Record the start time
    auto start = std::chrono::high_resolution_clock::now();
    long long c = 0;

    // Loop until 1 second has passed
    while (std::chrono::duration_cast<std::chrono::seconds>(std::chrono::high_resolution_clock::now() - start).count() < 1) {
        c++;
    }

    // Output the count
    std::cout << c << std::endl;
    return 0;
}