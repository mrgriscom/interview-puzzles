import random
import sys

class RandomGenerator(object):
    """Wrapper class for a random generator."""
    
    def __init__(self, range, generator_factory):
        """
        range: desired range of random integers, i.e., [0, range)
        generator_factory: when passed 'range', return a generator that emits a stream of random
          integers in the desired range
        """
        self.generator = generator_factory(range)
        self.range = range

    def next_int(self):
        return next(self.generator)

def generator_using_random(n):
    assert n > 0
    while True:
        yield random.randint(0, n - 1)
        
def generator_from_generator(n, generator):
    """
    n: desired range of uniform generator
    generator: existing uniform generator
    """
    assert n > 0
    if n > 1:
        assert generator.range > 1
    
    rand_int = 0
    effective_range = 1
    while True:
        while effective_range < n:
            rand_int = rand_int * generator.range + generator.next_int()
            effective_range *= generator.range
        usable_range = n * (effective_range // n)
        if rand_int < usable_range:
            yield rand_int % n
            rand_int /= n
            effective_range /= n
        else:
            rand_int -= usable_range
            effective_range -= usable_range

if __name__ == "__main__":

    n = int(sys.argv[1])
    k = int(sys.argv[2])
    num_trials = int(sys.argv[3])

    base_generator = RandomGenerator(k, generator_using_random)
    composed_generator = RandomGenerator(n, lambda rng: generator_from_generator(rng, base_generator))

    tallies = [0] * n
    for i in xrange(num_trials):
        tallies[composed_generator.next_int()] += 1

    for i, tally in sorted(enumerate(tallies), key=lambda (i, e): e):
        print '%.2f%% %d' % (100. * tally / num_trials, i)
