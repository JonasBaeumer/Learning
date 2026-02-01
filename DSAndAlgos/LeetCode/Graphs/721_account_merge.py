"""
Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.
"""

"""
Approach: 
	- We have our list linking all the accounts.
	- We can then use Union-Find to merge the sets of each account together
	- After all the connected components we can then go over all suncomponents and build our merged list

Questions / Challenges: 
	- How to I keep a running register of all mails that belong to one account?
		Idea: I could keep the root nodes list as alternable, e.g. when I add
			a new node to my subcomponents I will add the mails to my root node list 
	- How do I model edges in between this graph? Do I first need to manually create them and then add
	them?
		- How do I transform the input to somehow mirror the graph?
"""

"""
New approach: Rather than using the accounts I will work directlz with the emails and link them back to the accounts
This should make it much easier while also helping to create any difficult account edges mapping which would be 
quite expensive (O(n^2) just for creating the edges). 
If I instead stay with the mail mappings I just need O(# number of total emails) to create all the edges
While I do that I also need to create two dict mappings
Mails -> UF Ids (so I know which email is in which UF field when I run UF)
Mails -> Account name (map mail to account name were it is first seen)
"""

test_accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]

def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
	n = len(accounts)
	number_of_mails = 0

	# Create mapping between mails and ids
	mails_to_ids = {}

	# Create mapping between mails and account namems
	mails_to_names = {}	
	
	# Fill up both maps while going through each email list
	for account in accounts:
		# Go through all mails and check if they are already mapped in mail_to_ids
		for i in range(1:len(account)):
			if account[i] not in mails_to_ids:
				mails_to_ids[account[i]] = number_of_mails
				number_of_mails += 1
			if account[i] not in mails_to_names:
				mails_to_names[account[i]] = account[0]
		# Number of mails will give us which ID in UF field can be used for new mail when its added
		# Then also check if mail is already added in mails_to_names

	print(mails_to_ids)
	print(mails_to_names)

	parent = list(range(n))
	
	def find(x: int) -> int:
		if parent[x] != x:
			parent[x] = find(parent[x])
		return parent[x]

	def find_connected_account(account: list[list[str]]):
		for acc in accounts:
			if acc != account:
				for i in range(1, len(account)):
					

	for account in accounts:
		# If not in network -> Add all the mails to our root node
		
