from .. import stats

def report(*args):
    print("SUM:", sum(args))
    print("CNT:", len(args))
    print("MEAN:", sum(args) / len(args))