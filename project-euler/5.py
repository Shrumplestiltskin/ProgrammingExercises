#!/usr/bin/python
#Project Eueler #5

count = 2
while True:
    bool_ = True
    for x in range(1,21):
        if count % x != 0:
            bool_ = False
            break
    if bool_ == True:
        print(count)
        exit(0)
    count += 2
