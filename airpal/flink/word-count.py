from flink.plan.Environment import get_environment
from flink.plan.Constants import INT, STRING
from flink.functions.GroupReduceFunction import GroupReduceFunction

class Adder(GroupReduceFunction):
    def reduce(self, iterator, collector):
        count, word = iterator.next()
        count += sum([x[0] for x in iterator])
        collector.collect((count, word))


if __name__ == "__main__":
  env = get_environment()
  data = env.from_elements("Who's there?",
                           "I think I hear them. Stand, ho! Who's there?")

  data \
    flat_map(lambda x, c: [(1, word) for word in x.lower().split()]) \
    .group_by(1) \
    .reduce_group(Adder(), (INT, STRING)) \
    .output()

  env.execute(local=True)
