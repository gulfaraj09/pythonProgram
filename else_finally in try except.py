f1 = open("gulfaraj.txt")

try:
    f = open("does2.txt")

except IOError as e:
    print("print IOError", e)
except EOFError as e:
    print("Print eof error", e)
except Exception as e:
    print(e)

else:
    print("This will run only if except is not running")

finally:
    print("Run this anyway...")
    f1.close()

print("Important stuff")