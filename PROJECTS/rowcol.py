row_1 = ["🎅","✅","🔥"]
row_2 = ["🎅","✅","🔥"]
row_3 = ["🎅","✅","🔥"]

combined_row = [row_1,
                 row_2,
                  row_3]

put = input("Where do you want to put in rows and col :")

row = int(put[0])
col = int(put[1])

combined_row[row - 1][col - 1] = "x"

print(f"{combined_row}")