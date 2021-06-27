class SoccerPlayer(object):
    def _init_(self,name,position,back_number):
         self.name = name
         self.position = position
         self.back_number = back_number



    def _str_(self):
         return "Hello,My name is %s. I play in %s in center"%(self.name, self.position)

jinhyun = SoccerPlayer("jinhyun","MF",10)
print(jinhyun)
