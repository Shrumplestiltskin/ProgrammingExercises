def checkio(*args):
    try: return max(args) - min(args)
    except ValueError: return 0

if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert(almost_equal(checkio(1,2,3),2,3))
    assert(almost_equal(checkio(5,-5),10,3))
    assert(almost_equal(checkio(10.2,-2.2,0,1.1,0.5),12.4,3))
    assert(almost_equal(checkio(),0,3))
