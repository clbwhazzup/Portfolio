#include "Dice.h"

Dice::Dice()
{
	die = 0;
}
char Dice::rollDie()			// Rolls a die using rand function, and returns die result.
{
	die = 1 + (rand() % 6);		// 1 + sets the range up one, with min value being 1, and % 6 sets max value to 6.
	if (die >= 4 && die <= 6)	// Converts to character accordingly
	{
		return '*';
	}
	else if (die == 1)
	{
		return 'L';
	}
	else if (die == 2)
	{
		return 'R';
	}
	else if (die == 3)
	{
		return 'C';
	}
}