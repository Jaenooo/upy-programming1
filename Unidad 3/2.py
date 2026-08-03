class SavingsGoal:
    def __init__ (self, goal, monthly):
        self.goal = goal
        self.monthly = monthly
        
    def months_to_goal(self):
        saved = 0
        months = 0
        while saved < self.goal:
            saved = saved + self.monthly
            months = months + 1
        return months
print(SavingsGoal(1000,250).months_to_goal())
            