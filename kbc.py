from hashlib import new
import random
from questions import QUESTIONS


def isAnswerCorrect(question, answer):
    '''
    :param question: question (Type JSON)
    :param answer:   user's choice for the answer (Type INT)
    :return:
        True if the answer is correct
        False if the answer is incorrect
    '''
    corr_ans = question["answer"]
    return True if answer == corr_ans else False      # do not remove this


def lifeLine(ques):
    '''
    :param ques: The question for which the lifeline is asked for. (Type JSON)
    :return: delete the key for two incorrect options and return the new ques value. (Type JSON)
    '''
    op = [1,2,3,4]
    ansop = ques['answer']
    op.remove(ansop)
    finop=[]
    finop.append(ansop)
    finop.append(random.choice(op))
    return finop

# def printOptions(options,rounds):
#     for o in options:
#             print(f'\t\t\tOption {o}: {QUESTIONS[rounds][f"option{o}"]}')

def kbc():
    '''
        Rules to play KBC:
        * The user will have 15 rounds
        * In each round, user will get a question
        * For each question, there are 4 choices out of which ONLY one is correct.
        * Prompt the user for input of Correct Option number and give feedback about right or wrong.
        * Each correct answer get the user money corresponding to the question and displays the next question.
        * If the user is:
            1. below questions number 5, then the minimum amount rewarded is Rs. 0 (zero)
            2. As he correctly answers question number 5, the minimum reward becomes Rs. 10,000 (First level)
            3. As he correctly answers question number 11, the minimum reward becomes Rs. 3,20,000 (Second Level)
        * If the answer is wrong, then the user will return with the minimum reward.
        * If the user inputs "lifeline" (case insensitive) as input, then hide two incorrect options and
            prompt again for the input of answer.
        * NOTE:
            50-50 lifeline can be used ONLY ONCE.
            There is no option of lifeline for the last question( ques no. 15 ), even if the user has not used it before.
        * If the user inputs "quit" (case insensitive) as input, then user returns with the amount he has won until now,
            instead of the minimum amount.
    '''
    #  Display a welcome message only once to the user at the start of the game.
    #  For each question, display the prize won until now and available life line.
    # For now, the below code works for only one question without LIFE-LINE and QUIT checks
    rounds=0
    curr_prize = 0
    quitGame = 0
    validans='1 2 3 4 quit lifeline'
    options = [1,2,3,4]
    llOptions=[]
    ll = 0
    isllavail = 1
    while rounds < 15:
        print(f'\tQuestion {rounds+1}: {QUESTIONS[rounds]["name"]}' )
        print(f'\t\tOptions:')
        if ll == 1:
            ll -=1
            for o in llOptions:
                print(f'\t\t\tOption {o}: {QUESTIONS[rounds][f"option{o}"]}')
        else:
            for o in options:
                print(f'\t\t\tOption {o}: {QUESTIONS[rounds][f"option{o}"]}')
        print("\nAvailable Lifeline:\t",isllavail)
        ans = input('Your choice ( 1-4 ) or "quit" to Quit : ')
        ansindx = QUESTIONS[rounds]["answer"]
        
        if ans not in validans:
            print("Invalid Answer, Enter Valid Choice\nValid Options:(1-4)\n'quit' to Quit")
            ans = input('Enter Valid choice ( 1-4 ) or "quit" to Quit : ')
        # check for the input validations

        if ans == 'lifeline' and rounds != 14 and ll==False and isllavail != 0:
            ll += 1
            isllavail -= 1
            llOptions = lifeLine(QUESTIONS[rounds])
            continue
        elif ans=='lifeline' and rounds==14:
            print("\nCan not use lifeline on this round!\n")
            continue
        elif ans=='lifeline' and isllavail == 0:
            print("\nSorry, you've already used a lifeline!\n")
            continue

        if ans == 'quit':
            quitGame = 1
            break
        
        if isAnswerCorrect(QUESTIONS[rounds], int(ans) ):
            curr_prize = QUESTIONS[rounds]["money"]
            print('\nCorrect Answer!')
            # print the total money won.
            print("Current Prize Amount: ",QUESTIONS[rounds]["money"])
            # See if the user has crossed a level, print that if yes
            print("Rounds Cleared: ", rounds+1)

        else:
            # end the game now.
            # also print the correct answer
            print('\nIncorrect Answer!\nThe Correct Answer is:',QUESTIONS[rounds][f"option{ansindx}"])
            break
        rounds +=1

    # print the total money won in the end.
    if quitGame == 0:
        prize=0
        print("Rounds Played:",rounds+1)
        if rounds < 5:
                prize = 0
        elif rounds < 11 and rounds >= 5:
            prize = 10000 
        elif rounds > 10:
            prize = max(320000, curr_prize)
        print("Your Prize:",prize)
    elif quitGame == 1:
        print("Rounds Played:",rounds+1)
        print("Your Prize:",curr_prize)

kbc()