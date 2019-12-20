import math
from pomegranate import *

#The guest's selection is pretty random
g=DiscreteDistribution({'A':1/3,'B':1/3,'C':1/3})

#The prize door's selection ,too, is random
p=DiscreteDistribution({'A':1/3,'B':1/3,'C':1/3})

#Monty's selection is heavily dependent on the prize and guest's selection
m=ConditionalProbabilityTable(
    [['A','A','A',0.0],
     ['A','A','B',0.5],
     ['A','A','C',0.5],
     ['A','B','A',0.0],
     ['A','B','B',0.0],
     ['A','B','C',1.0],
     ['A','C','A',0.0],
     ['A','C','B',1.0],
     ['A','C','C',0.0],
     ['B','A','A',0.0],
     ['B','A','B',0.0],
     ['B','A','C',1.0],
     ['B','B','A',0.5],
     ['B','B','B',0.0],
     ['B','B','C',0.5],
     ['B','C','A',1.0],
     ['B','C','B',0.0],
     ['B','C','C',0.0],
     ['C','A','A',0.0],
     ['C','A','B',1.0],
     ['C','A','C',0.0],
     ['C','B','A',1.0],
     ['C','B','B',0.0],
     ['C','B','C',0.0],
     ['C','C','A',0.5],
     ['C','C','B',0.5],
     ['C','C','C',0.0]],[g,p])

s1=State(g,name="Guest")
s2=State(p,name="Prize")
s3=State(m,name="Monty Hall")

network=BayesianNetwork("Monty Hall Problem")
network.add_states(s1,s2,s3)
network.add_edge(s1,s3)
network.add_edge(s2,s3)
network.bake()

beliefs=map(str,network.predict_proba({"Guest":"C"}))
print("\n".join("{}\t{}".format(state.name,str(belief)) for state,belief in zip(network.states,beliefs)))

beliefs_new=network.predict_proba({"Guest":"C","Monty Hall":"B"})
print("\n".join("{}\t{}".format(state.name,str(belief)) for state,belief in zip(network.states,beliefs_new)))
