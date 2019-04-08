class Candidate(object):
    def __init__(self, name, dept):
        self.name = name
        self.dept = dept
        
        self.officer_scores = []
        self.lead_scores = []
        self.lb_scores = []
        
        self.officer_score = -1
        self.lead_score = -1
        self.lb_score = -1
        
        self.score = -1
        
    def add_officer_score(self, evaluation):
        relationship = evaluation['How is the relationship building skills? ']
        leadership = evaluation['Leadership/Organization Ability']
        involvement = evaluation['Meeting Involvement (officer) / Meeting Effectiveness (Lead)']
        innovation = evaluation['Quality of ideas / Innovation']
        contribution = evaluation['Team Contribution']
        
        self.officer_scores.append(np.mean([relationship, leadership, involvement, innovation, contribution]) / 5.0)
    
    def add_lead_score(self, evaluation):
        relationship = evaluation['How is the relationship building skills? ']
        leadership = evaluation['Leadership/Organization Ability']
        involvement = evaluation['Meeting Involvement (officer) / Meeting Effectiveness (Lead)']
        innovation = evaluation['Quality of ideas / Innovation']
        contribution = evaluation['Team Contribution']
        
        self.lead_scores.append(np.mean([relationship, leadership, involvement, innovation, contribution]) / 5.0)
    
    def add_lb_score(self, evaluation):
        r_list = [
            evaluation['Please vote based on your assessment on the video contents.'],
            evaluation['Please vote based on your assessment on the feedback provided by the officers.'],
            evaluation['Please vote based on your knowledge about this candidate.']
        ]
        
        s_list = []
        for r in r_list:
            if type(r) == int:
                s_list.append(r)
        
        self.lb_scores.append(np.mean(s_list) / 5.0)
    
    def calculate_scores(self):
        scores = 0.0
        portions = 0.0
        
        if len(self.officer_scores) != 0:
            self.officer_score = np.mean(self.officer_scores)
            scores += self.officer_score * 0.3
            portions += 0.3
            
        if len(self.lb_scores) != 0:
            self.lb_score = np.mean(self.lb_scores)
            scores += self.lb_score * 0.3
            portions += 0.3
            
        if len(self.lead_scores) != 0:
            self.lead_score = np.mean(self.lead_scores) 
            scores += self.lead_score * 0.4
            portions += 0.4
        
        self.score = scores / portions * 100
    
    def __str__(self):
        return """name: {}
department: {}
officer_scores: {}
officer_score: {}
lead_scores: {}
lead_score: {}
lb_scores: {}
lb_score: {}
score: {}""".format(self.name, self.dept, self.officer_scores, 
                    self.officer_score, self.lead_scores, self.lead_score, 
                    self.lb_scores, self.lb_score, self.score)

