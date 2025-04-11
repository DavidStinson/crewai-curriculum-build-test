#!/usr/bin/env python
import os
import sys
import warnings

from datetime import datetime

from curriculum_test.crew import CurriculumTest

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    base_path = os.path.join(os.path.dirname(__file__), '..', '..', 'inputs')

    # Paths to both input files
    instructions_path = os.path.join(
        base_path, 'custom_outline_instructions.txt')
    philosophy_path = os.path.join(
        base_path, 'general_assembly_learning_philosophy.txt')

    try:
        with open(instructions_path, 'r', encoding='utf-8') as f:
            custom_outline_instructions = f.read()
    except FileNotFoundError:
        raise Exception(f"Could not find file at: {instructions_path}")

    try:
        with open(philosophy_path, 'r', encoding='utf-8') as f:
            general_assembly_learning_philosophy = f.read()
    except FileNotFoundError:
        raise Exception(f"Could not find file at: {philosophy_path}")

    # Inputs dictionary
    inputs = {
        'module_topic': 'Introduction to Javascript Arrays',
        'learner_persona': 'Little to no prior coding experience; basic computer literacy is assumed.',
        'learning_objectives': (
            "Learners will be able to define JavaScript arrays and explain how they organize data.\n\n"
            "Learners will be able to identify the components of an array, including its elements and index positions.\n\n"
            "Learners will be able to create arrays using JavaScript literal notation in VS Code.\n\n"
            "Learners will be able to access and modify elements within an array using square brackets.\n\n"
            "Learners will be able to use basic array methods, such as push() and pop(), to manage array data."
        ),
        'custom_outline_instructions': custom_outline_instructions,
        'general_assembly_learning_philosophy': general_assembly_learning_philosophy
    }

    try:
        crew_output = CurriculumTest().crew().kickoff(inputs=inputs)
        print(f"Tokens used: {crew_output.token_usage}")
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")



def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'module_topic': 'Introduction to Javascript Arrays',
    }
    try:
        CurriculumTest().crew().train(n_iterations=int(
            sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        CurriculumTest().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'module_topic': 'Introduction to Javascript Arrays',
        'learner_persona': 'Little to no prior coding experience; basic computer literacy is assumed.'
    }
    try:
        CurriculumTest().crew().test(n_iterations=int(
            sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
