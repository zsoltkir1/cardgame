class Card():
    
    def __init__(self,name,top,bot,left,right):
        self.name=name
        self.top=top
        self.bot=bot
        self.left=left
        self.right=right

    def __str__(self):
        return "name: "+self.name+"\nvalues: "+str(self.top)+" "+str(self.bot)+" "+str(self.left)+" "+str(self.right)