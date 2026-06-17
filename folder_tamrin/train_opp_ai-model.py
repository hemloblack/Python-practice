class AIModel:
   
    def __init__(self, name, accuracy,task):
        self.name = name          
        self.accuracy = accuracy  
        self.task=task
        self.is_trained = False

    def show_info(self):
        print(f"name ai model: {self.name} , ai accuracy: {self.accuracy} ,task:{self.task}")

    def train(self, epochs):
        print(f"Starting training for {self.name}...")
        self.is_trained = True
        for i in range(epochs):
            if self.accuracy < 100:
                self.accuracy += 0.5
                self.accuracy = round(self.accuracy,2)
        print(f"Training finished! New accuracy: {self.accuracy}%")

    def predict(self,data):
        if self.is_trained==False:
            print("worrning:The model must be trained first.")
        elif self.is_trained==True:
            print(f"Model {self.name} is predicting on {data}...")


ai_xrak=AIModel("xrak",70.5,"photograph")
ai_xrak.show_info()
ai_xrak.predict("i dont know ")