import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)
    
    def draw(self,number_of_balls):
        draw_results = []

        if number_of_balls >= len(self.contents):
            return self.contents

        for i in range(number_of_balls):
            draw_result = random.choice(self.contents)
            draw_results.append(draw_result)
            self.contents.pop(self.contents.index(draw_result))
            
        return draw_results
       
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    results = 0

    for i in range(num_experiments):
        copy_of_hat = copy.deepcopy(hat)

        actual = copy_of_hat.draw(num_balls_drawn)
    
        actual_dict = {ball: actual.count(ball) for ball in set(actual)}

        result = True
        for key, value in expected_balls.items():
            if key not in actual_dict or actual_dict[key] < expected_balls[key]:
                result = False
                break

        if result:
            results += 1

    return results/num_experiments

