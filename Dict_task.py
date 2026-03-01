#task 2
original = {'a': 1, 'b': 2, 'c': 3}
swapp={}
for key,value in original.items():
    swapp[value]=key
print(swapp)

#task 1
data = [1, 2, 2, 3, 4, 4, 4, 5]
freak={}
for item in data:
    if item in freak:
        freak[item]+=1
    else:
        freak[item]=1
print(freak)

#task 3

scores = {'Alice': 88, 'Bob': 95, 'Charlie': 70}
max_score=max(scores,key=scores.get)
print(max_score)

#task 4
unsorted = {'apple': 5, 'banana': 2, 'cherry': 7}
sort_order=dict(sorted(unsorted.items(),key=lambda item :item[1]))
print(sort_order)