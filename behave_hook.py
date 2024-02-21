# custom_behave_hooks.py
from behave.runner import ModelRunner
from behave.__main__ import main as behave_main
from behave.model import Scenario, ScenarioOutline


def add_custom_hooks_to_behave():
    behave_run_hook = ModelRunner.run_hook

    def run_hook(self, name, context, *args):
        if hasattr(context, "scenario"):
            scenario = context.scenario
            if isinstance(scenario, Scenario):
                if name == "before_scenario":
                    print("before_scenario")
                elif name == "after_scenario":
                    print("after_scenario")

        behave_run_hook(self, name, context, *args)

    ModelRunner.run_hook = run_hook


def process_items(items):
    # A lambda function to square each item
    squared_items = list(map(lambda x: x ** 2, items))
    return squared_items


if __name__ == "__main__":
    add_custom_hooks_to_behave()
    print(process_items([1, 2, 3, 4, 5]))
    behave_main()
