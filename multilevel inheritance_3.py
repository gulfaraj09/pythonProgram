class Dad:
    basketball =1

class Son(Dad):
    dance =1
    basketball = 9
    def isdance(self):
        return f"Yes I dance {self.dance} no of times"

class Grandson(Son):
    guitar =1
    dance = 6
    def isdance(self):
        return f"Jackson yeah!\n" \
               f"Yes I dance very awesomely {self.dance}" \
               f" no of times"

darry = Dad()
larry = Son()
gulfaraj = Grandson()

print(gulfaraj.isdance())
print(gulfaraj.basketball)
print(gulfaraj.guitar)


# electronic device
# pocket gadget
# phone