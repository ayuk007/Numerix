from langchain.agents import initialize_agent
from langchain.agents.agent_types import AgentType
from src.tools import WikipediaTool, MathTool, ReasoningTool

class Agent:
    def __init__(self):
        """
        An agent that'll use all the tools required to solve the mathematical problem.
        """

        self.math_tool = MathTool.math_tool
        self.wikipedia_tool = WikipediaTool.wikipedia_tool
        self.reasoning_tool = ReasoningTool.reasoning_tool
        self.agent = initialize_agent(
            tools = [self.wikipedia_tool, self.math_tool, self.reasoning_tool],
            llm = MathTool.llm_model,
            agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose = False,
            handle_parsing_errors = True,
        )
    