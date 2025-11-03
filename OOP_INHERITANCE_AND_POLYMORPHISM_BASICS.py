# exe1
class Agent:
    total_agents=0
    def __init__(self,code_nema,clearance_level):
        self.code_nema=code_nema
        self._clearance_level=clearance_level
        Agent.total_agents+=1
        
    def get_clearance_level(self):
        return self._clearance_level
    def set_clearance_level(self,clearance):
        self.clearance=clearance
        if 1 <= clearance <=10:
            self._clearance_level = clearance
        return self._clearance_level
    @classmethod
    def get_total_agents(cls):
        return F'number of agents is {cls.total_agents}'
    
    def report(self):
        print(f"agent {self.code_nema} reporting. Clearance Level:{self.get_clearance_level()}", end=" ")
agent=Agent("danny",1)
# agent.report()
# agent.set_clearance_level(10)
# agent.report()



# exe2
class Mission:
    def __init__(self,mission_name:str,target_location:str,assigned_agent):
        self.mission_name=mission_name
        self.target_location=target_location
        self.assigned_agent=assigned_agent
    def brief(self):
        print(f'mission {self.mission_name} target {self.target_location} assigned agent {self.assigned_agent.code_nema}')
        
# mission=Mission("a","b",agent)
# mission.brief()

# exe3

# exe4
class FieldAgent(Agent):
    def __init__(self, code_nema, clearance_level,region:str):
        self.region=region
        super().__init__(code_nema, clearance_level)
    def report(self):
        super().report()
        print(f"region {self.region}")
          
f_agent=FieldAgent("yosuf",1,"israel")
f_agent.report()

# exe5
class CyberAgent(Agent):
    def __init__(self, code_nema, clearance_level,specialty='hacking'):
        self.specialty=specialty
        
        super().__init__(code_nema, clearance_level)
    def report(self):
        super().report()
        print(f"specialty {self.specialty}")
        
          
c_agent=CyberAgent("evyatar",1)
# c_agent.report()
agents:Agent=[agent,f_agent,c_agent]
for agent in agents:
    agent.report()


    
print(Agent.get_total_agents())

# exe7
class AgencyDirector:
    counter=None
    def __init__(self,nema):
        if AgencyDirector.counter ==None:
            self.nema=nema
            AgencyDirector.counter=""
        else:
            self.nema=("this is singleton")


a=AgencyDirector("a")
b=AgencyDirector("b")
print(a.nema)
print(b.nema)