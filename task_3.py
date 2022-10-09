channels = ["BBC", "Discovery", "TV1000"]

class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.current_channel_index = 0

    
    def first_channel(self):
        return self.turn_channel(1)
    

    def last_channel(self):
        return self.turn_channel(len(self.channels))
    
    
    def turn_channel(self, channel):
        self.current_channel_index = channel - 1
        return self.channels[self.current_channel_index]
    
    
    def next_channel(self):
        next_channel = self.current_channel_index + 2
        
        if next_channel > len(self.channels):
            next_channel = 1
        return self.turn_channel(next_channel)
    
    
    def previous_channel(self):
        previous_channel = self.current_channel_index
        
        if previous_channel < 1:
            previous_channel = len(self.channels)
        return self.turn_channel(previous_channel)
    
    
    def current_channel(self):
        return self.channels[self.current_channel_index]
    
    
    def is_exist(self, channel):

        if isinstance(channel, int):
            if channel - 1 in range(len(self.channels)):
                return True
        if isinstance(channel, str):
            if channel in self.channels:
                return True
            
        return False

        

controller = TVController(channels)
# print(controller.is_exist("Discovery"))


print(controller.first_channel() == "BBC")

print(controller.last_channel() == "TV1000")

print(controller.turn_channel(1) == "BBC")

print(controller.next_channel() == "Discovery")

print(controller.previous_channel() == "BBC")

print(controller.current_channel() == "BBC")

controller.is_exist(4) == False

controller.is_exist("Discovery") == True