from pyevolve import G1DList, GSimpleGA, Initializators, Mutators, Consts
import math

# This is the Griewank Function, a deception function
def griewank(xlist):
    sum = 0
    for x in xlist:
        sum += x * x
    product = 1
    for i in xrange(len(xlist)):
        product *= math.cos(xlist[i] / math.sqrt(i + 1))
    return 1 + sum / 4000 - product


# Genome instance
genome = G1DList.G1DList(2);
genome.setParams(rangemin=-5.0, rangemax=5.0)
genome.initializator.set(Initializators.G1DListInitializatorReal)
genome.mutator.set(Mutators.G1DListMutatorRealGaussian)

# The evaluator function (objective function)
genome.evaluator.set(griewank)

# Genetic Algorithm Instance
ga = GSimpleGA.GSimpleGA(genome)
ga.minimax = Consts.minimaxType["minimize"]
ga.setGenerations(800)
ga.setMutationRate(0.05)

# Create DB Adapter and set as adapter
#sqlite_adapter = DBAdapters.DBSQLite(identify="griewank")
#ga.setDBAdapter(sqlite_adapter)

# Do the evolution, with stats dump # frequency of 10 generations
ga.evolve(freq_stats=50)

# Best individual
best = ga.bestIndividual()
print "\nBest individual score: %.2f" % (best.getRawScore(),)
print best
