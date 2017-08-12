class Outcome:
    def __init__(self, figure):
        self.figure = int(figure)
        if self.figure % 2 == 0:
            self.is_even = True
        else:
            self.is_even = False

    def __str__(self):
        if self.is_even:
            parity = "even"
        else:
            parity = "odd"
        return str(self.figure) + " " + parity


class Roulette:
    def __init__(self):
        self.lastOutcome = None
        self.mean = 0
        self.numbers = []  # store each Outcome drawn
        self.frequency = {"0": 0, "1": 0, "2": 0, "3": 0, "12":0, "23": 0, "34": 0}  # store frequency outcomes for each figure

    # Calculates the mean value after each extraction
    def _mean(self):
        m = 0
        if len(self.numbers) > 0:
            for n in self.numbers:
                m = m + n.figure
            m = m / len(self.numbers)
        else:
            m = 0
        return m

    def new_outcome(self, number):
        outcome = Outcome(number)
        self.lastOutcome = outcome
        self.numbers.append(outcome)
        self.frequency[str(outcome.figure)] = self.frequency[str(outcome.figure)] + 1
        print self._mean()


if __name__ == "__main__":
    r = Roulette()
    cmd = '0'
    while cmd != '99':
        cmd = raw_input("Numero estratto ")
        r.new_outcome(cmd)
