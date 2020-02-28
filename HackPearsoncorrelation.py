import math
def correlation_numerator(x,y,n):
    sum_xy=sum([a*b for a,b in zip(x,y)])
    sumX_sumY=sum(x)*sum(y)
    return (n*sum_xy)-(sumX_sumY)

def correlation_denominator(x,y,n):
    square_x=sum([a*b for a,b in zip(x,x)])
    total_sum_x=sum(x)*sum(x)
    square_y=sum([a*b for a,b in zip(y,y)])
    total_sum_y=sum(y)*sum(y)
    return (math.sqrt((n*square_x)-total_sum_x)*math.sqrt((n*square_y)-total_sum_y))

def pearson(num,denom):
    return num/denom
    
n = int(input())
mathematics = []
physics     = []
chemistry   = []
for i in range(n):
    elements = list(map(float, input().split()))
    mathematics.append(elements[0])
    physics.append(elements[1])
    chemistry.append(elements[2])

print('%.2f' % pearson(correlation_numerator(mathematics,physics,n), correlation_denominator(mathematics,physics,n)))   
print('%.2f' % pearson(correlation_numerator(physics,chemistry,n),correlation_denominator(physics,chemistry,n)))  
print('%.2f' % pearson(correlation_numerator(chemistry,mathematics,n),correlation_denominator(chemistry,mathematics,n)))   


