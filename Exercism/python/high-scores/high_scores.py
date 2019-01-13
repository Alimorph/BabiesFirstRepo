class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores[len(self.scores)-1]
    
    def personal_best(self):
        best = 0
        for score in self.scores:
            if score > best:
                best = score
        return best

    def personal_top(self):
        return sorted(self.scores, reverse=True)[0:3]

    def report(self):
        best = self.personal_best()
        latest = self.latest()
        if best > latest:
            return "Your latest score was "+str(latest)+". That's "+str(best-latest)+" short of your personal best!"
        else:
            return "Your latest score was "+str(latest)+". That's your personal best!"