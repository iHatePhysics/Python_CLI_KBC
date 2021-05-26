 
# Welcome to Kaun Banega Crorepati

I have coded Kaun Banega Crorepati. The idea behind is to make myselves familiar with python language.This is my first project. 
  
  It's like a quiz game where there will be 15 questions asked from user. Every question has one correct answer. They can also go for lifelines. At the end you will display the results how much the user earned. Perform following tasks to complete the game.
  
### SETUP THE GAME CODE.

  *  Install git
  * `github.com/iHatePhysics/cli-kbc-game.git`
  * `python kbc.py` (to run code, you would be using python3) 

---
### ( Complete kbc function ):
  ### (How to Play)
  * after cloning the code, cd to the kbc directory and run the code using "python kbc.py"

  ### (MINIMUM REWARD ACCORDING TO THE Level(Padaav))
  If the user is:
  * below questions number 6, then the minimum amount rewarded is Rs. 0 (zero)
  * As he correctly answers question number 5, the minimum reward becomes Rs. 10,000 (First Level)
  * As he correctly answers question number 10, the minimum reward becomes Rs. 3,20,000 (Second Level)

  ### (LIFELINE)

  There is a 50-50 life-line where two incorrect options get disappeared

  * 50-50 lifeline can be used ONLY ONCE.
  * There is no option of lifeline for the last question( ques no. 15 ), even if the user has not used it before.
  
  ### (QUIT)
  
  If the user inputs "quit" (case insensitive) as input, then user returns with the amount he/she has won until now,
	instead of the minimum amount.