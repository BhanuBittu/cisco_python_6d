def find_salaries_sum(first, second, **named_salaries):
    result = first + second 
    for keyword in named_salaries:
        result += named_salaries[keyword] 
    return result 

print(find_salaries_sum(first=1000,second=2000))
print(find_salaries_sum(first=1000,second=2000,third=3000))
print(find_salaries_sum(first=1000,second=2000,third=3000,fourth=4000))

def find_salaries_bonus(first, second, bonus=500):
    return first + second + bonus

print(find_salaries_bonus(first=1000,second=2000))
print(find_salaries_bonus(first=1000,second=2000,bonus=100))