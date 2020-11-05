from deeppavlov.deprecated.skills.pattern_matching_skill import PatternMatchingSkill
from deeppavlov.deprecated.agents.default_agent import DefaultAgent
from deeppavlov.deprecated.agents.processors.highest_confidence_selector import HighestConfidenceSelector

hello = PatternMatchingSkill(responses=['Hello world!'], patterns=["hi", "hello", "good day"])
bye = PatternMatchingSkill(['Goodbye world!', 'See you around'], patterns=["bye", "chao", "see you"])
fallback = PatternMatchingSkill(["I don't understand, sorry"])

agent = DefaultAgent([hello, bye, fallback], skills_selector=HighestConfidenceSelector())

print(agent(['HellSo deAR', 'Bye', 'Or not']))

hello = PatternMatchingSkill(responses=["Hello world!"], patterns=["(hi|hello|good day)"], regex=True)
sorry = PatternMatchingSkill(responses=["don’t be sorry", "Please don’t"], patterns=["(sorry|excuse)"], regex=True)
perhaps = PatternMatchingSkill(responses=["Please be more specific"], patterns=["(.*)perhaps(.*)"], regex=True)

agent = DefaultAgent([hello, sorry, perhaps], skills_selector=HighestConfidenceSelector())
print(agent(['hi, how are you', 'I am sorry', 'perhaps I am not sure']))

# print(agent([input("Enter some Words(hi, how are you, I am sorry, perhaps):")]))
