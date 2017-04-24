"""
This is a python file created for the NoRedInk take home challenge.
It should take in a int argument through the command line and return
a list of comma-separated question ids based off of even distribution
between all three categories of strands<standards<questions. 

"""
import sys
from itertools import cycle


NUM_QUESTIONS = int(sys.argv[1])


# class Question_Tree_Node(object):
#     """tree for categorizing questions"""
#     def __init__(self, data, children=None):
#         self.children = None or []
#         self.data=data
#     def add_child(self, child):
#         self.children.append(child)
#     def __repr__(self, level=0):
#         ret = "\t"*level+repr(self.data)+"\n"
#         for child in self.children:
#             ret += child.__repr__(level+1)
#         return ret

# def retrieve_questions(num, filename):

#     questions = open(filename, 'r').readlines()[1:]

#     strands = set()


#     print questions
#     for row in questions:
#         row = row.strip()
#         items = row.split(',')
#         strands.add(items[0])
    
      

#     question_tree = Question_Tree_Node(None)
#     print strands
#     for item in strands:

#         strand_node = Question_Tree_Node(item)
#         question_tree.add_child(strand_node)
#         print question_tree, "LOOK HERE"
#         for row in questions:
#             row = row.strip()
#             items = row.split(',')
            
#             if item == items[0]:
#                 standard_node = Question_Tree_Node(items[2])
#                 strand_node.add_child(Question_Tree_Node(standard_node))
#                 # standards.add(items[2])
#                 # for standard in standards:
#                 #     if standard == items[2]:
#                 #         question_node = Question_Tree_Node(items[4])
#                 #         standard_node.add_child(question_node)


                    
#     print question_tree



set_strands = []


class Question(object):
    def __init__(self, strand, standard, question, ease):
        self.strand = strand
        self.standard = standard
        self.question = question
        self.ease = ease

def retrieve_questions(num, filename):
    
    
    total_outputted = 0

    total_result = ""

    while num > total_outputted: 
        quest_file = open(filename, 'r').readlines()[1:]
        strands = set()
        questions = []
        for row in quest_file:
            row = row.strip()
            items = row.split(',')
            question = Question(items[0], items[2], items[4], items[5])

            strands.add(items[0])


            questions.append(question)

        
        strands = list(strands)
        strand_cat = []
        cycled_strands = cycle(strands)
        seen = set()
        for i in range(num):

            current_strand = cycled_strands.next()
     
            for question in questions:
                if question.strand == current_strand and question not in seen:
                    strand_cat.append(question)
                    seen.add(question)
                    break


        standards = set()

        stan_cat = []


        question_ids = []
        result = strand_cat[0].question

        for question in strand_cat[1:]:
            result += "," + question.question
        total_result += result
        total_outputted += len(questions)

    print total_result



















retrieve_questions(NUM_QUESTIONS, 'questions.csv')


        