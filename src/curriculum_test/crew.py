from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task

claude_sonnet = LLM(
    model="claude-3-5-sonnet-20240620",
    max_tokens=8192
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
            llm=claude_sonnet
        )
    
    @agent
    def subject_matter_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['subject_matter_expert'],
            verbose=True,
            llm=claude_sonnet
        )

    @task
    def generate_module_outline_task(self) -> Task:
        return Task(
            config=self.tasks_config['generate_module_outline'],
        )
    
    @task
    def develop_microlesson_content_task(self) -> Task:
        return Task(
            config=self.tasks_config['develop_microlesson_content'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CurriculumTest crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
