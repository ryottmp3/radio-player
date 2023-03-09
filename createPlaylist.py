import os, random
n=0
random.seed()
for root, dirs, files in os.walk('/Music/the-reeks/the-reeks'):
  for name in dirs:
    n += 1
    if random.uniform(0, n) < 1:
        rfile=os.path.join(root, name)
        print(rfile)