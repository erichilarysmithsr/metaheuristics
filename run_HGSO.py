from models.multiple_solution.physics_based.HGSO import BaseHGSO, OppoHGSO, LevyHGSO
from utils.FunctionUtil import *

## Setting parameters
root_paras = {
    "problem_size": 100,
    "domain_range": [-1, 1],
    "print_train": True,
    "objective_func": C25
}
hgso_paras = {
    "epoch": 500,
    "pop_size": 100,
    "n_clusters": 5
}

## Run model
md = LevyHGSO(root_algo_paras=root_paras, hgso_paras=hgso_paras)
md._train__()

