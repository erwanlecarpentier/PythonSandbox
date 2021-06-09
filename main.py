import sys
sys.path.append('/home/wahara/Documents/git/myrl/src')

import cfg.config as cfg
import myrl
from myrl.experiments import benchmark as benchmark

if __name__ == "__main__":
    benchmark(cfg.MYRL_TEST)
    print("Holà!")