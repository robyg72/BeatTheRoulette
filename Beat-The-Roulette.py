# percentuale di pari e dispari
# percentuale di rossi e neri
# percentuale dozzina


reds = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
blacks = [2, 6, 4, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

class Outcome(object):
    def __init__(self, number):
        # store the number drawn
        self.number = int(number)

        # set if number is even or odd
        if self.number % 2 == 0:
            self.is_even = True
        else:
            self.is_even = False

        # set if number is zero
        if self.number == 0:
            self.is_zero = True
        else:
            self.is_zero = False

        # set color of the number
        if self.number in reds:
            self.is_red = True
        else:
            self.is_red = False

        if self.number in blacks:
            self.is_black = True
        else:
            self.is_black = False

    def __str__(self):
        if self.is_even:
            parity = "even"
        else:
            parity = "odd"

        if self.is_zero:
            parity = "is zero"
            color = ""
        else:
            if self.is_red:
                color = "RED"
            else:
                color = "BLACK"

        return str(self.number) + " " + parity + " " + color

class Roulette(object):
    def __init__(self):
        self.lastOutcome = None
        self.mean = 0
        self.red_percentage = 0
        self.black_percentage = 0
        self.odd_percentage = 0
        self.even_percentage = 0
        self.numbers = []  # store each Outcome drawn
        self.extractionNumber = 0
        self.frequency = {"0": 0,
                          "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "10": 0, "11": 0,
                          "12":0, "13":0, "14":0, "15":0, "16": 0,
                          "34": 0, "35": 0, "36": 0}  # store frequency outcomes for each figure

    # Calculates the mean value after each extraction
    def __mean(self):
        m = 0
        if len(self.numbers) > 0:
            for n in self.numbers:
                m = m + n.number
            m = m / len(self.numbers)
        else:
            m = 0
        return m

    def new_outcome(self, number):
        outcome = Outcome(number)
        self.lastOutcome = outcome
        self.numbers.append(outcome)
        if str(outcome.number) in self.frequency:
            self.frequency[str(outcome.number)] = self.frequency[str(outcome.number)] + 1
        self.extractionNumber = len(self.numbers)

        for o in self.numbers:
            if o.number != 0:
                if o.number % 2 == 0:
                    self.even_percentage += 1
                else:
                    self.odd_percentage += 1

if __name__ == "__main__":
    r = Roulette()
    cmd = '0'
    while cmd != '99':
        cmd = raw_input("Numero estratto ")
        r.new_outcome(cmd)
        print "------------------------------"
        print "Numero di estrazioni " + str(r.extractionNumber)
        for e in r.numbers:
            print e
        print "------------------------------"