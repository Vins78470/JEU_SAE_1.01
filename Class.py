class Coder():
    def __init__(self, cl, em, e, r):
        self.coding_level = cl
        self.energie_max = em
        self.energie = e
        self.richesse = r


class Mission():
    def __init__(self, sw, rw,d):
        self.starting_workload= sw
        self.remaining_worload = rw
        self.difficulte = d             

    def Get_remaining_workload(self):
        print(self.remaining_worload)




Mission1 = Mission("8h", "3h",0) 

Mission.Get_remaining_workload(Mission1)




