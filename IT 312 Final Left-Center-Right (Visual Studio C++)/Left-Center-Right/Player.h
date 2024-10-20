#pragma once

class Player
{
private:
	int chips;
	int playerLeft;
	int playerRight;
public:
	Player(int c = 3, int l = 0, int r = 0);
	void setPlayerLeft(int i);
	void setPlayerRight(int i);
	void setChips(int i);
	int getPlayerLeft();
	int getPlayerRight();
	int getChips();
};