"""For guessing selected number"""

import numpy as np

class GuessGame:
    """
    Game where u need to guess number from 1 to 100
    in this class u can guess number manually or by computer calculations
    """
    def __init__(self, type='manual') -> None:
        # attempt quantity
        self.count = 0
        self.type = type
        if self.type in ['manual', 'calc']:
            self.number = np.random.randint(1, 101) # random number
        elif self.type == 'semicalc':
            self.number = 0
    
    def start(self, *args):
        """Statring the game
        Depends on type parameter
        """
        if self.type == 'manual':
            self.__start_manual()
        elif self.type == 'calc':
            self.__start_calc()
        elif self.type == 'semicalc':
            self.__start_semicalc(*args)
    
    def __start_manual(self):
        """Start with manual guessing if random number"""
        while True:
            try:
                predict_number = int(input('Guess number from 1 to 100 '))
            except ValueError:
                continue
            self.count += 1
            classify_number = self.__classify_number(predict_number)
            if classify_number == 0:
                break
    
    def __start_calc(self):
        """Start with automatic guessing of random number (w/o any parameters)"""
        while True:
            self.count += 1
            guess_num = np.random.randint(1, 101)
            classify_number = self.__classify_number(guess_num)
            if classify_number == 0:
                break
    
    def __start_semicalc(self, number):
        """Start with automatic guessing with custom number initialisation"""
        self.number = number
        self.__start_calc()
            
    def __classify_number(self, predict_number: int) -> int:
        """Comparing potential number with self.number

        Args:
            predict_number (int): Number for comparing with self.number

        Returns:
            int: function result where:
                0: guessed
                1: predict_number more than self.number
                -1: predict_number less than self.number
        """
        if predict_number > self.number:
            if self.type == 'manual':
                print('Number must be less')
            return -1
        elif predict_number < self.number:
            if self.type == 'manual':
                print('Number must be more')
            return 1
        else:
            if self.type in ['manual', 'calc']:
                print(f'Congratalutions! You have guessed the number, number = {self.number}. Attempt quant = {self.count}')
            return 0

def start_game_calc(type:str='calc'):
    """For statring game

    Args:
        type (str, optional): For selecting game type. Defaults to 'calc'.
    """
    g = GuessGame(type='calc')
    g.start()


def estimate_random_guessing() -> float:
    """ Testing the game algorithm: we need to know average quantity of attempts

    Returns:
        float: average score of attempts
    """
    count_list = []
    np.random.seed(1)
    random_arr = np.random.randint(1, 101, size=1000)
    for random_num in random_arr:
        g = GuessGame(type='semicalc')
        g.start(random_num)
        count_list.append(g.count)
    score = int(np.mean(count_list))
    print(f'Mean attempts = {score}')
    return score

if __name__ == '__main__':
    estimate_random_guessing()