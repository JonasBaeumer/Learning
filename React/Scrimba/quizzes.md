1. Where does React put all of the elements I create in JSX when I 
   call `root.render()`?

in index.html in the <body> under the <div> named "root"

2. What would show up in my console if I were to run this line of code:
```
console.log(<h1>Hello world!</h1>)
```
<h1>Hello world!</h1>

3. What's wrong with this code:
```
root.render(
    <h1>Hi there</h1>
    <p>This is my website!</p>
)
```
the is not unified parent element, in react at multiple components at the same level must share a common parent

4. What does it mean for something to be "declarative" instead of "imperative"?
declarative -> We say what we want, but dont have to care about the how
imparative -> Have to define what and how (more tedious)

5. What does it mean for something to be "composable"?
composable -> can break it down into smaller things, and then have custom components that can be reused across the project. 
