book_prices = {"Python Book": 3000, "HTML Book": 1000, "CSS Book": 2000}

for key, value in book_prices.items():
    print(key.ljust(len(max(book_prices))) + ":" + "{:,d}".format(value))

#参考元 https://note.nkmk.me/python-rjust-center-ljust/