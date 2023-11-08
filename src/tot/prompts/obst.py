#5-shot
standard_prompt = '''Given an array k and an array freq where k contains key values from 1 to n
and freq the respective frequencies for the use of these keys. Construct an 
optimal binary search tree to minimize the average search time for the key values.
Output only the JSON representation of the optimal binary search tree.
No further explanation needed.

Input: k=[1,2,3], freq=[3,7,2]
Answer: [2, [1, null, null],
            [3, null, null]]
            
Input: k=[1,2,3], freq=[6,4,9]
Answer: [3, [1, null,
                [2, null, null]],
            null]
            
Input: k=[1,2,3,4,5], freq=[11,8,6,10,4]
Answer: [2, [1, null, null],
            [4, [3, null, null],
                [5, null, null]]]
                
Input: k=[1,2,3,4,5,6,7], freq=[4,13,8,22,9,2,32]
Answer: [4, [2, [1, null, null],
                [3, null, null]],
            [7, [5, null,
                    [6, null, null]],
                null]]
                
Input: k=[1,2,3,4,5,6,7,8,9], freq=[7,1,9,4,3,8,2,5,6]
Answer:  [6, [3, [1, null,
                    [2, null, null]],
                [4, null,
                    [5, null, null]]],
            [8, [7, null, null],
                [9, null, null]]]

Input: {input}
Answer: 
'''

#5-shot
cot_prompt = '''Given an array k and an array freq where k contains key values
and freq the respective frequencies for the use of the keys. Construct an 
optimal binary search tree to minimize the average search time for the key values.
Output the array representing the optimal binary search tree. 
Construct the binary tree stepwise from top to bottom. With each step, try to 
estimate which new nodes can minimize the total costs the most.

Input: k=[1,2,3], freq=[3,7,2]
Steps: Your step-by-step solution
Answer: [2, [1, null, null],
            [3, null, null]]
            
Input: k=[1,2,3], freq=[6,4,9]
Steps: Your step-by-step solution
Answer: [3, [1, null,
                [2, null, null]],
            null]
            
Input: k=[1,2,3,4,5], freq=[11,8,6,10,4]
Steps: Your step-by-step solution
Answer: [2, [1, null, null],
            [4, [3, null, null],
                [5, null, null]]]
                
Input: k=[1,2,3,4,5,6,7], freq=[4,13,8,22,9,2,32]
Steps: Your step-by-step solution
Answer: [4, [2, [1, null, null],
                [3, null, null]],
            [7, [5, null,
                    [6, null, null]],
                null]]
                
Input: k=[1,2,3,4,5,6,7,8,9], freq=[7,1,9,4,3,8,2,5,6]
Steps: Your step-by-step solution
Answer:  [6, [3, [1, null,
                    [2, null, null]],
                [4, null,
                    [5, null, null]]],
            [8, [7, null, null],
                [9, null, null]]]

Input: {input}
Steps:
Answer:
'''

#1-shot
propose_prompt = '''Input: k=[1,2,3,4,5], freq=[11,8,6,10,4], and the partially created tree [2, ...]
Possible next steps in the Optimal Binary Tree Construction:
[2, [1, ...], [3, ...]]
[2, [1, ...], [4, ...]]
[2, [1, ...], [5, ...]]
[2, null, [3, ...]]
[2, null, [4, ...]]
[2, null, [5, ...]]
[2, [1, ...], null]
Input: {input}
Possible next steps in the Optimal Binary Tree Construction:
'''

value_prompt = '''Given a partially constructed binary tree, evaluate whether it has a chance of becoming
the Optimal Binary Search Tree and how high that chance is. Give an estimator value representing this chance.
The estimator value must be an integer between 1 and 10 where 1 indicates a very low chance, and 10 a very high chance.

Input: k=[1,2,3], freq=[3,7,2], and the partially created tree [2, ...]
Reasoning: The key value 2 has the highest frequency and is in the middle of the values of the key array. 
Judgement: 9

Input: k=[1,2,3], freq=[6,4,9], and the partially created tree [1, ...]
Reasoning: The key value 1 only has the second-highest frequency and is not in the middle of the values of the key array.
Judgement: 3

Input: k=[1,2,3,4,5], freq=[11,8,6,10,4], and the partially created tree [2, [1, ...], [4, ...]]
Reasoning: The root of the partially created tree has the value 2. It is not exactly in the middle of the array
of keys, but it can still split it in half almost perfectly. Also, it has a modestly high frequency value.
Jugement pobably likely. But the key values 1 and 4 are on the second level of the tree, and they have
the two highest frequency numbers of all the key values. Additionally, the key value 4 splits the partial
array [3,4,5] very well in half.
Judgement: 8

Input: {input}
Reasoning:
Judgement: {{Fill in your estimator value here. Value must be an integer between 1 and 10}}
'''


'''Input: k=[1,2,3,4,5,6,7], freq=[4,13,8,22,9,2,32], and the partially created tree [2, [1, ...], [4, [5, ...]]]
The root of the partially created tree has the value 2. It does not split the array of keys in half very well.
Additionally, the key 2 only has the third-hightest frequency value among all keys. 
In the right sub-tree, the value 4 does not split the array on the right side of 2 very well either, and
although it has the second-highest frequency, the key value 7 still has a significantly higher frequency.
less likely

Input: k=[1,2,3,4,5,6,7,8,9], freq=[7,1,9,4,3,8,2,5,6], and the partially created tree [6, [3, ...], [8, ...]]
The root of the partially created tree has the value 6. It does not split the array of keys in the middle,
but is still in a reasonable position to be considered the root node. Additionally, its frequency value
is the second-highest among all frequency values. In the left sub-tree, the key with the value 3 splits
the remaining left array in half very well and has the highest frequency. In the right sub-array, the 
key with the value 5 is in the middle and has a relatively high frequency.
So the root node is a bit suspicious, but the partially created tree still has a good chance of becoming
the optimal binary search tree for the given input.
likely'''

value_last_step_prompt = '''Given an array k and an array freq where k contains key values
and freq the respective frequencies for the use of the keys. Construct an 
optimal binary search tree to minimize the average search time for the key values.
Output only the array representing the optimal binary search tree. 
No further explanation needed.

Input: k=[1,2,3], freq=[3,7,2]
Answer: [2, [1, null, null],
            [3, null, null]]
            
Input: k=[1,2,3], freq=[6,4,9]
Answer: [3, [1, null,
                [2, null, null]],
            null]
            
Input: k=[1,2,3,4,5], freq=[11,8,6,10,4]
Answer: [2, [1, null, null],
            [4, [3, null, null],
                [5, null, null]]]
                
Input: k=[1,2,3,4,5,6,7], freq=[4,13,8,22,9,2,32]
Answer: [4, [2, [1, null, null],
                [3, null, null]],
            [7, [5, null,
                    [6, null, null]],
                null]]
                
Input: k=[1,2,3,4,5,6,7,8,9], freq=[7,1,9,4,3,8,2,5,6]
Answer:  [6, [3, [1, null,
                    [2, null, null]],
                [4, null,
                    [5, null, null]]],
            [8, [7, null, null],
                [9, null, null]]]
'''


