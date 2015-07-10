from __future__ import division
import multiprocessing as mp
from buy import Buy
#from quote_buy import QuoteBuy
from sell import Sell
from give import Give  # tests give and messaging
from logger_test import LoggerTest
from endowment import Endowment
from production_multifirm import ProductionMultifirm
from production_firm import ProductionFirm
from utility_household import UtilityHousehold
from abce import *


def main():
    for parameters in read_parameters('simulation_parameters.csv'):
        s = Simulation(parameters)
        action_list = [
            repeat([
                ('all', 'one'),
                ('all', 'two'),
                ('all', 'three'),
                ('all', 'clean_up')
                ], 100),
            ('buy', 'panel'),
            ('endowment', 'Iconsume'),
            ('productionmultifirm', 'production'),
            ('productionfirm', 'production'),
            ('utilityhousehold', 'consumption'),
            ('all', 'all_tests_completed')]
        s.add_action_list(action_list)

        s.declare_round_endowment(resource='labor_endowment', units=5, product='labor')
        s.declare_round_endowment(resource='cow', units=10, product='milk')
        s.declare_perishable(good='labor')
        s.panel('buy', variables=['price'])

        s.build_agents(Buy, 2)
        #s.build_agents(QuoteBuy, 2)
        s.build_agents(Sell, 2)
        s.build_agents(Give, 2)  # tests give and messaging
        s.build_agents(Endowment, 2)  # tests declare_round_endowment and declare_perishable
        s.build_agents(LoggerTest, 1)
        s.build_agents(ProductionMultifirm, 1)
        s.build_agents(ProductionFirm, 5)
        s.build_agents(UtilityHousehold, 5)



        s.run()

if __name__ == '__main__':
    mp.freeze_support()
    main()
