ASSIGNMENT 4 : Depth limited minimax with alpha-beta pruning

NAME: Rahul Myneni
UTA ID: 1001678634
LANGUAGE: Python
CODE STRUCTURE:
	The class minimax performs the decision making. Contains methods decision() which returns minimax's decision, 
	maximumValue() which performs maximizing operations, 
	minimumValue() which perfoms minimizing operations, 
	utility() which returns the utility that needs to be maximized or minimized.
	result() calculates the new state after a particular move
	availablemoves() returns the moves that are possible on a state

COMPILATION AND EXECUTION:
	To run the code, execute maxconnect4.py with standard python compilation commands (works on omega)

	For interactive mode:
		python maxconnect4.py interactive [input_file] [computer-next/human-next] [depth]

	For one-move mode:
		python maxconnect4.py one-move [input_file] [output_file] [depth]	

TOURNAMENT:
	Yes, the program has depth limted and alpha-beta implemented and can be entered into the tournament