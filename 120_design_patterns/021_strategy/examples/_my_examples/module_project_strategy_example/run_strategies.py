from strategies.execute_strategy import ExecuteStrategy
from strategies.strategy_almpl import StrategyAlmpl
from strategies.strategy_blmpl import StrategyBlmpl
from strategies.strategy_clmpl import StrategyClmpl
from strategies.strategy_dlmpl import StrategyDlmpl


def run_strategies():
    valueToCalculate = 100.0
    print('Value to calculate is: ' + str(valueToCalculate))

    executeStrategyA = ExecuteStrategy(StrategyAlmpl)
    executeStrategyA.execute(valueToCalculate)

    executeStrategyB = ExecuteStrategy(StrategyBlmpl)
    executeStrategyB.execute(valueToCalculate)

    executeStrategyC = ExecuteStrategy(StrategyClmpl)
    executeStrategyC.execute(valueToCalculate)

    executeStrategyD = ExecuteStrategy(StrategyAlmpl)
    executeStrategyD.execute(valueToCalculate)



if __name__ == '__main__':
    run_strategies()
