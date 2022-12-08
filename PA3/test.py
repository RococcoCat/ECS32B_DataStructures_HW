import unittest
from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('tests')
    with open('results.json', 'w') as f:
        #set buffer = False for Section 3 to see progress of tests.
        tr = JSONTestRunner(visibility='visible', verbosity=0, buffer=True, stream=f)
        out = tr.run(suite)

    score = 0
    for test in sorted(tr.json_data["tests"],key=lambda x: x['name']):
        score += test['score']
        if test['score']==test['max_score']:
            print(bcolors.OKGREEN+'-'*10)
            for k,v in test.items():
                print(k,v)
        else:
            print(bcolors.FAIL+'-'*10)
            for k,v in test.items():
                print(f"{k}:{v}")

    print(bcolors.HEADER + bcolors.BOLD + f"Your final score: {min(round(score,2),24)}/18")
    print(bcolors.ENDC)