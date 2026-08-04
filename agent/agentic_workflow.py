

from utils.model_loader import ModelLoader
from prompt_library.prompt import SYSTEM_PROMPT
from langgraph.graph import StateGraph , MessagesState , END , START 
from langgraph.prebuilt import ToolNode, tools_condition

from tools.weather_info_tool import WeatherInfoTool
from tools.place_search_tool import PlaceSearchTool
from tools.currency_conversion_tool import CurrencyConverterTool
from tools.expense_calculator_tool import CalculatorTool 



class GraphBuilder () :
    
    def __init__(self, agent):
        pass
    
    def agent_function(self )  :
        pass
    
    def build_graph(self, task):
        pass
    
    def __call__(self) :
        pass 