import stars_background from './assets/stars-background.mp4'
import flaskcon_logo_animated from './assets/flaskcon-2025-stars.gif'
import pycon_2025_logo from './assets/pyconus-logo-e.svg'

export default function Index() {


    return (
        <>
            <video autoPlay muted loop id="bg-video">

                <source src={stars_background} type="video/mp4"/>

            </video>
            <main>
                <div className={"container"}>
                    <section className={"logo-container"}>

                        <img src={flaskcon_logo_animated} alt="FlaskCon 2025 Logo."/>
                        <img src={pycon_2025_logo} className={"pyconus-logo"} alt="pycon2025 Logo."/>

                    </section>

                    <section className={"text-center p-5"}>
                        <h1>Friday May 16, 2 PM -6 PM</h1>
                        <p className={"my-2"}>Inside PyCon US 2025</p>
                    </section>

                    {/*<section className={"text-center p-2"}>*/}
                    {/*    <p>Join us in a mini conference dedicated to Flask,*/}
                    {/*        its community and ecosystem, as well as related*/}
                    {/*        web technologies. Meet maintainers and community*/}
                    {/*        members, learn about how to get involved,*/}
                    {/*        and join us during the sprint days to contribute.*/}
                    {/*        /!*Submit your talk proposal today!*!/</p>*/}

                    {/*    /!**/}
                    {/*    <a className={"a-button my-10"}*/}
                    {/*       href={"https://www.papercall.io/flaskcon-pyconus2025"}>*/}

                    {/*        Submit a talk*/}

                    {/*        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24"*/}
                    {/*             fill="none"*/}
                    {/*             stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"*/}
                    {/*             className="lucide lucide-square-arrow-out-up-right">*/}
                    {/*            <path d="M21 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h6"/>*/}
                    {/*            <path d="m21 3-9 9"/>*/}
                    {/*            <path d="M15 3h6v6"/>*/}
                    {/*        </svg>*/}

                    {/*    </a>*/}

                    {/*    <p>*/}
                    {/*        CFP closes at April 24, 2025 00:00 UTC*/}
                    {/*    </p>*/}

                    {/*    <div className={"flex flex-col items-center justify-center mt-10"}>*/}
                    {/*        <button className={"btn rounded-2xl bg-blue-400"} disabled={true}>*/}
                    {/*            CFP closed on the 26th of April*/}
                    {/*        </button>*/}
                    {/*    </div>*/}
                    {/*    *!/*/}
                    {/*</section>*/}

                    <section className={'container'}>
                        {/*<h1 className={"text-center text-3xl"}>We are in room 317</h1>*/}

                        <h2 className={"text-center text-2xl py-4"}>Schedule</h2>
                        <table>
                            <thead>
                            <tr>
                                <th>Time</th>
                                <th>Event</th>
                            </tr>
                            </thead>
                            <tbody>
                            <tr>
                                <td>14:00 - 14:30</td>
                                <td>Testing Flask and Quart Apps with Pytest and Playwright - Pamela Fox</td>
                            </tr>
                            <tr>
                                <td>14:45 - 15:15</td>
                                <td>Turning Data into an Interactive Artwork That Tells a Story - Diane Phan</td>
                            </tr>
                            <tr>
                                <td>15:30 - 16:00</td>
                                <td>Python’s New Template Strings — And Flask - Paul Everitt</td>
                            </tr>
                            <tr>
                                <td>16:00 - 16:30</td>
                                <td>Break</td>
                            </tr>
                            <tr>
                                <td>16:30 - 17:00</td>
                                <td>Let's PyScript: Flask frontends in Python! - Nicholas Tollervey &amp; Paul Everitt
                                </td>
                            </tr>
                            <tr>
                                <td>17:15 - 17:45</td>
                                <td>Death to the spinner: event sourcing for reactive web apps - Chris May</td>
                            </tr>
                            </tbody>
                        </table>

                        {/*<div className={"text-center"}>*/}
                        {/*    <p className={"py-4"}>Looking forward to seeing you!</p>*/}
                        {/*     <p className={"pb-2"}>If you can't make it on the day it would be*/}
                        {/*        great to see you at the PyCon sprints*/}
                        {/*        through Monday, May 19th to Thursday, May 22nd.*/}
                        {/*        </p>*/}
                        {/*    <p>See more info on <a target={"_blank"} href={"https://us.pycon.org/2025/events/dev-sprints/"}>*/}
                        {/*            PyCon Development Sprints*/}
                        {/*    </a></p>*/}
                        {/*</div>*/}
                    </section>

                    <section>
                        <div className={'container text-center'}>
                            <p className={'text-xl'}>
                                <a href="https://pyvideo.org/events/flaskcon-2025.html">
                                    FlaskCon2025 on PyVideo

                                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24"
                                         fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"
                                         stroke-linejoin="round" className={'inline-block ml-2'}>
                                        <path d="M15 3h6v6"/>
                                        <path d="M10 14 21 3"/>
                                        <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/>
                                    </svg>
                                </a>
                            </p>
                        </div>
                    </section>

                    <footer className={"text-center text-xs py-20"}>
                        Copyright © 2025 FlaskCon, A PSF-registered trademark owned by Pallets.
                    </footer>
                </div>
            </main>

        </>
    )

}
