from groq import Groq
from typing import Optional,List
from pydantic import BaseModel
import time
from groq import GroqError,APIStatusError,RateLimitError,APIConnectionError,APIError,APITimeoutError,NotFoundError,BadRequestError,AuthenticationError,InternalServerError,UnprocessableEntityError,PermissionDeniedError
import os

class Messages(BaseModel):
  id:str
  role:str
  content:str

class LLMParams(BaseModel):
  api_key:str
  model:str
  temprature:float
  max_retries:int
  
class InvokeParams(BaseModel):
  messages:List[Messages]
  

class LLMResponse(BaseModel):
  content:str


class GroqLLM(BaseModel):
  def __init__(self,params:LLMParams):
    self._limit=params['max_retries'] # this is the maximum retry llm have to do
    self._delay=1 # timer
    self._curr=1
    self._model=params['model']
    self._temp=params['temprature']
    groq_api_key:str=params['api_key']
    try:
      if(type(groq_api_key)!=str):
          print("Invalid api key")
      self._client = Groq(
          # This is the default and can be omitted
          api_key=groq_api_key,
          )
    except Exception as e:
      raise Exception("kuch to hua hai",str(e))  
    
  def invoke(self,params:InvokeParams)->dict:
    
    try:
      while(self._curr<self._limit):
        if(self._curr>1):
          time.sleep(self._delay)
        chat_completion = self._client.chat.completions.create(
                messages=params['messages'],
                model=self._model if self._model!="" else "openai/gpt-oss-20b",
            )
        # raise RateLimitError(message="something went wrong",response="rate limit ho gaya hai",body={"success":False})
        # response=chat_completion.choices[0].message.content
        # return {"content":response}

      if(self._curr==self._limit):
        print("maximum limit exceed for max try plz try again later after 1hr")
        
        
      
    except (RateLimitError,InternalServerError,APITimeoutError,APIConnectionError) as e: 
      # these are retriable erros 
      self._delay*=2
      self._curr+=1
      print(str(e))

    except (AuthenticationError,BadRequestError,NotFoundError) as e: 
      # these are non retriable erros 
      print(str(e))

    except GroqError as e:
      print(str(e))
      
    
      

    

      

