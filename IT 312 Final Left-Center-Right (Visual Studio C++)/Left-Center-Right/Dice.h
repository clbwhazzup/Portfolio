#pragma once
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

class Dice
{
private:
	int die;
public:
	Dice();
	char rollDie();
};