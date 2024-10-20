// Left-Center-Right.cpp
// This program's documentation is included seperately

#include "Player.h"
#include "Dice.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int main()
{
	// Initializing variables
	int numPlayers = 0;
	int currentTurn = 1;
	bool endCondition = false;
	srand(time(0));

	// Prints rules from .txt
	ifstream rules("rules.txt");
	if (rules)
	{
		string line;
		while (getline(rules, line))
		{
			cout << line << endl;
		}
		rules.close();
	}

	// Asking for number of players, making sure it is at least 3
	cout << "How many people will be playing?" << endl;
	while (numPlayers < 3)
	{
		cout << "There must be at least 3 players." << endl;
		cin >> numPlayers;
	}

	// Instantiating players into a vector
	vector<Player> players;
	Player p;
	Dice dice;
	for (int i = 0; i <= numPlayers; i++)
	{
		players.push_back(p);
	}
	// Setting players to left and right of each player, if there are x players, player x's right wouldn't be player x+1, it would be player 1
	for (int i = 1; i <= numPlayers; i++)
	{
		players[i].setPlayerLeft((i - 1 == 0) ? numPlayers : i - 1);
		players[i].setPlayerRight((i + 1 > numPlayers) ? 1 : i + 1);
	}

	// Main game loop; Each loop is one player's turn
	int chips = players[currentTurn].getChips(); // Initializes integer chips to ensure entry at if (chips != 0)
	while (endCondition == false)
	{
		if (chips != 0)
		{
			// Clear screen for each turn, and sets the players beside the current player (saves space later)
			system("cls");
			int playerLeft = players[currentTurn].getPlayerLeft();
			int playerRight = players[currentTurn].getPlayerRight();

			// Setting amount of rolls player will take; 3 if player has 3 or more chips; otherwise, how many chips the player has
			int rolls = (players[currentTurn].getChips() >= 3 ? 3 : players[currentTurn].getChips());
			cout << "It is player " << currentTurn << "'s turn. " << endl;						// Prints turn number
			cout << "You have " << players[currentTurn].getChips() << " chips" << endl << endl;	// Prints chips left

			// Loop for rolls; Loops through for however many rolls were decided earlier
			for (int i = 1; i <= rolls; i++)
			{
				// Gets player's chips in case it is not first roll; States the roll number of turn
				chips = players[currentTurn].getChips();
				cout << "This is roll " << i << " of " << rolls << " rolls." << endl;

				// Waits for input to roll the die
				cout << "Press enter to roll" << endl << endl;
				char die = dice.rollDie();
				cin.ignore();
				cin.get();

				// Prints roll; decision tree depending on the roll
				// C, L, and R remove chip from current player, L and R add that chip to player on left or right, and * does nothing
				// Uses playerLeft and playerRight variables so that the getters are used once, and saves space 
				cout << "You rolled a " << die << endl;
				if (die == 'C')
				{
					players[currentTurn].setChips(chips - 1);
					cout << "So you pass a chip to the center" << endl;
				}
				else if (die == 'L')
				{
					players[currentTurn].setChips(chips - 1);
					cout << "So you pass a chip to the player to the left, " << playerLeft << endl;
					players[playerLeft].setChips(players[playerLeft].getChips() + 1); //gets left players chips, adds 1, set chips to value
				}
				else if (die == 'R')
				{
					players[currentTurn].setChips(chips - 1);
					cout << "So you pass a chip to the player to the right, " << playerRight << endl;
					players[playerRight].setChips(players[playerRight].getChips() + 1);	//gets right players chips, adds 1, set chips to value
				}
				else if (die == '*')
				{
					cout << "So you do nothing" << endl;
				}
				cout << "You still have " << players[currentTurn].getChips() << " chips" << endl << endl << endl; // Prints chips left

			}
		}

		// End game condition
		// Checks each player's chips, if it is zero, add to counter integer, out
		int out = 0;
		for (int i = 1; i <= numPlayers; i++)
		{
			if (players[i].getChips() == 0)
			{
				out++;
			}
		}
		// If out is equal to or one less than the number of players, it checks which player still has chips, prints them as the winner, breaks game loop on next input
		if (out == numPlayers || out == numPlayers - 1)
		{
			for (int i = 1; i <= numPlayers; i++) // Who is the winner?
			{
				if (players[i].getChips() > 0)
				{
					cout << "Player " << i << " wins!" << endl;
				}
			}
			cin.get();
			break;
		}

		// Going to next player
		// Increments turn number and if it is more than number of players, the turn number should actually be one; waits for input
		currentTurn++;
		if (currentTurn > numPlayers)
		{
			currentTurn = 1;
		}
		cout << "Press enter to go to the next player" << endl;
		cin.get();
	}
}