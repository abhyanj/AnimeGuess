#anime guessing game
import pandas as pd
import random
import numpy as np


whole= pd.read_csv('animes.csv') #whole entire anime csv (contains names, rank, reviews, avg score, etc...)
df = whole[['title', 'synopsis', 'popularity']].copy() #grab smaller dataframe with only names, popularity rank, and synopsis
df = df.sort_values('popularity') #sort by popularity since I'm only grabbing the top 500ish
df = df.drop_duplicates(subset=['title']) #had some duplicates with unique ids, so I removed them
df = df.head(500) # take only the first 500 values 
# print(df.tail(10)) 
df['synopsis'] = df['synopsis'].astype(str) 
df['title'] = df['title'].astype(str)
# print(df.dtypes) 
x = 0
while x < 500:
	
	originalSynop = df.iloc[x]['synopsis'] #grab the original synopsis
	synopTitle = df.iloc[x]['title'] #grab the corresponding title from that synopsis
	
	originalSynop = str(originalSynop) #turn this into a string
	synopTitle = str(synopTitle) #turn this into a string

	newSynop = originalSynop.replace(synopTitle, 'REDACTED') # everytime the title is mentioned in the synopsis, replace it with redacted
	df['synopsis'] = df['synopsis'].replace(originalSynop, newSynop)
	#df.at[x, 'synopsis'] = newSynop # set the synopsis at row x to the newSynop
	
	x+=1

def gameSetup():
	print("Guess the anime based on the synopsis (top 500 anime based on MAL popularity)! 10 Multiple choice questions!")
	print()
	score = 0
	i = 0
	while i < 10:
		choices = [0] * 4
		randArr = random.sample(range(1, 501), 4)

		randInt = randArr[0]
		randomSynop = df.iloc[randInt]['synopsis'] #grab a random synopsis 
		randomTitle = df.iloc[randInt]['title'] #grab the corresponding title from that synopsis
		choices[0] = randomTitle

		print(randomSynop)
		print()
		
		option2 = randArr[1]
		choices[1] = df.iloc[option2]['title'] 

		option3 = randArr[2]
		choices[2] = df.iloc[option3]['title'] 

		option4 = randArr[3]
		choices[3] = df.iloc[option4]['title'] 

		np.random.shuffle(choices)
		#display the 4 options (randomly) with 1,2,3,4
		print("1) ", choices[0], " 2) ", choices[1], " 3) ", choices[2]," 4) ", choices[3]) 

		
		#set the correct answer to one of the 4 options
		correctAnswer = str(choices.index(randomTitle) + 1)
		userResponse = input()
		if userResponse == correctAnswer:
			print("Correct!")
			score+=10
		elif userResponse == 'quit':
			quit()
		else:
			print("Nope!")
			print("The correct answer was", correctAnswer)

		i+=1
		print()

	print("That's the end! Your final score is: ", score)
	print("Would you like to play again? 1 for yes, enter anything else to exit")
	again = input()
	if again == '1':
		print()
		gameSetup()
	else:
		quit()


gameSetup()


