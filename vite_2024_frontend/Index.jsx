import flaskcon_logo from './assets/flaskcon-2024-animated.gif'
import bottom_clouds from './assets/bottom-clouds.png'
import {createSignal, onMount, Show} from "solid-js";

export default function Index() {

    const [loggedIn, setLoggedIn] = createSignal(false)
    const [conference, setConference] = createSignal({})

    const dev = import.meta.env.DEV
    const api = dev ? 'http://127.0.0.1:5001/' : '/'

    // function isLoggedIn() {
    //     fetch(api + 'api/logged-in', {
    //         method: 'GET',
    //         credentials: 'include',
    //         headers: {
    //             'Content-Type': 'application/json'
    //         }
    //     })
    //         .then(response => response.json())
    //         .then(data => {
    //             if (data.logged_in) {
    //                 setLoggedIn(true)
    //             }
    //         })
    // }
    //
    // function get_conference() {
    //     fetch(api + 'api/conference/2024', {
    //         method: 'GET',
    //         credentials: 'include',
    //         headers: {
    //             'Content-Type': 'application/json'
    //         }
    //     })
    //         .then(response => response.json())
    //         .then(jsond => {
    //             setConference(jsond)
    //         })
    // }
    //
    // onMount(() => {
    //     isLoggedIn()
    //     get_conference()
    // })

    return (
        <section>
            <div className={'hero'}>
                <div className={'hero-overlay'} style={{background: `url(${bottom_clouds}) repeat-x bottom`}}>
                    <img src={flaskcon_logo} alt="FlaskCon 2024 Logo."/>
                </div>
            </div>
            <section className={'container'}>
                <h1 className={'text-center my-14'}>
                    FlaskCon 2024 will be happening Friday, May 17 inside PyCon US 2024.
                </h1>
            </section>
            {/*
            <section className={'container mb-14'}>

                <div className={'mt-5 mb-10 text-center'}>
                    <Show when={conference().call_for_proposals_days_left > -1}
                          fallback={
                              <h2>Call for proposals have ended.</h2>
                          }>
                        <h2 className={'mb-2'}>Call for proposals are now live!</h2>
                        <p>Call for proposals will end on {conference().call_for_proposals_end_date}</p>
                    </Show>
                </div>

                <div className={'flex justify-center w-full'}>
                    {
                        loggedIn() ?
                            <div className={'flex flex-col gap-2 text-center'}>
                                <a className={'btn'} href={'https://flaskcon.com/account'}>Go to my account</a>
                            </div>
                            :
                            <div className={'flex flex-col gap-2 text-center'}>
                                <a className={'btn'} href={'https://flaskcon.com/signup'}>Signup To Join In</a>
                                <a href={'https://flaskcon.com/login'}>...or login here</a>
                            </div>
                    }
                </div>
            </section>

            {/*

            <section className={'container'}>
                <h2 className={'my-5'}>Proposal Ideas!</h2>
                <p>If you are a developer who uses or contributes to Flask,
                    Click, Jinja, or other parts of Pallets,
                    designers who work with them,
                    or sysadmins who administer them,
                    here are some talk ideas to consider:</p>
                <ul>
                    <li>HTMX</li>
                    <li>WSGI and ASGI</li>
                    <li>Accessibility</li>
                    <li>Performance</li>
                    <li>Case Studies</li>
                    <li>Your experience as a newbie</li>
                </ul>
            </section>

            <section className={'container'}>
                <h2 className={'my-5'}>Speaking Experience</h2>
                <ul>
                    <li>We are focused on accepting lightning talks this year, typically 5 - 15 mins.</li>
                    <li>
                        If your talk is accepted and you haven't secured a PyCon 2024 ticket yet,
                        you'll need to sign
                        up to acquire one for entry to the venue.
                        You can register for a
                        ticket by following <a href={'https://us.pycon.org/2024/registration/register'}>this link
                        here</a>
                    </li>
                </ul>
            </section>
            */}

            <section className={'container'}>
                <h2 className={'my-5'}>The Current Schedule (may change)</h2>
                <table>
                    <thead>
                    <tr>
                        <th>Time</th>
                        <th>Event</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr>
                        <td>11:00 - 11:30</td>
                        <td>Intro from David Lord and Q&A</td>
                    </tr>
                    <tr>
                        <td>11:45 - 12:15</td>
                        <td>Async in Flask - Phil Jones</td>
                    </tr>
                    <tr>
                        <td>12:30 - 13:00</td>
                        <td>Introduction to OpenTelemetry with Flask - Jessica Garson</td>
                    </tr>
                    <tr>
                        <td>13:00 - 14:00</td>
                        <td>Lunch</td>
                    </tr>
                    <tr>
                        <td>14:00 - 14:30</td>
                        <td>Adding OpenAPI to a Flask Application with APIFlask - Will Lachance</td>
                    </tr>
                    <tr>
                        <td>14:45 - 15:15</td>
                        <td>Extending Flask using the Flask Plugins API - Abdur-Rahmaan Janhangeer</td>
                    </tr>
                    <tr>
                        <td>15:30 - 16:00</td>
                        <td>Building Single Page Apps w/Flask - Adam Englander</td>
                    </tr>
                    <tr>
                        <td>16:00 - 16:30</td>
                        <td>Break</td>
                    </tr>
                    <tr>
                        <td>16:30 - 18:00</td>
                        <td>Office Hours - The Pallets Team</td>
                    </tr>
                    </tbody>
                </table>
            </section>
            <section className={'container text-center'}>
                <p className={'text-sm'}>Copyright &copy; 2024 FlaskCon, A PSF-registered trademark owned by
                    Pallets.</p>
            </section>
        </section>

    )

}