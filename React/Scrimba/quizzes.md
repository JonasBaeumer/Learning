
1. What do props help us accomplish?
Props help us to make our components truly reusable. Now we can use components as a component blueprint that will be dynamically populated with different data. This way we strongly reduce code duplucations as we only have to define a component once and can just create copies of it with different data that should be displayed. 


2. How do you pass a prop into a component?
<Component prop1="" prop2="" prop3="">
export default function Component(props){
    return (
        <h1>{props.prop1}{props.prop2}{props.prop3}</h1>
    )    
}


3. Can I pass a custom prop (e.g. `blahblahblah={true}`) to a native
   DOM element? (e.g. <div blahblahblah={true}>) Why or why not?
   No that is not possible, since html / dom elements are predefined and therefore have a specific set of allowed parameters that one can pass (arguments). This is unlike react where we build custom components where we can define what props we pass.

   Sample solution:
   No, because the JSX we use to describe native DOM elements will
be turned into REAL DOM elements by React. And real DOM elements
only have the properties/attributes specified in the HTML specification.
(Which doesn't include properties like `blahblahblah`)


5. How do I receive props in a component?
function Navbar(props) {
    return (
        <header>
            {props}
        </header>
    )
}


6. What data type is `props` when the component receives it?
Javascript Object

---------------------------------------------------

1. What is a React component?
A javascript object that will be embedded into html code. It is reusable so it has to be defined only once and can be reused across the codebase. 

2. What's wrong with this code?
```
function myComponent() {
    return (
        <small>I'm tiny text!</small>
    )
}
```
This code violates the coding convention for ReactComponents (the first letter should be written in capital letters)

3. What's wrong with this code?
```
function Header() {
    return (
        <header>
            <img src="./react-logo.png" width="40px" alt="React logo" />
        </header>
    )
}

root.render(Header())
```
In react convention, while we officially declare React components in the scope of functions we shouldnt call the function in the same way we call normal functions. Rather we should call it like a normal html component (e.g. <Header />)

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
the is not unified parent element, in react at multiple components at the same level must share a common parent, since 
react on render one parent element at a time. 

4. What does it mean for something to be "declarative" instead of "imperative"?
declarative -> We say what we want, but dont have to care about the how
imparative -> Have to define what and how (more tedious)

5. What does it mean for something to be "composable"?
composable -> can break it down into smaller things, and then have custom components that can be reused across the project. 
