from AI import *
from Board import *


p1 = Agent("p1")
p2 = Agent("p2")

st = Board(1, 2)
print("training...")
st.play_ai(p1,p2,25000)



