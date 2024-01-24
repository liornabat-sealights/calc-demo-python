# custom_behave_hooks.py
from behave.runner import ModelRunner
from behave.__main__ import main as behave_main
from behave.model import Scenario
def add_custom_hooks_to_behave():
    behave_run_hook = ModelRunner.run_hook

    def run_hook(self, name, context, *args):
        if hasattr(context, "scenario"):
            scenario = context.scenario
            if isinstance(scenario, Scenario):
                print(f"Running hook from sl: {name} for scenario: {scenario.name}")
            else:
                print(f"Running hook from sl: {name} for scenario: {scenario}")
            scenario.skip()
        behave_run_hook(self, name, context, *args)
        print(f"Running hook: {name}")

    ModelRunner.run_hook = run_hook


if __name__ == "__main__":
    add_custom_hooks_to_behave()
    behave_main()

