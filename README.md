# Homework for Week 6
_(Scroll down for some reminder on cloning this repository and making commits)_

Remember the Rock-Paper-Scissor game?
- Rock beats scissors
- Scissors beats paper
- Paper beats rock

 The `main.py` file has some code which is prepared for this game. The game is played against the computer (or the program) which should be running like the following:
1. The program asks for user's name 
2. Then decides for either `rock`, `paper` or `scissor` randomly for itself
3. Then asks for user's choice
4. Decides who is the winner for the current round
5. The score increases by `one` for the winner of the current round
6. The game ends, when one of the players reaches a score higher than 3

However, the code is not working as expected, there are some bugs in it. 🐛  Which is completely normal! To be more clear, the output should be something like this: 
```
What's your name?
Harika
Harika, do yo want to choose rock, paper or scissors?
rock
Computer chose paper
Harika chose rock
Paper wins!
Computer won this round!
Scores
Computer:1
Harika:0
Harika, do yo want to choose rock, paper or scissors?
rock
Computer chose paper
Harika chose rock
Paper wins!
Computer won this round!
Scores
Computer:2
Harika:0
Harika, do yo want to choose rock, paper or scissors?
paper
Computer chose rock
Harika chose paper
Paper wins!
Harika won this round!
Scores
Computer:2
Harika:1
Harika, do yo want to choose rock, paper or scissors?
scissors
Computer chose paper
Harika chose scissors
Scissors win!
Harika won this round!
Scores
Computer:2
Harika:2
Harika, do yo want to choose rock, paper or scissors?
paper
Computer chose paper
Harika chose paper
It's a tie!
Scores
Computer:2
Harika:2
Harika, do yo want to choose rock, paper or scissors?
paper
Computer chose paper
Harika chose paper
It's a tie!
Scores
Computer:2
Harika:2
Harika, do yo want to choose rock, paper or scissors?
paper
Computer chose scissors
Harika chose paper
Scissors win!
Computer won this round!
Scores
Computer:3
Harika:2
```


### Task 1
Your task is to find those bugs and try to make the program work as expected. 

### Task 2
Although the program shows the scores along the way (or it's supposed to show), it doesn't tell who won the game at the end. Display the winner at the end of the game. 

### Task 3
If you've come this far, congratulations! 🎉 Now, please commit and push your current version of the program. Because, we are about to change the logic and we also don't want to lose your current progress. If you are not sure how to do commit and push, please get help from the teachers. 

Anyways, let's say we want to now change the logic, and instead of stopping the program when a player reaches the score of 3, we want to run it only 5 rounds and decide the winner of the game by looking at the scores then. Whoever has the higher score, he/she is the winner. (HINT: you need a new variable to keep track of the number of rounds)



--------------------------------------
## Bonus Exercise:
Write a program that asks the user input for a string and then creates a counter dictionary which holds the number of characters for each character. Print this dictionary at the end. 

Example: 
User input: 
```
hello
```
Program output: 
```js
{'h': 1, 'e': 1, 'l': 2, 'o': 1}
```
Because there is one `h`, one `e`, one `o` and two `l`s in "`hello`".

Another example:
User input:
```
redi school is awesome
```
Program output:
```js
{'r': 1, 'e': 3, 'd': 1, 'i': 2, ' ': 3, 's': 3, 'c': 1, 'h': 1, 'o': 3, 'l': 1, 'a': 1, 'w': 1, 'm': 1}
```

---------------------------------------
### What you need to do to publish your code
1. Download (clone) this repository to your computer by clicking on Code, copying the URL from there and then putting the following command in VSCode terminal: `git clone {url_you_copied}`
3. Open it in VSCode
4. Open the `main.py` file
5. Edit the file (instructions are directly in the file)
6. Push your changes to GitHub

### Hint: pushing changes to GitHub
- Click on the Git button in VSCode  
![git-button](https://user-images.githubusercontent.com/20370225/132511360-8d934539-2eba-4714-b006-38a308c3caf9.png)
- Prepare (=stage) any changes you want to commit with the + button next to the file name  
![change](https://user-images.githubusercontent.com/20370225/132511457-cb0b0f6e-4f73-41c4-8fca-d9eebed764b7.png)
- Add a commit message  
![image](https://user-images.githubusercontent.com/20370225/132511610-d753a5a9-9085-4807-9214-7ece0bee8633.png)
- Click the ✅ button to commit your changes  
![image](https://user-images.githubusercontent.com/20370225/132511856-b6acea15-0750-46f2-96c7-54121f8327f9.png)
- Click on the icon in the bottom left part of VSCode to push your changes to GitHub (will look like either of the images below)  
![image](https://user-images.githubusercontent.com/20370225/132512016-56f3d964-5b6d-4cf2-a915-62f5632179ed.png)
![image](https://user-images.githubusercontent.com/20370225/132512288-b5b0827c-14f7-48cb-a87e-0419d75dab9c.png)





