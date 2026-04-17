def engineering_agent(context , llm):
  
  prompt = f"""
  
  You are a Software Engineer
  
  Analyze:
  {context}
  
  Identify technical risks or inefficiencies.
  """
  
  return llm(prompt)