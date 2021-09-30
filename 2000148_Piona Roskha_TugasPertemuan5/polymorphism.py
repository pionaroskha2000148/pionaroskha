class Indonesia:
    def __init__(self, daerah, mata_uang):
        self.daerah = daerah
        self.mata_uang = mata_uang 

    def sapaan(self):
        print(f"Hallo, Indonesia berada di", self.daerah,"mata uang di negara ini ialah", self.mata_uang)

class Jepang:
    def __init__(self, daerah, mata_uang):
        self.daerah = daerah
        self.mata_uang = mata_uang

    def sapaan(self):
        print(f"Kon'nichiwa, Jepang berada di", self.daerah, "mata uang di negara ini ialah", self.mata_uang)

Indonesia1 = Indonesia("Asia Tenggara","Rupiah")
Jepang1 = Jepang("Asia Timur","Yen") 

for negara in (Indonesia1, Jepang1): 
    negara.sapaan()
