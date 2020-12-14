import json
import numpy

class ScoreAnalyzer:

    def __init__(self,data):
        self.data = data

    def print_scores(self):
        #ハマったのでメモ
        #まずforを入れ子する、分からんから1つのfor文でやろうとしない
        for dates in self.data:
            for Processing_date in dates.values():
                #end=''をつければ改行なし、中に文字を入れたら一緒に出力してくれる
                print(Processing_date, end=' ')
            #こいつで改行
            print("")
    
    def print_total_score(self):
        total = 0
        for dates in self.data:
            #もう一度読むのも大事 https://github.com/murayama333/python2020/blob/master/01_basic/text/07_basic.md
            total += dates["math"] + dates["english"] + dates["science"]
        print("- total scores -")
        print(total)

    def print_scores_by_subject(self, subject, with_name=False):
        print("- scores by science -")
        for dates in self.data:
            if with_name:
                #self無くても行けるのを知らなくてハマった
                #まぐれの発見
                print(dates["name"],dates[subject])
            else:
                print(dates[subject])


    def print_total_score_by_subject(self, subject):
        total = 0
        for dates in self.data:
            total += dates[subject]
        print("- total score by science -")
        print(total)

    def save(self, file_name):
        with open(file_name, "w") as f:
            json.dump(self.data, f, indent=4)

    @classmethod
    def load(cls, file_name):
        with open(file_name, "r") as f:
            data = json.load(f)
            return cls(data)


    def ave(self,subject):
        for dates in self.data:
            pass
        print("average")
        print(numpy.average(dates[subject]))

if __name__ == "__main__":
    scores = [
        {"name": "Andy", "math": 70, "english": 90, "science": 80},
        {"name": "Betty", "math": 80, "english": 90, "science": 100},
        {"name": "Carol", "math": 40, "english": 90, "science": 90},
        {"name": "Daniel", "math": 80, "english": 100, "science": 40},
        {"name": "Ellen", "math": 90, "english": 70, "science": 90},
    ]

score_analyzer = ScoreAnalyzer(scores)
score_analyzer.ave("math")


#最近配列使ってなかったからかなり時間かかったのは内緒