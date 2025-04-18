from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource
import litellm

litellm._turn_on_debug()

# Create a text file knowledge source
text_sources_instructional_architect = TextFileKnowledgeSource(
    file_paths=["general_assembly_learning_philosophy.txt"]
)

text_sources_learning_experience_designer = TextFileKnowledgeSource(
    file_paths=["creating-clear-exercises.txt",
                "markdown-document-structure.txt", "modular-code.txt", "modular-writing.txt", "technical-voice.txt", "creating-inclusive-and-globally-relevant-content.txt"]
)

claude_sonnet = LLM(
    model="claude-3-5-sonnet-20240620",
    max_tokens=8192
)

chatgpt_41 = LLM(
    model="gpt-4.1",
    max_tokens=8192,
)

openai_o3mini = LLM(
    model="o3-mini",
    max_tokens=8192,
)


@CrewBase
class CurriculumTest():
    """CurriculumTest crew"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def instructional_architect(self) -> Agent:
        return Agent(
            config=self.agents_config['instructional_architect'],
            verbose=True,
            llm=claude_sonnet,
            knowledge_sources=[text_sources_instructional_architect],
            cache=False
        )

    @agent
    def subject_matter_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['subject_matter_expert'],
            verbose=True,
            llm=chatgpt_41,
            cache=False
        )

    @agent
    def learning_experience_designer(self) -> Agent:
        return Agent(
            config=self.agents_config['learning_experience_designer'],
            verbose=True,
            llm=claude_sonnet,
            knowledge_sources=[text_sources_learning_experience_designer],
            cache=False
        )

    @task
    def generate_module_outline_task(self) -> Task:
        return Task(
            config=self.tasks_config['generate_module_outline']
        )

    @task
    def develop_microlesson_content_task(self) -> Task:
        return Task(
            config=self.tasks_config['develop_microlesson_content'],
        )

    @task
    def learning_design_task(self) -> Task:
        return Task(
            config=self.tasks_config['learning_design_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CurriculumTest crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        my_crew = Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            output_log_file="./output/crew_log.md",
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )

        my_crew.reset_memories(command_type = "all")

        return my_crew
