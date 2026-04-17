def growth_agent(llm , context):
  
  prompt = f"""
  
  You are a growth strategist
  
  Analyze this:
  {context}
  
  
  Identify:
  - conversion issues
  - activation gaps
  """
  
  
  return llm(prompt)