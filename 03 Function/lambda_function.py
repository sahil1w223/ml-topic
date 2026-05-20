# basic syntax lambda arguments : expression

val = [lambda x: x**2]
sum = lambda a,b: a + b
for f in val:
    print(f(2)) # This will print 4 five times, because each lambda function captures the same variable 'x' which has the value 4 after the loop ends.

print(sum(2,4)) # This will print 6, as the lambda function takes two arguments 'a' and 'b', adds them together, and returns the result.