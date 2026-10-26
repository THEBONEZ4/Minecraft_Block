class Mapmanager():
    def __init__(self):
        self.model = 'block'
        self.texture = 'block.png'
        self.color = (225, 255, 255, 1)
        self.startNew()
        self.addBlock((0, 10, 0))

    def startNew(self):
        self.ground_dirt = render.attachNewNode('White Concrete')


    def addBlock(self, position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.block.setColor(self.color)
        self.block.reparentTo(self.ground_dirt)


