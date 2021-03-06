def run (autoTester):
	aList = [1, 2, 3, 'sun', 'moon', 'stars']
	autoTester.check (aList)
	autoTester.check (aList [2:4:1])
	autoTester.check (aList [:])
	autoTester.check (aList [2:])
	autoTester.check (len (aList))
	aList.append ('milkyway')
	autoTester.check (aList)
	aList.extend (['m1', 'm31'])
	autoTester.check (aList)

	anotherList = list (('a', 'b', 'c'))
	autoTester.check (anotherList)

	aDict = {1: 'plant', 'animal': 2}
	autoTester.check (aDict)
	autoTester.check (aDict [1], aDict ['animal'])

	aTuple = (1, 2, 3, 4, 5)
	autoTester.check(aTuple)
	autoTester.check (len (aTuple))

	anotherTuple = (1,)
	autoTester.check (anotherTuple)

	aSet = {1, 2, 2, 3}
	autoTester.check	(aSet)
	autoTester.check (len (aSet))

	anotherSet = set ((4, 5, 5, 6))
	autoTester.check (anotherSet)

	emptySet = set ()
	autoTester.check (emptySet)
	autoTester.check (len (emptySet))
