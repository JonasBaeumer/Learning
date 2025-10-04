import { createRoot } from "react-dom/client"
import Header from "./Header"
import Footer from "./Footer"
import MainContent from "./Main"
const root = createRoot(document.getElementById("root"))

/**
 * Challenge: move the MainContent and Footer components to their own
 * separate files.
 */

function Page() {
    return (
        <>
            <Header />
            <MainContent />
            <Footer />
        </>
    )
}


root.render(
    <Page />
)


import { createRoot } from "react-dom/client"
const root = createRoot(document.getElementById("root"))

/**
 * Challenge:
 * 
 * Using flexbox, line up the `li`s horizontally and put them inline
 * with the React logo.
 * 
 * NOTE: for practice's sake, don't select any
 * elements, but use classes for all styling.
 */

function Header() {
    return (
        <header className="nav-bar">
            <img src="react-logo.png" width="40px" alt="React logo" />
            <nav>
                <ul className="nav-list">
                    <li>Pricing </li>
                    <li>About </li>
                    <li>Contact </li>
                </ul>
            </nav>
        </header>
    )
}

function MainContent() {
    return (
        <main>
            <h1>Reason I am excited to learn React</h1>
            <ol>
                <li>React is a popular library, so I will be able to fit in with all the coolest devs out there! 😎</li>
                <li>I am more likely to get a job as a front end developer if I know React</li>
            </ol>
        </main>
    )
}

function Footer() {
    return (
        <footer>
            <small>© 2024 Ziroll development. All rights reserved.</small>
        </footer>
    )
}

function Page() {
    return (
        <>
            <Header />
            <MainContent />
            <Footer />
        </>
    )
}

root.render(
    <Page />
)

import { createRoot } from "react-dom/client"
const root = createRoot(document.getElementById("root"))

/** Challenge: 
 * Move the `main` element into its own component called "MainContent" 
 * and render that component inside the Page component.
 * 
 * Do the same with the `footer` element, moving it into a new
 * component called "Footer"
*/

function Header() {
    return (
        <header>
            <img src="react-logo.png" width="40px" alt="React logo" />
        </header>
    )
}

function Main() {
    return (
        <main>
            <h1>Reason I am excited to learn React</h1>
            <ol>
                <li>React is a popular library, so I will be able to fit in with all the coolest devs out there! 😎</li>
                <li>I am more likely to get a job as a front end developer if I know React</li>
            </ol>
        </main>
    )
}

function Footer() {
    return (
        <footer>
            <small>© 2024 Ziroll development. All rights reserved.</small>
        </footer>
    )
}

function Page() {
    return (
        <>
            <Header />
            <Main/>
            <Footer />
        </>
    )
}

root.render(
    <Page />
)

import { createRoot } from "react-dom/client"
const root = createRoot(document.getElementById("root"))

/**
Challenge: 

Part 2: 
- Add a `<header>` element with an `<img />` element with the image of the 
  React logo inside (src="react-logo.png") and make sure to set the 
  width to something more manageable so it doesn't take up the whole screen.
  Also, as always, you should include some alt text on the image.
- Add an `<h1>` with some text describing the page. (E.g. "Reasons
  I'm excited to learn React"). Place it above the ordered list, then wrap
  the `<h1>` and `<ol>` inside a `<main>` element to keep our semantic
  structure flowing well.
- Add a `<footer>` after the list that says: 
    "© 20xx <last name here> development. All rights reserved."
 */


function Page() {
    return (
        <div>
            <header>
            <img src="react-logo.png" width="40px" alt="empty"/>
            </header>
            <main>
                <h1>Reasons Im excited to learn React</h1>
                <ol>
                <li>React is a popular library, so I will be able to
                fit in with all the coolest devs out there! 😎</li>
                <li>I am more likely to get a job as a front end developer
                if I know React</li>
                </ol>
            </main>
            <footer>
                © 20xx Jonas Baeumer development. All rights reserved.
            </footer>
        </div>
    )
}

root.render(
    <Page />
)

import { createRoot } from "react-dom/client"
const root = createRoot(document.getElementById("root"))

/**
 * Challenge (part 1):
 * Create a custom "Page" component
 * 
 * It should return an ordered list with the reasons why you're
 * excited to be learning React :)
 * 
 * Render the Page component.
 */

root.render(
    <Page />
)

function Page() {
    return (
        <ol> 
            <li>I am excited</li>
            <li>I love building</li>
            <li>I want to get this SE entry job so bad!</li>
        </ol>
    )
}

/*
Challenge: Starting from scratch, build and render the 
HTML for our section project. Check the Google slide for 
what you're trying to build.

We'll be adding more styling to it later.

Hints:
* The React logo is a file in the project tree, so you can
  access it by using `src="react-logo.png"` in your image
  element
* You can also set the `width` attribute of the image element
  just like in HTML. In the slide, I have it set to 40px
 */
import {createRoot} from "react-dom/client"

const root = createRoot(document.getElementById("root"))
root.render(
    <main>
        <img src="react-logo.png" width="40px"/>
        <h1>Fun facts about React!</h1>
        <ul>
            <li>Was first released in 2013</li>
            <li>Was first created by Jordan Walke</li>
            <li>Has well over 100k stars on Github</li>
            <li>Is maintained by Meta</li>
            <li>Powers thousands of enterprise apps, including mobile apps</li>
        </ul>
    </main>
)


/**
 * Challenge: set up a new React app from scratch!
 * Hints:
 * 1. Need to import the method to create a new root 
 *    from the "react-dom/client" package)
 * 2. Use that root to render some JSX. For now, just render
 *    an h1 element that says anything you want.
 */

import {createRoot} from "react-dom/client"

const root = createRoot(document.getElementById("root"))
root.render(
    <h1>Anything I want </h1>
)

/* 
Challenge - recreate the above line of code in vanilla JS by creating and
appending an h1 to our div#root (without using innerHTML).

- Create a new h1 element (createElement)
- Give it some textContent
- Give it a class name of "header"
- append it as a child (using `appendChild`) of the div#root

Don't use innerHTML to accomplish any of this.
    
*/

const newElement = document.createElement("h1")
newElement.textContent = "Hello World!"
newElement.className = "header"

const root = document.getElementById("root")
root.appendChild(newElement)

import { createRoot } from "react-dom/client"
const root = createRoot(document.getElementById("root"))

function MyAwesomeNavbar() {
    return (
        <nav className="navbar navbar-expand-sm navbar-dark bg-dark" aria-label="Third navbar example">
            <div className="container-fluid">
                <a className="navbar-brand" href="#">MyAwesomeNavbar</a>
                <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarsExample03" aria-controls="navbarsExample03" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>

                <div className="collapse navbar-collapse" id="navbarsExample03">
                    <ul className="navbar-nav me-auto mb-2 mb-sm-0">
                        <li className="nav-item">
                            <a className="nav-link active" aria-current="page" href="#">Home</a>
                        </li>
                        <li className="nav-item">
                            <a className="nav-link" href="#">Link</a>
                        </li>
                        <li className="nav-item">
                            <a className="nav-link disabled" aria-disabled="true">Disabled</a>
                        </li>
                        <li className="nav-item dropdown">
                            <a className="nav-link dropdown-toggle" href="#" data-bs-toggle="dropdown" aria-expanded="false">Dropdown</a>
                            <ul className="dropdown-menu">
                                <li><a className="dropdown-item" href="#">Action</a></li>
                                <li><a className="dropdown-item" href="#">Another action</a></li>
                                <li><a className="dropdown-item" href="#">Something else here</a></li>
                            </ul>
                        </li>
                    </ul>
                    <form role="search">
                        <input className="form-control" type="search" placeholder="Search" aria-label="Search" />
                    </form>
                </div>
            </div>
        </nav>
    )
}

function MainContent() {
    return (
        <h1>React is great!</h1>
    )
}

/**
 * Challenge:
 * Create your very first custom React component!
 * Call it "MainContent", and have it return a simple
 * h1 element that says "React is great!"
 * 
 * Afterward, render it on the line below MyAwesomeNavbar
 */

root.render(
    <div>
        <MyAwesomeNavbar />
        <MainContent />
    </div>
)
