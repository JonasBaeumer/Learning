export default function Info() {
    return (
        <header className="header">
            <h2 className="header-name">Jonas Baeumer</h2>
            <h4 className="header-job">Full Stack Developer</h4>
            <p>test_mail@stanford.edu</p>
            <div className="header-bar">
                <div className="header-email">
                    <img src="./ressources/mail.png" className="header-icon" alt="Mail Icon" />
                    <p>Email</p>
                </div>
                <div className="header-linkedin">
                    <img src="./ressources/linkedin.png" className="header-icon" alt="LinkedIn Icon" />
                    <p>LinkedIn</p>
                </div>
            </div>
        </header>
    )
}
