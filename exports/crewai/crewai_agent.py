from crewai import Agent
def create_agent():
    return Agent(role='GitCompBenchmark', goal='Autonomous Compensation Equity, Salary Band Parity & Equal Pay Compliance Agent', backstory='Autonomous agent', verbose=True)
