#include "Player.h"
#include <iostream>
using namespace std;

//Constructor
Player::Player(int c, int l, int r)
{
	chips = c;
	playerLeft = l;
	playerRight = r;
}

// Setters
void Player::setPlayerLeft(int i)
{
	playerLeft = i;
}
void Player::setPlayerRight(int i)
{
	playerRight = i;
}
void Player::setChips(int i)
{
	chips = i;
}

//Getters
int Player::getPlayerLeft()
{
	return playerLeft;
}
int Player::getPlayerRight()
{
	return playerRight;
}
int Player::getChips()
{
	return chips;
}