from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableBrach
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = 'classify the sentiment of the following feedback text into positive or negative \n {feedback}',
    input_variables = ['feedback']
)

class Feedback(BaseModel):
    sentiment: Literal['Positive', 'negative'] = Field(description = 'Give the sentiment of the feedback text into positive or negative \n {feedback} \n {format_instruction}')

parser2 = PydanticOutputParser(pydantic_object=Feedback)

classifier_chain = prompt1 | model | parser2

branch_chain = RunnableBranch(
    (condition1, chain),
    (co)

)