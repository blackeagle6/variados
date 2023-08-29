inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]
txt="The store has {} {}, each for {} USD."
for x in inventory:
    print(txt.format(x,'','')+txt.format('',x,'')+txt.format('','',x))


