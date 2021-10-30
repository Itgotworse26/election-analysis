counties = ["Arapahoe", "Denver", "Jefferson"]
counties_tuple = ("Arapahoe","Denver","Jefferson")
counties_dict = {}
voting_data = []

counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438

voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

# my_votes = int(input("How many votes did you get in the election? "))

# total_votes = int(input("What is the total votes in the election? "))

# print(f"I received {my_votes / total_votes * 100}% of the total votes.")

# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)