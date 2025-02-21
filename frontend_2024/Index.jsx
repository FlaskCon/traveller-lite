import flaskcon_logo from './assets/flaskcon-2024-animated.gif'
import bottom_clouds from './assets/bottom-clouds.png'

export default function Index() {

    return (
        <section>
            <div className={'hero'}>
                <div className={'hero-overlay'} style={{background: `url(${bottom_clouds}) repeat-x bottom`}}>
                    <img src={flaskcon_logo} alt="FlaskCon 2024 Logo."/>
                </div>
            </div>
            <section className={'container'}>
                <h1 className={'text-center my-14'}>
                    May 17th @ PyCon US 2024.
                </h1>
            </section>

            {/*<section className={'container'}>*/}
            {/*    <div className={*/}
            {/*        "flex flex-col items-center justify-center px-4 py-8 bg-blue-100 rounded-2xl border"*/}
            {/*    }>*/}
            {/*        <h2 className={"text-3xl"}>We are in room 317</h2>*/}
            {/*        <p><strong>See you there!</strong></p>*/}
            {/*    </div>*/}
            {/*</section>*/}

            <section className={'container'}>
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
                        <td>Building Single Page Apps w/Flask - Adam Englander</td>
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
                        <td>15:30 - 18:00</td>
                        <td>Office Hours - The Pallets Team</td>
                    </tr>
                    </tbody>
                </table>
            </section>
            <section>
                <div className={'container text-center'}>
                    <p className={'text-xl'}>
                        <a href="https://pyvideo.org/events/flaskcon-2024.html">
                            FlaskCon2024 on PyVideo

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
            <section className={'container text-center'}>
                <p className={'text-sm'}>Copyright &copy; 2024 FlaskCon, A PSF-registered trademark owned by
                    Pallets.</p>
            </section>
        </section>
    )

}