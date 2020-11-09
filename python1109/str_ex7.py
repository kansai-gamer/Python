names = ["Alice", "Batty", "Carol", "Daniel", "Ellen"]
target = "l"

names_in = [s for s in names if s.endswith(target)]
print(names_in)

# 参考元 https://note.nkmk.me/python-list-str-select-replace/