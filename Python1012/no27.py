names_list = [["Ellen", "Betty", "Diana"],
              ["Fox", "Helen", "Andy"],
              ["Ian", "Glen", "Carol"]]

i = 0

for names in names_list:
    for name in names:
        i = i + 1
        print(i,":",name)