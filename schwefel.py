from pyevolve import G1DList, GSimpleGA, Initializators, Mutators, Consts
import math

# This is the Schwefel Function, a deception function
def schwefel(xlist):
   n = len(xlist)
   total = 0
   for i in range(n):
      total += xlist[i]*math.sin(math.sqrt(math.fabs(xlist[i])))
   return 418.9829*2+total



# Genome instance
genome = G1DList.G1DList(2);
genome.setParams(rangemin=-500, rangemax=500)
genome.initializator.set(Initializators.G1DListInitializatorReal)
genome.mutator.set(Mutators.G1DListMutatorRealGaussian)

# The evaluator function (objective function)
genome.evaluator.set(schwefel)

# Genetic Algorithm Instance
ga = GSimpleGA.GSimpleGA(genome)
ga.minimax = Consts.minimaxType["minimize"]
ga.setGenerations(2000)
ga.setMutationRate(0.02)

# Create DB Adapter and set as adapter
#sqlite_adapter = DBAdapters.DBSQLite(identify="schwefel")
#ga.setDBAdapter(sqlite_adapter)

# Do the evolution, with stats dump # frequency of 10 generations
ga.evolve(freq_stats=50)

# Best individual
best = ga.bestIndividual()
print "\nBest individual score: %.2f" % (best.getRawScore(),)
print best
