import math, time
primelist = []
def prime(n):
    y = math.ceil(math.sqrt(n))
    for x in range(2, n+1):
		    for i in range(2, y+1):
			    if i != x and x % i == 0:
				    break
		    else:
		        primelist.append(x)

start = time.time()
prime(100)
end = time.time()
print(end - start)
print(primelist)
