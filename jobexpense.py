
n=int(input())
expense=0

total_expenses=list(map(int, input().split()))
for total_expense in total_expenses:
    if total_expense < 0:
        expense+=abs(total_expense)

print(expense)
        