#include <iostream>
using namespace std;

// Function to print the Tic Tac Toe board
void printBoard(char board[]) {
    cout << " " << board[0] << " | " << board[1] << " | " << board[2] << endl;
    cout << "-----------" << endl;
    cout << " " << board[3] << " | " << board[4] << " | " << board[5] << endl;
    cout << "-----------" << endl;
    cout << " " << board[6] << " | " << board[7] << " | " << board[8] << endl;
}

// Function to check if the game has been won
bool checkWin(char board[], char mark) {
    return ((board[0] == mark && board[1] == mark && board[2] == mark) ||
            (board[3] == mark && board[4] == mark && board[5] == mark) ||
            (board[6] == mark && board[7] == mark && board[8] == mark) ||
            (board[0] == mark && board[3] == mark && board[6] == mark) ||
            (board[1] == mark && board[4] == mark && board[7] == mark) ||
            (board[2] == mark && board[5] == mark && board[8] == mark) ||
            (board[0] == mark && board[4] == mark && board[8] == mark) ||
            (board[2] == mark && board[4] == mark && board[6] == mark));
}

int main() {
    char board[9] = {'1', '2', '3', '4', '5', '6', '7', '8', '9'};
    int player = 1;
    int choice;
    bool draw = false;

    do {
        printBoard(board);

        // Get player's move
        if (player % 2 == 1) {
            cout << "Player 1, enter a number: ";
        } else {
            cout << "Player 2, enter a number: ";
        }
        cin >> choice;

        char mark = (player % 2 == 1) ? 'X' : 'O';

        // Update the board
        if (choice >= 1 && choice <= 9 && board[choice - 1] != 'X' && board[choice - 1] != 'O') {
            board[choice - 1] = mark;
            player++;
        } else {
            cout << "Invalid move. Please try again." << endl;
        }

        // Check for a win or a draw
        if (checkWin(board, 'X')) {
            printBoard(board);
            cout << "Player 1 wins!" << endl;
            break;
        } else if (checkWin(board, 'O')) {
            printBoard(board);
            cout << "Player 2 wins!" << endl;
            break;
        } else if (player > 9) {
            draw = true;
            break;
        }
    } while (!draw);

    if (draw) {
        printBoard(board);
        cout << "It's a draw!" << endl;
    }

    return 0;
}
