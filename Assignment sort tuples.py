# tuple workshop : calculate average score

students =('Ksb','Dang','Nan','John','Jkob','Phu','Mimi')
scores   =(15,12,18,20,17,19,16)


total = sum(scores)
numStudent = len(scores)
avg = total/numStudent

i = 0
for std in students:
    print('{}{} => {}'.format(i+1,std,scores[i]))
    i += 1

print('-----------')
print('Total Students:',numStudent)
print('Avg score=',avg)
print('Max score=',max(scores))
print('Min score=',min(scores))
print('-----------')
