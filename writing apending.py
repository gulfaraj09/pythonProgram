# f = open("gulfaraj.txt", "w")
# a = f.write("Harry bhai bahut achhe hain\n")
# print(a)
# f.close()

# f = open("gulfaraj2.txt", "a")
# a = f.write("Harry bhai bahut achhe hain\n")
# print(a)
# f.close()


# Handle read and write both
f = open("gulfaraj2.txt", "r+")
print(f.read())
f.write("thank you")

