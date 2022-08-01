class Evaluate:
  """This class validates and evaluate postfix expression.
  Attributes:
      top: An integer which denotes the index of the element at the top of the stack currently.
      size_of_stack: An integer which represents the size of stack.
      stack: A List which acts as a Stack.
  """
    # Write your code here


  def ___init___(self, size):
    """Inits Evaluate with top, size_of_stack and stack.
    Arguments:
      size_of_stack: An integer to set the size of stack.
    """
    self.top = -1
    self.size_of_stack = size
    self.stack = []


  def isEmpty(self):
    return (self.top==-1)
    """
    Check whether the stack is empty.
    Returns:
      True if it is empty, else returns False.
    """
      


  def pop(self):
    return (self.top==-1)
    """
    Do pop operation if the stack is not empty.
    Returns:
      The data which is popped out if the stack is not empty.
    """
      return (self.top==-1)


  def push(self, operand):
     self.top+=1
     self.stack[self.top]=operand
    """
    Push the operand to stack if the stack is not full.
    Arguments:
      operand: The operand to be pushed.
    """
    # Write your code here


  def validate_postfix_expression(self, expression):
    operatorcon=0
    operandcon=0
    flag=0
    for i in expression:

      if(not(i=="-" or i=="+" or i=="*" or i=="/" or i=="^")):

        k=int(i)
      if(i=="-" or i=="+" or i=="*" or i=="/" or i=="^"):

        operatorcon+=1
        flag=1
      elif(isinstance(k,int)):    
        operandcon+=1
        flag=1
      else:
        flag=0
        break
    if(flag==1 and operandcon==(operatorcon+1)):
      return True
    else:
      return False

    
    """
    Check whether the expression is a valid postfix expression.
    Arguments:
      expression: A String which represents the expression to be validated.
    Returns:
      True if the expression is valid, else returns False.
    """
    # Write your code here


  def evaluate_postfix_expression(self, expression):
    flag=0
    for i in expression:

      if(not(i=="-" or i=="+" or i=="*" or i=="/" or i=="^")):

        self.push(i)
      else:
        self.push(i)
        operator=self.pop()
        secoperator=self.pop()
        if(operator=="+"):

          self.stack[self.top]=int(self.stack[self.top])+int(secoperator)
        elif(operator=="-"):
          self.stack[self.top]=int(self.stack[self.top])-int(secoperator)
        elif(operator=="*"):
          self.stack[self.top]=int(self.stack[self.top])*int(secoperator)
        elif(operator=="/"):
          flag=1
          self.stack[self.top]=int(self.stack[self.top])/int(secoperator)
        else:
          self.stack[self.top]=int(self.stack[self.top])^int(secoperator)
    
    return int(self.stack[self.top])
    """
    Evaluate the postfix expression
    Arguments:
      expression: A String which represents the the expression to be evaluated
    Returns:
      The result of evaluated postfix expression.
    """
    # Write your code here


# Do not change the following code
postfix_expression = input()  # Read postfix expression
tokens = postfix_expression.split()
evaluate = Evaluate(len(tokens))
if evaluate.validate_postfix_expression(tokens):
    print(evaluate.evaluate_postfix_expression(tokens))
else:
    print('Invalid postfix expression')
