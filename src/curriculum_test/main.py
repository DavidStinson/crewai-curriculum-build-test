#!/usr/bin/env python
import sys
import warnings

from curriculum_test.crew import CurriculumTest

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """

    # Inputs dictionary
    inputs = {
        'module_title': 'Introduction to Javascript Arrays',
        'module_topic': 'This JavaScript Arrays module is designed to provide a comprehensive introduction to arrays, a fundamental list datatype in programming. The module concludes with an extended practical exercise where learners will create, modify, and iterate through an array of strings. This content is suitable for beginners who are relatively new to JavaScript programming.',
        'learner_persona': 'Little to no prior coding experience; basic computer literacy is assumed. Students are adult learners and aspiring professionals.',
        'learning_objectives': (
            "Define JavaScript arrays and explain how they organize data.\n\n"
            "Identify the components of an array, including its elements and index positions.\n\n"
            "Create arrays using JavaScript literal notation in VS Code.\n\n"
            "Access and modify elements within an array using square brackets.\n\n"
            "Use basic array methods, such as push() and pop(), to manage array data."
        ),
        'tools': 'VSCode',
    }

    non_technical_inputs = {
        'module_title': 'Introduction to Typography',
        'module_topic': 'Introduction to Typography',
        'learner_persona': 'Little to no prior experience. Students are adult learners who are in a 420-hour UX Design program and aspiring professionals.',
        'learning_objectives': (
            'Identify the different aspects of typography to apply them to your designs.\n\n'
            'Make type choices to highlight hierarchy and the importance of elements in your design.\n\n'
        ),
        'tools': '',
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
