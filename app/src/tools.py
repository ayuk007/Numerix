from dotenv import load_dotenv
from dataclasses import dataclass
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.prompts import PromptTemplate
from langchain.agents import Tool
from langchain_groq import ChatGroq
from langchain.chains import LLMMathChain, LLMChain
load_dotenv()  # load the environment credentials 

@dataclass
class WikipediaTool:
    """
    A wikipedia tool to get the information from the web. Like date, events, year etc.
    For ex:
    John was born after the 10 years of the last coldwar.
    This tool will help in search the wed to get the information of the last coldwar.
    """

    wikipedia = WikipediaAPIWrapper()
    wikipedia_tool = Tool(
        name = "Wikipedia",
        func = wikipedia.run,
        description = """A usefull tool to search the internet for information 
        related to world events, issues, dates, years, etc. 
        Worth using for general topics. Use precise questions.""",
    )

@dataclass
class MathTool:
    """
    A math tool, that'll be useful for mathematical operation.
    In the backend it uses 'numexpr' library to evaluate the mathematical expression.
    """

    # Initializing large language model Gemma2-9b-It,
    # with temperature 0.1 to decrease the randomness of the answer
    llm_model = ChatGroq(model = "Gemma2-9b-It", temperature = 0.1)
    math_chain= LLMMathChain.from_llm(llm = llm_model)
    math_tool = Tool.from_function(
        name = "Calculator",
        func = math_chain.run,
        description = """Useful for when you need to answer questions 
        about math. This tool is only for math questions and nothing else. Only input
        math expressions."""
    )

@dataclass
class ReasoningTool:
    """
    A reasoning tool, that'll provide the methods and reasons for the solving the question given.
    It also helps to formulate the answer in steps.
    """

    template = """You are a reasoning agent tasked with solving 
    the user's logic-based questions. Rearrange the question according to your understanding. 
    Logically arrive at the solution, and be factual. 
    In your answers, clearly detail the steps involved and give the 
    final answer. Provide the response in bullet points.
    As the final output clearly state all the steps to solve the problem in bullet points.
    Question  {question} Answer"""
    
    llm_model = MathTool.llm_model
    prompt = PromptTemplate.from_template(
        template = template,
        input_variable = ["question"]
    )
    word_chain = LLMChain(
        llm = llm_model,
        prompt = prompt
    )
    reasoning_tool = Tool.from_function(
        name = "Reasoning Tool",
        func = word_chain.run,
        description = "Useful for when you need to answer logic-based/reasoning questions."
    )