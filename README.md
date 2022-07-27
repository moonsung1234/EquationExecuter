
# Equation Executer

-----

<br/>

## func.py

![lex_flowchart](https://user-images.githubusercontent.com/71556009/181166384-323eb0b8-884a-4518-99f6-05ddf78a9c4a.PNG)

- get equation argument 
- split equation as characters
- return token list after setting characters' tokens

<br/>
<br/>

![parse_flowchart](https://user-images.githubusercontent.com/71556009/181166394-3b3aa0c1-ce1e-4f8b-b767-ef6bd95be554.PNG)

- make element(execution, token) tree and return it

<br/>
<br/>

![execute_flowchart](https://user-images.githubusercontent.com/71556009/181166398-778c3185-8fdd-481f-a533-3d401f77eba9.PNG)

- get top element of element tree
- make equation function through tree search
- put input value into function and return that value

<br/>
<br/>