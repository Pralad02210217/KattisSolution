day, month = map(int, input().split())

daysInMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = 0

for i in range(1, month):
    days += daysInMonth[i]

currentDate = (days + day) % 7
day_names = ["Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday"]

print(day_names[currentDate])
