n = int(input())
flights = []
for i in range(n):
    flightTicket = int(input())
    flights.append(flightTicket)
maximum_cost = max(flights) //2
remainingCost = maximum_cost - (min(flights))
if remainingCost < 0:
    print(abs(remainingCost))
else:
    print(0)