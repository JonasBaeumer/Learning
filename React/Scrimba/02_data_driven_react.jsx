/**
 * Challenge: create a page that displays your favorite jokes
 * - Create a Joke component in its own file.
 * - Import and render 4-5 <Joke /> components
 * - Each Joke should receive a "setup" prop and a "punchline" prop
 *   and render those however you'd like
 * - Use your favorite 2-part jokes (setup & punchline), or check
 *   jokes.md file for some examples.
 * 
 * EXTRA CREDIT:
 * Some jokes are only a punchline with no setup:
 * 
 * E.g.: "It’s hard to explain puns to kleptomaniacs because 
 * they always take things literally."
 * 
 * If you don't pass in a "question" prop, how might you make it only 
 * show the punchline?
 */
import Joke from "./Joke"

export default function App() {
    return (
        <>
            <Joke setup="I got my daughter a fridge for her birthday." punchline="I can't wait to see her face light up when she opens it."/>
            <Joke setup="How did the hacker escape the police?" punchline="He just ransomware!"/>
            <Joke setup="Why don't pirates travel on mountain roads?" punchline="Scurvy."/>
            <Joke setup="Why do bees stay in the hive in the winter?" punchline="Swarm."/>
            <Joke setup="What's the best thing about Switzerland?" punchline="I don't know, but the flag is a big plus!"/>
        </>
    )
}

/**
 * Challenge: fix the bug, now that we've 
 * destructured the props object
 */
export default function Contact({img, name, phone, email}) {
    return (
        <article className="contact-card">
            <img
                src={props.img}
                alt="Photo of Mr. Whiskerson"
            />
            <h3>{props.name}</h3>
            <div className="info-group">
                <img
                    src="./images/phone-icon.png"
                    alt="phone icon"
                />
                <p>{props.phone}</p>
            </div>
            <div className="info-group">
                <img
                    src="./images/mail-icon.png"
                    alt="mail icon"
                />
                <p>{props.email}</p>
            </div>
        </article>
    )
}

const person = {
    img: "./images/mr-whiskerson.png",
    name: "Mr. Whiskerson",
    phone: "(800) 555-1234",
    email: "mr.whiskaz@catnap.meow"
}

const {img, name} = person
console.log(img)

/**
 * Challenge: Fix the code below to use the `props`
 * object values in place of the hardcoded values below
 * 
 * Note: There will be a small bug in the code, so do your
 * best to squash it! 🐛
 */

export default function Contact(props) {
    
    return (
        <article className="contact-card">
            <img
                src={props.img}
                alt={"Photo of " + props.name}
            />
            <h3>{props.name}</h3>
            <div className="info-group">
                <img
                    src="./images/phone-icon.png"
                    alt="phone icon"
                />
                <p>{props.phone}</p>
            </div>
            <div className="info-group">
                <img
                    src="./images/mail-icon.png"
                    alt="mail icon"
                />
                <p>{props.email}</p>
            </div>
        </article>
    )
}

import Contact from "./Contact"

/**
 * Challenge (I'm sorry!): Add all the rest of the
 * data to the contact card instances. 😈
 */

function App() {
    return (
        <div className="contacts">
            <Contact
                img="./images/mr-whiskerson.png"
                name="Mr. Whiskerson"
                tel="(212) 555-1234"
                mail="mr.whiskaz@catnap.meow"
            />
            <Contact 
                img="./images/fluffykins.png"
                name="FluffyKins"
                tel="(212) 555-2345"
                mail="fluff@me.com"
            />
            <Contact 
                img="./images/felix.png"
                name="Felix"
                tel="(212) 555-4567"
                mail="thecat@hotmail.com"
            />
            <Contact 
                img="./images/pumpkin.png"
                name="Pumpkin"
                tel="(0800) CAT KING"
                mail="pumpkin@scrimba.com"
            />
        </div>
    )
}

export default App


import ReactDOM from 'react-dom/client';

function App() {
  const hours = new Date().getHours()
  let timeOfDay

  if (hours < 12) {
    timeOfDay = "morning"
  } else if (hours >= 12 && hours < 17) {
    timeOfDay = "afternoon"
  } else if (hours < 21) {
    timeOfDay = "evening"
  } else {
    timeOfDay = "night"
  }
  
  /**
   * Challenge: change the hard-coded "night" to display the
   * text we determined from the logic above.
   */

  return (
    <h1>Good {timeOfDay}</h1>
  )
}

ReactDOM.createRoot(document.getElementById('root')).render(<App />);

import ReactDOM from 'react-dom/client';

function App() {
  const firstName = "Joe"
  const lastName = "Schmoe"
  
  /**
   * Challenge: finish off the h1 below so it says "Hello Joe Schmoe"
   */
  
  return (
    <h1>Hello {firstName + " " + lastName}</h1>
  )
}

ReactDOM.createRoot(document.getElementById('root')).render(<App />);

/**
 * Challenge: Build out the Entry component and render 1 instance of it
 * to the App
 * 
 * For now, just hard-code in the data, which you can find in
 * japan.md so you don't have to type it all out manually :)
 * 
 * Notes:
 * – Only render 1 instance of this Entry component for now
 * – I've pulled in marker.png for the little map marker icon
 *   that goes next to the location name
 * – The main purpose of this challenge is to show you where our limitations
 *   currently are, so don't worry about the fact that you're hard-coding all
 *   this data into the component.
 */
export default function Entry() {
    return(
        <div className="entry">
            <img src="../images/marker.png" className="entry-img" alt="fuju picture" />
            <div>
                <div className="entry-location">
                    <img src="../images/marker.png" className="entry-pointer" alt="fuju picture" />
                    <p>JAPAN</p>
                    <a href="https://www.google.com/maps/place/Mount+Fuji/@35.3606421,138.7170637,15z/data=!3m1!4b1!4m6!3m5!1s0x6019629a42fdc899:0xa6a1fcc916f3a4df!8m2!3d35.3606255!4d138.7273634!16zL20vMGNrczA?entry=ttu" className="entry-gmaps">View on Google Maps</a>
                </div>
                <h2>Mount Fuji</h2>
                <p className="entry-date">12 Jan, 2021 - 24 Jan, 2021</p>
                <p className="entry-description">Mount Fuji is the tallest mountain in Japan, standing at 3,776 meters (12,380 feet). Mount Fuji is the single most popular tourist site in Japan, for both Japanese and foreign tourists.</p>
            </div>
        </div>
    )
}
