from AI import *
from Board import *
from againsthuman import *


playerSelection = str(input("Select your player(B or R): ").lower())
if playerSelection == "R":
    p1= Agent("computer",exp_rate=0.3)
    p1.load_policy("for_p1")
    p2 = againsthuman("human")
    st= Board(1,2)
    st.play_human(p1,p2)
else:
    p2= Agent("computer",exp_rate=0.3)
    p2.load_policy("for_p2")
    p1 = againsthuman("human")
    st= Board(1,2)
    st.play_human(p1,p2)

