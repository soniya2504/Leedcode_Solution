class MinStack(object):
    """
    Implements a stack that supports O(1) push, pop, top, and getMin.
    Uses two internal lists (stacks): one for all data and one for tracking the minimums.
    """
    def __init__(self):
        # The primary stack to store all elements
        self.data_stack = []
        # The auxiliary stack to store the minimum element seen so far at each stage
        self.min_stack = []

    def push(self, val):
        """
        Pushes the element onto the data stack. Updates the min_stack if the new 
        value is less than or equal to the current minimum.
        Time Complexity: O(1)
        """
        self.data_stack.append(val)
        
        # Check if the min_stack is empty OR if the new value is the new minimum
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        """
        Removes the top element from the data stack. If the popped element was 
        the current minimum, it is also removed from the min_stack.
        Time Complexity: O(1)
        """
        # We assume the stack is non-empty per problem constraints, but a check is good practice.
        if self.data_stack:
            popped_value = self.data_stack.pop()

            # If the value popped from the data stack is the same as the current minimum,
            # we must also pop from the min_stack to expose the previous minimum.
            if popped_value == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self):
        """
        Gets the top element of the data stack.
        Time Complexity: O(1)
        """
        # Returns the last element of the data_stack.
        return self.data_stack[-1]

    def getMin(self):
        """
        Retrieves the minimum element in the stack. This is always the top of the min_stack.
        Time Complexity: O(1)
        """
        # Returns the last element of the min_stack.
        return self.min_stack[-1]

# Example of how the methods work internally:
# 1. Push -2: data_stack=[-2], min_stack=[-2]
# 2. Push 0:  data_stack=[-2, 0], min_stack=[-2] (0 is not <= -2)
# 3. Push -3: data_stack=[-2, 0, -3], min_stack=[-2, -3] (-3 <= -2)
# 4. getMin(): returns -3
# 5. pop():   data_stack removes -3. min_stack removes -3 (since -3 == -3).
#             data_stack=[-2, 0], min_stack=[-2]
# 6. top():   returns 0
# 7. getMin(): returns -2