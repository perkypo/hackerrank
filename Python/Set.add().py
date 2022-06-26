# Apply your knowledge of the .add() operation to help your friend Rupal. 
# Rupal has a huge collection of country stamps. She decided to count the 
# total number of distinct country stamps in her collection. She asked for 
# your help. You pick the stamps one by one from a stack of  country stamps. 
# Find the total number of distinct country stamps.

N=int(input())
S=set()
for _ in range(N):
     S.add(input())
print(len(S))