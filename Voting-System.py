print('''
Welcome, Voters!
You can vote for your favorite candidate.
The nominees are:
1. Donald Trump
2. Kamala Harris
''')

candidate1 = "Donald Trump"
candidate2 = "Kamala Harris"
candidate1_count = 0
candidate2_count = 0

voters = [101, 102, 103, 104, 105]  # List of registered voters
voted = []  # List to store voters who have already voted

while True:
    voter_id = input("Enter your Voter ID number: ")

    if voter_id.isdigit():
        voter_id = int(voter_id)

        if voter_id in voted:
            print("You have already voted.")
        elif voter_id in voters:
            print("You are eligible to vote.")

            # Keep asking until the user enters a valid vote (1 or 2)
            while True:
                vote = input("Enter 1 for Donald Trump or 2 for Kamala Harris: ")
                if vote == "1":
                    print("You have voted for Donald Trump.")
                    candidate1_count += 1
                    break
                elif vote == "2":
                    print("You have voted for Kamala Harris.")
                    candidate2_count += 1
                    break
                else:
                    print("Invalid choice. Please enter 1 or 2.")

            voted.append(voter_id)  # Mark voter as voted
        else:
            print("You are not eligible to vote.")
    else:
        print("Invalid input. Please enter a numeric Voter ID.")

    # Check if all registered voters have voted
    if len(voted) == len(voters):
        print("\nAll voters have voted. Counting votes...")

        if candidate1_count > candidate2_count:
            print(f"{candidate1} wins with {candidate1_count} votes!")
        elif candidate2_count > candidate1_count:
            print(f"{candidate2} wins with {candidate2_count} votes!")
        else:
            print("It's a tie!")

        break  # Exit the loop after vote counting
