message = "Hello"



file_name = "../data/hello.txt"

# "\r\n" Windows
# "\n" Linux Mac

f = open(file_name, "a")
f.write(message + "\n")
f.close()

# 参考元 https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q1348964283