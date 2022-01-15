"""
Inside conditions.json, you will see a subset of UNSW courses mapped to their 
corresponding text conditions. We have slightly modified the text conditions
to make them simpler compared to their original versions.

Your task is to complete the is_unlocked function which helps students determine 
if their course can be taken or not. 

We will run our hidden tests on your submission and look at your success rate.
We will only test for courses inside conditions.json. We will also look over the 
code by eye.

NOTE: This challenge is EXTREMELY hard and we are not expecting anyone to pass all
our tests. In fact, we are not expecting many people to even attempt this.
For complete transparency, this is worth more than the easy challenge. 
A good solution is favourable but does not guarantee a spot in Projects because
we will also consider many other criteria.
"""
import json

# NOTE: DO NOT EDIT conditions.json
with open("./conditions.json") as f:
    CONDITIONS = json.load(f)
    f.close()


# {
#     "COMP1511": "",

#     "COMP1521": "COMP1511    or DPST1091 or COMP1911 or COMP1917",
#     "COMP1531": "COMP1511 or DPST1091 or COMP1917 or COMP1921",
#     "COMP2041": "COMP1511 OR DPST1091 OR COMP1917 OR COMP1921.",
#     "COMP2521": "COMP1511    OR DPST1091 OR COMP1917 OR COMP1921",
#     "COMP3121": "COMP1927 or    COMP2521.",
#     "COMP3131": "COMP2511 or COMP2911",
#     "COMP3141": "COMP1927 or COMP2521.",
#     "COMP3153": "MATH1081",
#     "COMP3161": "COMP2521 or COMP1927",
#     "COMP3211": "COMP3222 or ELEC2141",
#     "COMP4121": "COMP3121 or   COMP3821",
#     "COMP4952": "4951",
#     "COMP4953": "4952",
#     "COMP9447": "COMP6441 or COMP6841 or COMP3441",
#     "COMP4336": "Prerequisite: COMP3331.",
#     "COMP9418": "Prerequisite:  MATH5836 or COMP9417",
#     "COMP4418": "Pre-req: COMP3411",
#     "COMP9444": "Prequisite: COMP1927 or COMP2521 or MTRN3500",

#     "COMP4161": "Completion  of 18 units of credit",
#     "COMP4951": "36 units of credit in COMP courses",
#     "COMP9301": "12 units of credit in (COMP6443,  COMP6843, COMP6445, COMP6845, COMP6447)",
#     "COMP9491": "18 units oc credit in (COMP9417, COMP9418, COMP9444, COMP9447)"

#     "COMP3901": "Prerequisite: 12 units of credit in  level 1 COMP courses and 18 units of credit in level 2 COMP courses",
#     "COMP3902": "Prerequisite: COMP3901 and 12 units of credit in level 3 COMP courses",
#     "COMP4128": "Prerequisite: COMP3821 or (COMP3121 and 12 units of credit in level 3 COMP courses)",


#     "COMP2111": "MATH1081 AND    (COMP1511 OR DPST1091 OR COMP1917 OR COMP1921)",
#     "COMP2511": "COMP1531 AND (COMP2521 OR COMP1927)",
#     "COMP4141": "Pre-requisite: MATH1081 and (COMP1927 or COMP2521)",
#     "COMP3900": "COMP1531 and (COMP2521 or COMP1927) and 102 units of credit",

#     "COMP2121": "COMP1917 OR COMP1921 OR COMP1511 OR DPST1091 OR COMP1521 OR DPST1092 OR (COMP1911 AND MTRN2500)",
#
#     "COMP3151": "COMP1927    OR ((COMP1521 or DPST1092) AND COMP2521)",
#     "COMP4601": "(COMP2511 or COMP2911) and completion of 24 units of credit",
#     "COMP9302": "(COMP6441 OR COMP6841) AND 12 units of credit in (COMP6443, COMP6843, COMP6445, COMP6845, COMP6447)",
#     "COMP9417": "MATH1081 and ((COMP1531 or COMP2041) or (COMP1927 or COMP2521))",


# }


def parseShitString(requirementsString):
    requirementsString.replace("Prerequisite: ", "")
    requirementsString.replace("Pre-requisite: ", "")
    requirementsString.replace("Pre-req: ", "")
    return requirementsString


def extractOuterBrackets(stringWithBrackets):
    return stringWithBrackets[1:-1]


def containsOne(courses_list, requirements):
    cleanedString = parseShitString(requirements)
    cleanedString = cleanedString.replace("OR", "or")
    requirementsList = cleanedString.split("or")
    cleanedRequirementsList = [c.strip() for c in requirementsList]
    print(cleanedRequirementsList)

    for course in cleanedRequirementsList:
        if course in courses_list:
            return True
    return False


def countOccurences(courses_list, target_number, requirementsString):
    requirementsString = requirementsString.strip()
    cleanedString = extractOuterBrackets(requirementsString)
    requirementsList = cleanedString.split(",")

    count = 0
    requirementsList = [c.strip() for c in requirementsList]
    for c in requirementsList:
        if c.strip() in courses_list:
            count += 1

    print(count >= target_number)
    return count >= target_number


def countOccurencesLevel(courses_list, target_number, level):
    count = 0
    pattern = "COMP" + str(level)
    for c in courses_list:
        if pattern in c:
            count += 1
    return count >= target_number


def is_unlocked(courses_list, target_course):
    """Given a list of course codes a student has taken, return true if the target_course 
    can be unlocked by them.

    You do not have to do any error checking on the inputs and can assume that
    the target_course always exists inside conditions.json

    You can assume all courses are worth 6 units of credit
    """
    total_uoc = len(courses_list) * 6
    comp_uoc = len([c for c in courses_list if "COMP" in c]) * 6

    if target_course == "1511":
        return True
    if target_course in ["COMP1521", "COMP1531", "COMP2041", "COMP2521",  "COMP2521", "COMP3121", "COMP3131", "COMP3141", "COMP3153",  "COMP3161", "COMP3211", "COMP4121", "COMP9447", "COMP9418" "COMP4336", "COMP9418", "COMP4418", "COMP9444"]:
        return containsOne(courses_list, CONDITIONS[target_course])
    if target_course == "COMP4161":
        return total_uoc >= 18
    if target_course == "COMP4951":
        return comp_uoc >= 36
    if target_course == "COMP4952":
        return "COMP4951" in courses_list
    if target_course == "COMP4953":
        return "COMP4952" in courses_list
    if target_course in ["COMP9301", "COMP9491"]:
        credits_required = int(CONDITIONS[target_course].split()[0])
        reqString = CONDITIONS[target_course].split("in")[1]

        return countOccurences(courses_list, credits_required // 6, reqString)
    if target_course == "COMP3901":
        return countOccurencesLevel(courses_list, 2, 1) and countOccurencesLevel(courses_list, 3, 2)
    if target_course == "COMP3902":
        return "COMP3901" in courses_list and countOccurences(2, 3)
    if target_course == "COMP3900":
        return "COMP1531 in" in courses_list and containsOne(courses_list, extractOuterBrackets(CONDITIONS[target_course].split("and")[1])) and total_uoc >= 102
    if target_course == "COMP2121":
        return ("COMP1911" in courses_list and "MTRN2500" in courses_list) or containsOne(courses_list, CONDITIONS[target_course].split("OR (")[0])
    if target_course == "COMP3151":
        right = extractOuterBrackets(CONDITIONS[target_course].split("OR ")[1])
        return "COMP1927" in courses_list or (containsOne(courses_list, extractOuterBrackets(right.split("AND")[0])) and 'COMP2521' in courses_list)
    if target_course == "COMP9302":
        left = CONDITIONS[target_course].split("AND")[0]
        right = CONDITIONS[target_course].split("AND")[1]
        return containsOne(courses_list, extractOuterBrackets(left.strip())) and countOccurences(courses_list, 2, right.split("in"))

    return True
