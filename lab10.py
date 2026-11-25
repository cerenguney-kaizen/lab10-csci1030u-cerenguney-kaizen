# Problem-solving practice 2 (competition / LeetCode style) - a step up in difficulty.
#
# Most of these are natural fits for a STACK or a QUEUE (this week's data structures).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def eval_rpn(tokens):
    # Outline (write your plan here first):
    #   Restate: I get a list of strings. Each string is a number or one of
    #     + - * /. The operator comes after its two numbers (postfix).
    #     I have to calculate the result and return it as an integer.
    #   Example: ["4","13","5","/","+"]
    #     "4"  number, push        stack: [4]
    #     "13" number, push        stack: [4, 13]
    #     "5"  number, push        stack: [4, 13, 5]
    #     "/"  pop 5, pop 13, 13/5 = 2, push 2    stack: [4, 2]
    #     "+"  pop 2, pop 4, 4+2 = 6, push 6      stack: [6]
    #     Answer: 6 (the last item left in the stack)
    #   Approach: A stack fits because an operator always uses the two MOST
    #     RECENT numbers, and the last one pushed is the first one popped.
    #     Steps: make an empty list as a stack. Go through the tokens.
    #     If the token is a number, convert it with int() and append it.
    #     If it is an operator, pop b first (right side), then pop a (left side),
    #     calculate a (op) b, and append the result. For "/" use int(a / b)
    #     so it truncates toward zero. At the end, return the one number left.
    stack = []                          # boş stack (tabak yığını)
    for token in tokens:                
        if token in ("+", "-", "*", "/"):           
            b = stack.pop()        
            a = stack.pop()         
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            else:                       
                stack.append(int(a / b))  
        else:                          
            stack.append(int(token))   
    return stack[0]                    


def decode_string(s):
    # Outline:
    #   Restate: The string has the rule k[text], meaning text repeated k times.
    #   Brackets can be inside other brackets. I have to return the decoded string.
    #   Example: "3[a2[c]]" -> inside the inner [ ] I get "cc", so "acc",
    #   then the outer 3 repeats it -> "accaccacc"
    #   Approach: A stack fits because when I see "[" I must remember the
    #   text and the number from OUTSIDE, then work on the inside. When I see "]"
    #   I go back to the most recent outside context (last in, first out).
    stack = []
    current = ""                   
    num = 0                        
    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)        
        elif ch == "[":
            stack.append((current, num))   
            current = ""
            num = 0
        elif ch == "]":
            prev, k = stack.pop()          
            current = prev + current * k   
        else:
            current += ch                 
    return current


def daily_temperatures(temps):
        # Outline:
    #   Restate: For each day I must find how many days until a warmer day.
    #   If there is no warmer day, the answer is 0.
    #   Example: [30,40,50,60] -> every day is followed by a warmer day
    #   the next day, so [1,1,1,0].
    #   Approach: A stack fits because I need the most recent day that is
    #   still waiting for a warmer day. I keep the INDEXES of waiting days.
    #   When today is warmer than the day on top, that day stops waiting:
    #   pop it and set its answer to today - that_day.
    result = [0] * len(temps)               # başta hepsi 0
    stack = []                             
    for i in range(len(temps)):             
        while stack and temps[i] > temps[stack[-1]]:  
            j = stack.pop()                
            result[j] = i - j             
        stack.append(i)                    
    return result


def num_islands(grid):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: `grid` is a list of equal-length strings of "1" (land) and "0" (water).
    #   Count the islands - groups of "1"s connected up/down/left/right (not diagonally).
    #   Example: ["11000","11000","00100","00011"]  ->  3
    pass


def main():
    # Optional scratch space - try your functions here, then run: python lab10.py
    # print(eval_rpn(["2", "1", "+", "3", "*"]))   # 9
    pass


if __name__ == "__main__":
    main()
