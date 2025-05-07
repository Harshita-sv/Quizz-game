# to find palindrome
# def is_palindrome(a):
#     cleaned= a.replace(" ", "").lower()
#     return cleaned== cleaned[::-1]
# a= input("Enter a name")
# palin=is_palindrome(a)
# print(f"The name that you have given is a palindome: {palin}")

# def fact(n):
#     product=1
#     for i in range(1,n+1):
        
#         product*=i
#     return product

# n=int(input("Enter a number"))
# print(fact(n))
# def fact(n):
#     sum=0

#     for i in range(1,n+1):
#         sum +=i
#     return sum
# print(fact(5))
def fact(n):
    sum=0
    i=1
    while i<=n:
        sum+=i
        i+=1
    return sum
print(fact(3))            
    




# def second_largest(numbers):
#     largest = second = float('-inf')  # very small number
#     for num in numbers:
#         if num > largest:
#             second = largest
#             largest = num
#         elif num > second and num != largest:
#             second = num
#     return second



# # Example
# print(second_largest([10, 20, 40, 30]))  # Output: 30


# def rev_list(lst):
#     return lst[::-1]
# user_input=input("Enter numbers seperates by spaces: ")
# user_list= list(map(int, user_input.split()))
# print(rev_list(user_list))

# def factorial(n):
#     if n==1 or n==0:
#         return 1
#     return n* factorial(n-1)
# print(factorial(3))


 