from pydantic import BaseModel
from typing import List , Dict , Any

class AnalyzeRequest(BaseModel):
    transcript : str
    events : List[Dict[str, Any]]
    
    