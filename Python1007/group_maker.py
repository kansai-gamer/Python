names = ["Alice", "Alex", "Andy", "Abel", "Albert",
        "Betty", "Bob", "Bella", "Billie", "Benn",
        "Carol", "Connie", "Crysta", "Clara", "Cyndy",
        "Daniel", "David", "Denny", "Diana"]

group_count = int(input("Group Count: "))
member_count = len(names)
group_member_count = int(member_count / group_count)
rest_member = (member_count % group_count)

print("Member Count:", member_count)
print("Group Member Count:", group_member_count)
print("Rest Member Count:", rest_member)