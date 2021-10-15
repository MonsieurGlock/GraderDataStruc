

class TorKham:
	def __init__(self):
		self.words = []

	def restart(self):
		### Enter Your Code Here ###
		self.words.clear()
		print("game restarted")
		# return "game restarted"

	def play(self, word:str):
		### Enter Your Code Here ###
		for i in word:
			if i.split()[0] == 'P':
				if i.split()[1] not in self.words:
					# print(self.words)
					if self.words == []:
						self.words.append(i.split()[1])
						print("\'{}\' -> {}".format(i.split()[1],self.words))
					elif i.split()[1][0:1].upper() == self.words[-1][-2:-1].upper(): #Is it work?
						self.words.append(i.split()[1])
						print("\'{}\' -> {}".format(i.split()[1],self.words))
					else:
						print("\'{}\' -> game over".format(i.split()[1]))
						# print("\'{}\' is Invalid Input !!!".format(i))
				else: print("\'{}\' -> game over".format(i.split()[1]))
				
			elif i.split()[0] == 'R':
				self.restart()
			elif i.split()[0] == 'X':
				break
			else: 
				print("\'{}\' is Invalid Input !!!".format(i))
				break


        # if word not in self.words:
        
        # else: print("\'p {} \'is Invalid Input !!!".format(word))
        
		# return "game over"

# *** TorKham HanSaa ***
# Enter Input : P Apple,P LEMON,R,P onion,X
# 'Apple' -> ['Apple']
# 'LEMON' -> ['Apple', 'LEMON']
# game restarted
# 'onion' -> ['onion']

torkham = TorKham()
print("*** TorKham HanSaa ***")

S = input("Enter Input : ").split(',')

torkham.play(S)
# print(S[0])
# print(S[0].split()[0] , S[0].split()[1])
 ### Enter Your Code Here ###






