# scramble
Practical exam for FP

The task is getting a random string from a line in a file, scramble it randomly leaving the first and last letter from a word unchanged (so from <b><u>s</u>crambl<u>e</u></b>, you may get <b><u>s</u>bmcrla<u>e</u></b>, and from <b><u>s</u>cr<u>a</u> <u>m</u>bl<u>e</u></b>, you may get <b><u>s</u>bc<u>a</u> <u>m</u>lr<u>e</u></b> because changing letters from different words is valid).

The command from the user looks like: <b>swap <word1> <letter1> - <word2> <letter2>< /b> . 

Score is calculated from the random selected word from taking the number of total characters minus the spaces.

Undo works for only one operation and leaves the score unchanged.

Game ends when the score is 0, <b>the player loses</b>, or players gets the original word right, <b>player wins and score is printed</b>.
