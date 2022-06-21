#HOW TO USE:
#Copy and paste the links as comma separated strings into mylist[] (ALT+SHIFT+G for multiline editting)
#The output is printed and can be copy and pasted directly into the excel sheet

mylist = ["https://www.youtube.com/watch?v=70m7ML8_Tfw&list=PLA6Q4fImhYLOyuXXZlF7X1tmb5uUBa5iT&index=151",
"https://www.youtube.com/watch?v=EM7uClKtmQg&list=PLA6Q4fImhYLOyuXXZlF7X1tmb5uUBa5iT&index=178",
"https://www.youtube.com/watch?v=cMFX3jmIB00&list=PLA6Q4fImhYLOyuXXZlF7X1tmb5uUBa5iT&index=199",
"https://www.youtube.com/watch?v=6JwbzSpVHYc&list=PLA6Q4fImhYLOyuXXZlF7X1tmb5uUBa5iT&index=215",
"https://www.youtube.com/watch?v=wWsjtLTQtms&list=PLA6Q4fImhYLOyuXXZlF7X1tmb5uUBa5iT&index=244",
"https://www.youtube.com/watch?v=WabwiGl-D3o&list=PLA6Q4fImhYLOyuXXZlF7X1tmb5uUBa5iT&index=264",
"https://www.youtube.com/watch?v=2Qc5d7Zi6Sk&list=PLA6Q4fImhYLOyuXXZlF7X1tmb5uUBa5iT&index=675",
"https://www.youtube.com/watch?v=I4BdjVEJdlk&list=PLA6Q4fImhYLOyuXXZlF7X1tmb5uUBa5iT&index=1025",
"https://www.youtube.com/watch?v=gUpdozvB3XA&list=PLA6Q4fImhYLOyuXXZlF7X1tmb5uUBa5iT&index=1201",
"https://www.youtube.com/watch?v=aHeVN2oquds&list=PLA6Q4fImhYLOyuXXZlF7X1tmb5uUBa5iT&index=1559",
"https://www.youtube.com/watch?v=U33yvLae2CQ&list=PLA6Q4fImhYLOyuXXZlF7X1tmb5uUBa5iT&index=1512",
"https://www.youtube.com/watch?v=sQBNJgkwY9c&list=PLA6Q4fImhYLOyuXXZlF7X1tmb5uUBa5iT&index=1338",
"https://www.youtube.com/watch?v=udG6Bt1RXT4&list=PLA6Q4fImhYLOyuXXZlF7X1tmb5uUBa5iT&index=912"
]

for x in range(0, len(mylist)):
    mylist[x] = "https://www.youtube.com/embed/" + mylist[x][32:43] + "?controls=0"
    print(mylist[x])