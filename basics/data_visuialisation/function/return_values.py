def sum_weights(first,second):
    sum_weight=first+second
    return sum_weight
def ave_weight(first,second):
    average_weight = (first+second) / 2
    return average_weight
def run():
    print("what is the weight of boop")
    first=float(input())
    print("what is the beep weight ")
    second=float(input())
    print("what whould you like to calculate(sum or avarage)")
    action=input()
    if (action=="sum"):
      answer=sum_weights(first,second)
      print("the sum of beep's and boop's weightis{:.2}".format(answer))
    elif(action=="avarage"):
      answer=ave_weight(first,second)
      print("the average of weights is{:.2f}".format(answer))
    else:
      print("i am not sure what whould you like to do")
run()


   