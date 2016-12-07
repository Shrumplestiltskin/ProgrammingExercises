def probability(dice_number, sides, target):
    return 0.0

if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision
        
    print(almost_equal(probability(2, 6, 3), 0.0556))
    print(almost_equal(probability(2, 6, 4), 0.0833))
    print(almost_equal(probability(2, 6, 7), 0.1667))
    print(almost_equal(probability(2, 3, 5), 0.2222))
    print(almost_equal(probability(2, 3, 7), 0.0000))
    print(almost_equal(probability(3, 6, 7), 0.0694))
    print(almost_equal(probability(10, 10, 50), 0.0375))
