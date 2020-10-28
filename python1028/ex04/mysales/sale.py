class Sale:
    def __init__(self, price, count):
        self.price = price
        self.count = count

    def calc(self):
        kotae = self.price * self.count
        return kotae

    def print(self):
        kekka = self.price * self.count
                    #↓カンマを入れる処理&出力
        return print("{:,}".format(kekka))

#参考元 https://www.yoheim.net/blog.php?q=20160404